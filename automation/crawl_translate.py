#!/usr/bin/env python3
"""
MS KR Security Blog — auto crawler + translator.

Pipeline:
  1. Fetch the Microsoft Security Blog RSS feed.
  2. For each new item (not in state/processed.json), read its <category> tags.
  3. Map tags -> solution -> owner using _data/solution_owners.yml.
     Only ENABLED solutions are processed (test scope: Security Copilot + Agent 365).
     Items matching no enabled solution are skipped (test mode).
  4. Translate title + body to Korean via Azure OpenAI (chat completions).
     If Azure OpenAI env vars are absent, fall back to a passthrough stub so the
     pipeline is still testable end-to-end.
  5. Write a Chirpy-compatible Markdown post into _posts/.
  6. Print a JSON summary (consumed by the GitHub Actions workflow to build the
     Teams approval card and decide reviewers).

Usage:
  python crawl_translate.py --max 3            # process up to 3 new items
  python crawl_translate.py --dry-run          # don't write posts/state, just report
  python crawl_translate.py --all-solutions    # ignore `enabled` flags (prod)

Env (translation):
  AZURE_OPENAI_ENDPOINT   e.g. https://my-aoai.openai.azure.com
  AZURE_OPENAI_KEY        api key (or use AZURE_OPENAI_AD_TOKEN)
  AZURE_OPENAI_DEPLOYMENT e.g. gpt-4o
  AZURE_OPENAI_API_VERSION (optional, default 2024-10-21)
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
import re
import sys
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from pathlib import Path

try:
    import yaml  # PyYAML
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "_posts"
STATE_FILE = Path(__file__).resolve().parent / "state" / "processed.json"
OWNERS_FILE = ROOT / "_data" / "solution_owners.yml"

FEED_URL = "https://www.microsoft.com/en-us/security/blog/feed/"
USER_AGENT = "ms-kr-security-blog-bot/1.0 (+https://akimcse.github.io/securitykorea)"

NS = {
    "content": "http://purl.org/rss/1.0/modules/content/",
    "dc": "http://purl.org/dc/elements/1.1/",
}


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def load_owners() -> dict:
    with open(OWNERS_FILE, encoding="utf-8-sig") as fh:
        return yaml.safe_load(fh)


def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8-sig"))
    return {"processed": {}}


def save_state(state: dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def fetch_feed() -> str:
    req = urllib.request.Request(FEED_URL, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", errors="replace")


def parse_items(xml_text: str) -> list[dict]:
    root = ET.fromstring(xml_text)
    items = []
    for it in root.findall("./channel/item"):
        guid = (it.findtext("guid") or it.findtext("link") or "").strip()
        title = (it.findtext("title") or "").strip()
        link = (it.findtext("link") or "").strip()
        pub = (it.findtext("pubDate") or "").strip()
        creator = (it.findtext("dc:creator", namespaces=NS) or "").strip()
        body_html = it.findtext("content:encoded", namespaces=NS) or it.findtext("description") or ""
        tags = [ (c.text or "").strip() for c in it.findall("category") if (c.text or "").strip() ]
        items.append({
            "guid": guid, "title": title, "link": link, "pubDate": pub,
            "creator": creator, "body_html": body_html, "tags": tags,
        })
    return items


def match_solution(tags: list[str], owners_cfg: dict, all_solutions: bool) -> tuple[str | None, dict | None]:
    """Return (solution_key, solution_cfg) for the first enabled solution whose
    tag substrings match any of the item's feed tags. None if no match."""
    low_tags = [t.lower() for t in tags]
    for key, cfg in owners_cfg.get("solutions", {}).items():
        if not all_solutions and not cfg.get("enabled", False):
            continue
        for needle in cfg.get("tags", []):
            n = needle.lower()
            if any(n in t for t in low_tags):
                return key, cfg
    return None, None


