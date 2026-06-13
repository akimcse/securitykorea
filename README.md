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
        ├─ 변경분 브랜치 push → PR 생성
        └─ 담당자를 PR 리뷰어로 지정 → GitHub가 담당자에게 이메일/알림 발송
   └─ (담당자가 PR 검토 후 머지 = 승인)
   └─ .github/workflows/stamp-author.yml
        └─ 머지 시 author=머지한 사람 기입 → Pages 재빌드 트리거
   └─ .github/workflows/pages-deploy.yml
        ├─ Jekyll 빌드 + html-proofer 검사
        └─ GitHub Pages 게시  ← main에 머지된 글만 게시됨
```

## 승인 게이트 (PR 머지 = 승인)

자동/수동 글은 모두 **Pull Request로 올라옵니다.** 담당자는 PR의 "Files changed"에서
번역문·내용을 직접 검토한 뒤 **머지하면 그것이 곧 승인**입니다. 머지되지 않은 글은
`main`에 들어가지 못하므로 게시되지 않습니다 — "담당자 승인 없이는 게시하지 않음"을 충족합니다.

> 머지 권한이 있는 사람(= 솔루션 담당자)만 게시를 확정할 수 있습니다.

## 알림 (GitHub 네이티브 — 이메일)

자동 게시 PR이 생성되면 워크플로가 해당 글의 솔루션 담당자를 **PR 리뷰어로 지정**합니다.
그러면 GitHub가 담당자에게 **리뷰 요청 이메일**(및 웹/모바일 알림)을 보냅니다. 별도의
webhook이나 외부 서비스가 필요 없어 회사 DLP 정책의 영향을 받지 않습니다.

> 리뷰어로 지정하려면 해당 담당자의 GitHub 로그인이 이 레포의 collaborator여야 합니다.
> `_data/solution_owners.yml`의 `owners` 값이 실제 GitHub 로그인과 일치해야 알림이 갑니다
> (일치하지 않는 placeholder는 자동으로 건너뜀).

## 작성자 = 머지한 사람

PR이 머지되면 `.github/workflows/stamp-author.yml`이 **머지한 사람의 GitHub 로그인**을
각 포스트의 `author` front matter로 기입하고, Pages 재빌드를 트리거합니다.
표시 이름은 `_data/authors.yml`에서 매핑합니다(예: `akimcse` → **Hyuna Kim**).
새 기여자가 처음 머지하면 `_data/authors.yml`에 한 줄만 추가하면 됩니다.

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

> Secret이 없어도 파이프라인은 동작합니다. 번역 엔진이 없으면 원문을 그대로 표시하는
> 테스트 스텁으로 대체됩니다. 알림은 GitHub 네이티브(리뷰어 지정 → 이메일)라 별도 secret이 필요 없습니다.

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
