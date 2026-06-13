# MS KR Security Blog

[Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/)의 주요 글을
한국어로 번역·정리하고, 한국 마이크로소프트 보안 팀의 솔루션별 인사이트를 전달하는 기술 블로그입니다.

> **상태**: 개인 계정(`akimcse`)에서 전체 워크플로우를 검증하는 **테스트 단계**입니다.
> 현재 자동 게시 대상은 **Security Copilot · Agent 365** 두 솔루션뿐입니다.

- 사이트: https://akimcse.github.io/securitykorea
- 테마: [Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy)

---

## 아키텍처

```
매일 1회(cron) 또는 수동 실행
   └─ automation/crawl_translate.py
        ├─ Microsoft Security Blog RSS 수집
        ├─ <category> 태그 → 솔루션 → 담당자 매핑 (_data/solution_owners.yml)
        ├─ Azure OpenAI로 한국어 번역
        └─ _posts/*.md 생성 + 중복 방지(state/processed.json)
   └─ .github/workflows/auto-post.yml
        ├─ 변경분 브랜치 push → Draft PR 생성
        └─ 담당자에게 Teams 승인 카드 발송
   └─ (담당자가 PR 머지 = 1차 승인)
   └─ .github/workflows/pages-deploy.yml
        ├─ Jekyll 빌드 + html-proofer 검사
        └─ deploy 잡: github-pages 환경의 'required reviewer'(담당자) 승인 대기
             → 승인 시에만 GitHub Pages 게시  ← 담당자 승인 없이는 게시 안 됨
```

## 승인 게이트 (Option A — GitHub Environment)

`Settings → Environments → github-pages`에서 **Required reviewers**에 담당자의
GitHub 계정을 추가하면, `deploy` 잡이 그 사람의 승인을 받기 전까지 멈춥니다.
테스트 단계에서는 `akimcse` 한 명만 지정합니다.

## 솔루션 → 담당자 매핑

`_data/solution_owners.yml` 한 파일에서 관리합니다(사이트와 크롤러가 공유).

| 솔루션 | 담당(GitHub) | 테스트 활성화 |
| --- | --- | --- |
| Security Copilot | akimcse | ✅ |
| Agent 365 | akimcse | ✅ |
| Purview | byungtae | ⛔ |
| Defender / Sentinel | jonggi | ⛔ |
| Entra / Intune | sanghyeok | ⛔ |

## 필요한 GitHub Secrets

| 이름 | 용도 |
| --- | --- |
| `AZURE_OPENAI_ENDPOINT` | 번역용 Azure OpenAI 엔드포인트 |
| `AZURE_OPENAI_KEY` | API 키 (또는 AAD 토큰) |
| `AZURE_OPENAI_DEPLOYMENT` | 배포 이름 (예: `gpt-4o`) |
| `AZURE_OPENAI_API_VERSION` | (선택) 기본 `2024-10-21` |
| `TEAMS_WEBHOOK_URL` | Teams 승인 카드 발송 webhook |

> Secret이 없어도 파이프라인은 동작합니다. 번역 엔진이 없으면 원문을 그대로 표시하는
> 테스트 스텁으로 대체되고, Teams webhook이 없으면 알림 단계만 건너뜁니다.

## 수동 포스팅

1. `_drafts/_template.md`를 복사해 `_posts/yyyy-mm-dd-제목.md`로 저장합니다.
2. front matter의 `categories` / `tags` / `solution` / `owners`를 채웁니다.
3. PR을 올리면 동일한 검수·승인 과정을 거쳐 게시됩니다.

## 로컬 미리보기

```bash
bundle install
bundle exec jekyll serve --livereload
# http://127.0.0.1:4000/securitykorea/
```

## 크롤러 수동 실행

```bash
pip install -r automation/requirements.txt
python automation/crawl_translate.py --max 5            # 테스트 범위(활성 솔루션만)
python automation/crawl_translate.py --all-solutions    # 전체 솔루션
python automation/crawl_translate.py --dry-run          # 파일/상태 변경 없이 미리보기
```