def html_to_markdown(body_html: str) -> str:
    """Lightweight HTML -> Markdown. Good enough for the WordPress block markup
    in the MS Security feed; the heavy lifting (clean prose) is done by the LLM."""
    text = body_html
    text = re.sub(r"<figure.*?>.*?</figure>", "", text, flags=re.S)
    text = re.sub(r"<script.*?>.*?</script>", "", text, flags=re.S)
    text = re.sub(r"<h2[^>]*>(.*?)</h2>", r"\n\n## \1\n\n", text, flags=re.S)
    text = re.sub(r"<h3[^>]*>(.*?)</h3>", r"\n\n### \1\n\n", text, flags=re.S)
    text = re.sub(r"<li[^>]*>(.*?)</li>", r"- \1\n", text, flags=re.S)
    text = re.sub(r"<a [^>]*href=\"(.*?)\"[^>]*>(.*?)</a>", r"[\2](\1)", text, flags=re.S)
    text = re.sub(r"<blockquote[^>]*>(.*?)</blockquote>", r"\n> \1\n", text, flags=re.S)
    text = re.sub(r"</p>", "\n\n", text)
    text = re.sub(r"<[^>]+>", "", text)              # strip remaining tags
    text = html.unescape(text)
    text = re.sub(r"\u00a0", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


# --------------------------------------------------------------------------- #
# Translation
# --------------------------------------------------------------------------- #
def translate_korean(title: str, body_md: str) -> tuple[str, str]:
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    key = os.getenv("AZURE_OPENAI_KEY")
    deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-10-21")

    if not (endpoint and deployment and (key or os.getenv("AZURE_OPENAI_AD_TOKEN"))):
        # Fallback stub so the pipeline runs without credentials during testing.
        note = "> ⚠️ 번역 엔진(Azure OpenAI) 미설정 — 원문 그대로 표시(테스트 스텁).\n\n"
        return f"[KO] {title}", note + body_md

    url = f"{endpoint.rstrip('/')}/openai/deployments/{deployment}/chat/completions?api-version={api_version}"
    sys_prompt = (
        "You are a professional Korean technical translator for Microsoft security content. "
        "Translate the given English Markdown into natural, professional Korean. "
        "Keep Markdown structure, links, code, and product names (e.g. Microsoft Defender, "
        "Microsoft Sentinel, Security Copilot, Microsoft Entra) intact. Do not add commentary. "
        "Return ONLY a JSON object: {\"title\": \"...\", \"body\": \"...\"}."
    )
    user_prompt = json.dumps({"title": title, "body": body_md}, ensure_ascii=False)

    payload = {
        "messages": [
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": 0.2,
        "response_format": {"type": "json_object"},
        "max_tokens": 4000,
    }
    headers = {"Content-Type": "application/json"}
    if key:
        headers["api-key"] = key
    else:
        headers["Authorization"] = f"Bearer {os.getenv('AZURE_OPENAI_AD_TOKEN')}"

    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"),
                                 headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    content = data["choices"][0]["message"]["content"]
    obj = json.loads(content)
    return obj.get("title", title), obj.get("body", body_md)


# --------------------------------------------------------------------------- #
# Post writing
# --------------------------------------------------------------------------- #
def slugify(title: str) -> str:
    s = re.sub(r"[^\w\s-]", "", title.lower())
    s = re.sub(r"[\s_-]+", "-", s).strip("-")
    return s[:60] or "post"


def yaml_list(items: list[str]) -> str:
    return "[" + ", ".join(json.dumps(i, ensure_ascii=False) for i in items) + "]"


def write_post(item: dict, solution_key: str, solution_cfg: dict,
               ko_title: str, ko_body: str, dry_run: bool) -> Path:
    try:
        pub_dt = dt.datetime.strptime(item["pubDate"], "%a, %d %b %Y %H:%M:%S %z")
    except (ValueError, KeyError):
        pub_dt = dt.datetime.now(dt.timezone.utc)
    date_str = pub_dt.strftime("%Y-%m-%d")
    fm_date = pub_dt.strftime("%Y-%m-%d %H:%M:%S %z")
    slug = slugify(item["title"])
    fname = f"{date_str}-{slug}.md"
    path = POSTS_DIR / fname

    categories = [solution_cfg["label"]]
    tags = item["tags"][:8] if item["tags"] else [solution_key]
    owners = solution_cfg.get("owners", [])

    front = [
        "---",
        f'title: {json.dumps(ko_title, ensure_ascii=False)}',
        f"date: {fm_date}",
        f"categories: {yaml_list(categories)}",
        f"tags: {yaml_list([t.lower() for t in tags])}",
        f"solution: {solution_key}",
        f"owners: {yaml_list(owners)}",
        f'source_url: {json.dumps(item["link"])}',
        f'source_author: {json.dumps(item["creator"], ensure_ascii=False)}',
        "auto_generated: true",
        "pin: false",
        "---",
        "",
    ]
    attribution = (
        f"> 본 글은 Microsoft Security Blog의 [{item['title']}]({item['link']}) "
        f"글을 한국어로 번역·정리한 것입니다. 원문 작성자: {item['creator'] or 'Microsoft'}.\n"
        "{: .prompt-info }\n\n"
    )
    content = "\n".join(front) + attribution + ko_body + "\n"

    if not dry_run:
        POSTS_DIR.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    return path


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max", type=int, default=5, help="max new items to process")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--all-solutions", action="store_true", help="ignore enabled flags")
    args = ap.parse_args()

    owners_cfg = load_owners()
    state = load_state()
    processed = state.setdefault("processed", {})

    xml_text = fetch_feed()
    items = parse_items(xml_text)

    results = []
    count = 0
    for item in items:
        if count >= args.max:
            break
        if item["guid"] in processed:
            continue
        sol_key, sol_cfg = match_solution(item["tags"], owners_cfg, args.all_solutions)
        if not sol_key:
            # Test scope: skip anything outside enabled solutions.
            continue

        ko_title, ko_body = translate_korean(item["title"], html_to_markdown(item["body_html"]))
        path = write_post(item, sol_key, sol_cfg, ko_title, ko_body, args.dry_run)

        owners = sol_cfg.get("owners", []) or [owners_cfg.get("default_owner")]
        results.append({
            "guid": item["guid"],
            "source_title": item["title"],
            "ko_title": ko_title,
            "solution": sol_key,
            "solution_label": sol_cfg["label"],
            "owners": owners,
            "source_url": item["link"],
            "post_path": str(path.relative_to(ROOT)).replace("\\", "/"),
        })
        if not args.dry_run:
            processed[item["guid"]] = {
                "title": item["title"],
                "solution": sol_key,
                "processed_at": dt.datetime.now(dt.timezone.utc).isoformat(),
                "post_path": str(path.relative_to(ROOT)).replace("\\", "/"),
            }
        count += 1

    if not args.dry_run:
        save_state(state)

    summary = {"new_posts": results, "count": len(results)}
    print(json.dumps(summary, ensure_ascii=False, indent=2))

    # Expose results to GitHub Actions via the step output file.
    gh_out = os.getenv("GITHUB_OUTPUT")
    if gh_out:
        with open(gh_out, "a", encoding="utf-8") as fh:
            fh.write(f"count={len(results)}\n")
            fh.write("posts<<EOF\n")
            fh.write(json.dumps(results, ensure_ascii=False))
            fh.write("\nEOF\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
