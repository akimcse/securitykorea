---
title: "Microsoft Build 2026: 개발 수명 주기 전반에서 코드·에이전트·모델 보호하기"
date: 2026-06-02 17:15:18 +0000
categories: ["Agent 365"]
tags: ["github", "microsoft agent 365", "security strategies"]
solution: agent-365
owners: ["akimcse"]
source_url: "https://www.microsoft.com/en-us/security/blog/2026/06/02/microsoft-build-2026-securing-code-agents-and-models-across-the-development-lifecycle/"
source_author: "Aleš Holeček"
auto_generated: true
pin: false
---

> 본 글은 Microsoft Security Blog의 [Microsoft Build 2026: Securing code, agents, and models across the development lifecycle](https://www.microsoft.com/en-us/security/blog/2026/06/02/microsoft-build-2026-securing-code-agents-and-models-across-the-development-lifecycle/) 글을 한국어로 번역·정리한 것입니다. 원문 작성자: Aleš Holeček.
{: .prompt-info }

오늘날 개발자와 보안 팀은 점점 커지는 긴장 속에 놓여 있습니다. AI는 개발 속도를 끌어올리는 동시에, 안전하지 않은 코드, 불투명한 모델, 데이터 노출, 컴플라이언스와 관련한 새로운 문제를 함께 가져옵니다. 여기에 섀도 AI(shadow AI)와 도구 난립(tool sprawl)이라는 과제까지 더해지면, 혁신과 통제 사이의 간극은 더욱 벌어집니다. 개발자가 더 빨리 움직일수록 보안 팀은 가시성·거버넌스·감독을 따라잡기 어려워집니다. 그 결과 개발 수명 주기 전반에 발생하는 마찰은, 본래 존재할 필요가 없는 '속도 vs. 안전'의 트레이드오프를 강요합니다. 보안은 상류(upstream)로 이동해 개발자가 실제로 일하는 방식의 일부가 되어야 합니다. 즉, 개발자의 일상 도구에 내장되고, 보안 팀이 사용하는 도구와 연결되어야 합니다.

[Microsoft Build 2026](https://build.microsoft.com/en-US/home)에서 우리는 새로운 보안 도구와 기능을 발표합니다. 이를 통해 개발자에게 실시간으로 명확한 가이드를 제공하고, 작업의 복잡도에 맞춰 확장하며, 보안 팀에는 전체 수명 주기에 걸친 일관된 가시성을 제공합니다. 그 결과 비즈니스가 통제력을 잃지 않으면서도 혁신은 빠르고 안전하게 나아갈 수 있습니다. 코드 보호, 에이전트 보호, 모델 보호를 돕는 솔루션을 아래에서 살펴보세요.

## 코드를 보호하세요 (Secure your code)

최근 헤드라인은 AI 모델의 강력함과, 이를 취약점 탐색·악용에 사용할 때 발생할 수 있는 위협 사이의 긴장을 드러냅니다. 이는 보안 팀이 이러한 모델의 힘을 안전하게 활용할 수 있는 솔루션을 찾도록 만드는 전환점이 되고 있습니다. 동시에 개발자는 같은 모델을 활용해 실제로 악용 가능한 위험을 효율적으로 식별하고, 작업 흐름 안에서 이를 해결하고자 합니다. 그래서 우리는 Microsoft Security 멀티모델 에이전트 스캐닝 하니스(코드네임 MDASH)를 개발하고, [Microsoft Defender](https://www.microsoft.com/en-us/security/business/microsoft-defender)와 GitHub Code Security(구 GitHub Advanced Security 제품군의 일부) 간의 네이티브 통합을 추가했습니다. 이로써 보안 팀과 개발 팀 모두가 더 이른 시점에 빈틈을 식별하고 메울 수 있습니다.

### 코드네임 MDASH로 악용 가능한 취약점 탐지·검증하기

새로운 Microsoft Security 멀티모델 에이전트 스캐닝 하니스(코드네임 MDASH)는 자격을 갖춘 조직을 대상으로 확장 프리뷰로 제공되며, 이제 [Microsoft Defender](https://www.microsoft.com/en-us/security/business/microsoft-defender)와의 통합을 포함합니다. 이 새로운 에이전트 보안 시스템은 여러 모델의 앙상블을 활용해 100개가 넘는 특화 AI 에이전트의 파이프라인을 오케스트레이션하여, 널리 쓰이는 프로그래밍 언어로 작성된 코드베이스 전반에서 악용 가능성을 탐지·검증·입증합니다.

이 접근 방식은 업계에서 독보적입니다. 우리의 멀티모델 에이전트 스캐닝 하니스는 구성 가능한 모델 패널을 사용합니다. 무거운 추론을 담당하는 최첨단(SOTA) 모델부터, 대량 작업을 위한 비용 효율적인 모델까지 아우릅니다. 덕분에 속도·재현율(recall)·비용을 상황에 맞게 조율하고, 특정 모델에 대한 의존성을 최소화할 수 있습니다.

여러 모델, 수백 개의 에이전트, 그리고 하루 100조 개가 넘는 신호의 조합은 이론적 잡음이 아닌 실제 위험을 식별하도록 도와, 팀이 '악용 가능한 것'에 집중하게 합니다. 전략적 함의는 분명합니다. AI 취약점 탐지는 연구실의 호기심을 넘어 엔터프라이즈 규모의 프로덕션급 방어로 넘어왔으며, 지속 가능한 우위는 단일 모델이 아니라 모델을 둘러싼 에이전트 시스템에 있습니다. [MDASH](https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-tops-leading-industry-benchmark/#how-capable-is-codename-mdash)는 최근 3주도 안 되는 기간에 약 10% 상승하여 CyberGym 업계 벤치마크에서 96.55%의 새로운 점수를 기록했습니다.

> "Accenture에서 우리는 늘 고객과 기업을 보호하기 위한 다음 단계를 모색합니다. Microsoft가 MDASH로 구축하고 있는 것은 반응적·규칙 기반 스캐닝에서, 숙련된 보안 연구자처럼 복잡한 코드베이스를 추론할 수 있는 에이전트 시스템으로의 의미 있는 전환을 보여줍니다." — Kris Burkhardt, Accenture 최고정보보안책임자(CISO). Accenture는 MDASH를 함께 발전시키고 에이전트 기반 AI 취약점 탐지를 가속하기 위해 프리뷰에 참여 중인 [보안 파트너 및 Microsoft Intelligent Security Association(MISA) 회원](https://aka.ms/MDASHengagedpartners)사 중 하나입니다.

파트너 협업은 반응적 탐지에서 악용 가능한 위험의 선제적 식별로 나아가려는 공동의 지향을 보여줍니다. "사이버 위협이 빠르게 진화하고 있으며, AI는 공격의 규모와 정교함을 모두 가속하고 있습니다. Microsoft의 MDASH 투자는 조직이 이 곡선보다 앞서 나가도록 돕겠다는 강한 의지를 보여줍니다. 초기 논의와 혁신 경험을 토대로, 우리는 MDASH가 SecOps를 단순화·강화하여 조직이 더 큰 회복탄력성과 자신감으로 운영하도록 도울 수 있는 강력한 잠재력을 봅니다." — Morgan Adamski, PwC US 사이버·데이터·기술 리스크 부문 프린시플 겸 부플랫폼 리더.

우리는 선도적인 모델과 우리의 플랫폼·전문성을 결합해 대규모로 보호를 제공하기 위해 업계 전반과 협력하고 있습니다. "MDASH가 고객이 직면한 가장 시급한 과제 중 하나, 즉 취약점 발견과 실질적 조치 사이의 시간을 단축하는 문제를 다루기 때문에 Microsoft와의 협업이 기대됩니다. 신뢰할 수 있는 보안 벤더로서 Microsoft의 역할이 중요합니다. 고객은 혁신을 원하지만, 동시에 확신·거버넌스, 그리고 의지할 수 있는 파트너를 필요로 합니다. MDASH에 대한 초기 경험은 고무적이었고, 조직이 취약점 탐지·해결 방식을 현대화하는 데 실질적으로 기여할 기회를 봅니다." — Jason Rader, Insight CISO.

코드네임 MDASH 확장 프리뷰에 대한 자세한 내용은 [Microsoft 계정 담당자](https://info.microsoft.com/ww-landing-security-generic-contact-me.html?culture=en-us&country=us)에게 문의하세요.

### Microsoft Defender와 GitHub Code Security로 코드 취약점 우선순위 지정·해결하기

코드네임 MDASH가 진정으로 악용 가능한 것을 식별·검증하는 한편, 이제 정식 출시(GA)된 [Microsoft Defender와 GitHub Code Security 간 통합](https://learn.microsoft.com/en-us/azure/defender-for-cloud/github-advanced-security-overview)(구 GitHub Advanced Security 제품군의 일부)은 런타임 컨텍스트를 개발·보안 워크플로로 가져옵니다. 덕분에 팀은 인적 리소스에 미치는 영향을 최소화하면서 위험을 조기에 우선순위화·해결할 수 있습니다. 코드에서 발견된 취약점은 인터넷 노출 여부, 데이터 민감도 같은 실제 프로덕션 신호로 자동 보강되어 우선순위 판단에 활용됩니다. 이후 개발자는 GitHub Copilot Autofix와 GitHub Copilot 클라우드 에이전트를 통해 생성·할당·검증되는 AI 보조 수정으로 문제를 해결할 수 있습니다.

실제 및 잠재적 취약점을 모두 나타내는 발견 사항을 책임 있고 조율된 방식으로 공개하기 위해, 역할 기반 액세스 제어(RBAC)는 권한이 있는 사람만 해당 내용을 보고 조치할 수 있도록 보장합니다. 프로덕션 신호 보강, AI 보조 해결, 그리고 단일 워크플로 내에서의 안전한 발견 사항 처리가 결합되어, 보안 팀과 개발 팀이 실제 위험에 집중하고 신속히 대응할 수 있습니다.

[에이전트 기반 개발자 SecOps에 대해 자세히 알아보기](https://aka.ms/AgenticDevSecOps)

## 에이전트를 보호하세요 (Secure your agents)

에이전트는 빠르게 애플리케이션 스택의 새로운 계층이 되고 있습니다. 개발자가 에이전트를 만들어 프로덕션으로 옮길 때는, 내장된 ID·거버넌스·안전성 테스트를 포함해 보안을 희생하지 않고도 빠르게 출시할 수 있는 도구가 필요합니다. 보안 팀의 요구도 이와 겹칩니다. 무엇이 실행 중인지에 대한 가시성, 에이전트가 접근할 수 있는 대상에 대한 통제, 그리고 클라우드와 엔드포인트 전반의 일관된 거버넌스가 필요합니다. Microsoft는 이를 돕기 위한 새로운 솔루션을 제공합니다.

### 첫날부터 안전한 에이전트 구축하기

[Build 2026](https://build.microsoft.com/en-US/home)에서 Microsoft는 개발자가 기본적으로 안전하고 엔터프라이즈에 즉시 사용할 수 있는 에이전트를 구축하도록 돕는 새로운 기능을 선보입니다. [Agent 365 SDK](https://learn.microsoft.com/en-us/microsoft-365/agents-sdk/agents-sdk-overview)의 정식 출시(GA)로, 개발자는 제어 기능을 개발 워크플로에 직접 통합하여 관찰 가능성(observability), 액세스 제어, 컴플라이언스 적용을 에이전트의 설계·배포 방식에 녹여낼 수 있습니다. 이를 통해 팀은 어떤 AI 플랫폼에서든 컴플라이언스를 준수하고 엔터프라이즈에 적합하며 Agent 365와 잘 어우러지는 맞춤형 에이전트를 구축할 수 있습니다.

보안은 개발을 넘어 에이전트의 실행 방식까지 확장됩니다. Windows에서는 [Microsoft Execution Container(MXC)](https://github.com/microsoft/mxc) SDK가 에이전트 실행에 대한 OS 수준의 제어를 제공하여, 개발자와 IT 팀이 격리 기술(프로세스·세션 격리 등)을 통해 OS가 적용하는 봉쇄(containment)와 정책을 정의할 수 있게 합니다. 이제 정식 출시된 [Windows 365 for Agents](https://learn.microsoft.com/en-us/windows-365/agents/introduction-windows-365-for-agents)를 사용하면, 완전히 격리되고 정책으로 통제되는 Cloud PC에서 어떤 에이전트든 실행할 수 있습니다. Agent 365와의 네이티브 Windows 통합은 관찰 가능성·보안·거버넌스를 위한 공통 기반을 제공하며, 에이전트 런타임 실행을 통제하고 에이전트 작동 방식을 제어하는 정책을 설정하는 내장 Intune 기능도 포함합니다.

이 [새로운 기능들](https://blogs.windows.com/windowsdeveloper/?p=57808)은 현재 얼리 프리뷰로 제공됩니다.

### Agent 365로 대규모 에이전트 관찰·거버넌스·보호하기 — 이제 로컬 에이전트 포함

에이전트가 여러 환경에 확산되면서, 이들에 대한 가시성과 통제 확보가 매우 중요해집니다. [Agent 365](https://www.microsoft.com/en-us/microsoft-agent-365)는 에이전트 난립과 위험을 관리하기 위한 새로운 기능을 도입합니다. 여기에는 [Microsoft Defender](https://www.microsoft.com/en-us/security/business/microsoft-defender), [Microsoft Entra](https://www.microsoft.com/en-us/security/business/microsoft-entra), [Microsoft Intune](https://www.microsoft.com/en-ie/security/business/microsoft-intune)이 함께 작동해 발견한 비관리 로컬 에이전트를 표면화하는 Agent 365 에이전트 레지스트리가 포함됩니다. 이 레지스트리는 코딩 에이전트, AI 데스크톱 애플리케이션, 로컬 및 원격 MCP(Model Context Protocol) 서버를 포함해 20가지가 넘는 로컬 에이전트 유형을 지원합니다. 여기서부터 Intune 정책을 사용해 OpenClaw 에이전트의 일반적인 실행 방식을 차단할 수 있습니다.

보안 팀은 또한 개발자 생산성을 저해하지 않으면서 신종 위협에 대응할 수 있어야 합니다. Microsoft Defender, Entra, Intune은 함께 작동해 개발자 생산성을 떨어뜨리지 않고도 에이전트 위험을 관리하는 데 필요한 가시성·런타임 보호·컨텍스트를 제공합니다. Defender는 분석가가 고급 헌팅(advanced hunting)을 사용해 에이전트 활동을 조사하도록 지원하고, 에이전트가 네트워크 전반에서 어떻게 연결되어 있는지 이해하도록 돕는 노출 그래프(exposure graph)를 제공합니다. 이 기능들의 프리뷰가 곧 제공될 예정입니다.

데이터 보호는 대규모 에이전트 보안의 토대입니다. [Microsoft Purview](https://www.microsoft.com/en-ie/security/business/microsoft-purview)는 데이터 유출 방지 제어, DSPM(데이터 보안 태세 관리) 위험 탐지, 그리고 코딩 에이전트(Claude Code, GitHub Copilot, OpenAI Codex, OpenClaw)에 대한 에이전트 위험 탐지를 제공합니다. 이를 통해 로컬 에이전트가 민감한 데이터에 접근하는 방식에 대한 가시성, 위험한 프롬프트에 대한 런타임 보호, 안전하지 않은 에이전트 행동에 대한 인사이트를 확보할 수 있습니다. [Microsoft Purview Audit](https://www.microsoft.com/en-ie/security/business/risk-management/microsoft-purview-audit)는 모든 에이전트 활동을 기록하여 완전한 추적성을 제공합니다. 이 기능들의 프리뷰도 곧 제공될 예정입니다.

[이 기능들은 현재 프리뷰로 제공됩니다](https://techcommunity.microsoft.com/blog/microsoft-security-blog/securing-the-new-risk-surface-local-agents-claws-and-open-runtimes/4524602)

## 데이터를 에이전트에 안심하고 맡기세요 (Trust agents with your data)

개발자는 자신이 구축하는 에이전트와 관련된 데이터 보안 태세 및 위험 신호에 대해 직접적이고 실시간적인 통찰도 필요로 합니다. 이제 정식 출시된 Foundry Control Plane에 내장된 Purview 데이터 위험 신호는, 민감한 데이터가 노출되기 전에 어디에 보호를 적용해야 하는지에 대한 가이드를 개발자에게 제공합니다. 예를 들어 Purview는 테스트 중 에이전트가 민감한 금융 데이터를 표면화할 때 이를 실시간으로 플래그하고, 배포 전에 접근을 마스킹하거나 제한하도록 개발자를 안내합니다.

위험을 한층 더 줄이기 위해, Purview는 Foundry의 에이전트 프롬프트에 대한 런타임 데이터 유출 방지(DLP)를 도입하며, 이는 Agent 365와 함께 프리뷰로 제공됩니다. 이 기능은 민감한 데이터가 에이전트에 의해 처리되기 전에 이를 탐지·차단·감사하여, 민감 정보가 결코 AI 모델에 도달하지 않도록 보장합니다.

[개발자를 위한 Microsoft Purview에 대해 자세히 알아보기](https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-purview-enables-developers-with-strong-data-security-across-ai-apps-an/4524626)

## 모델을 보호하세요 (Secure your models)

AI가 프로덕션에 도달하기 전에, 팀은 자신이 의존하는 모델이 안전한지 검증해야 합니다. 이제 개발자는 프리뷰로 제공되는 [Defender AI 모델 스캐닝](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-model-security?pivots=defender-portal)을 통해 플랫폼 네이티브든 BYO(bring-your-own)든 모델 아티팩트를 검사할 수 있습니다. 빈틈을 조기에 메우기 위해, Defender AI 모델 스캐닝은 레지스트리·작업 영역·CI/CD 파이프라인 전반에서 잠재적으로 취약하거나 손상된 모델을 탐지·차단하여 배포 전에 모델 무결성을 검증합니다.

## 신뢰는 보안에서 시작됩니다 (Trust starts with security)

혁신과 안전 사이에서 선택을 강요받아서는 안 됩니다.

오늘 발표된 기능들은 전체 개발 수명 주기를 아우릅니다. 무엇이 악용 가능한지 발견하고, 무엇이 실행 중인지 거버넌스하며, AI가 의존하는 데이터를 보호하고, 에이전트가 프로덕션에 도달하기 전에 의도대로 동작하는지 검증합니다. Microsoft 보안은 개발자가 이미 사용하는 플랫폼과 워크플로에 직접 내장되어, [Microsoft Foundry](https://azure.microsoft.com/en-us/products/ai-foundry), [Copilot Studio](https://www.microsoft.com/en-us/microsoft-365-copilot/microsoft-copilot-studio), GitHub, 오픈소스 프레임워크 전반의 혁신을 지원하고, 섀도 AI에 대한 발견과 거버넌스를 제공합니다.

그러나 AI의 진정한 진보는 획기적인 기능 그 이상에 달려 있습니다. 바로 조직이 자신이 구축·배포하는 시스템을 신뢰할 수 있는가에 달려 있습니다. 이것이 [Build 2026](https://build.microsoft.com/en-US/home)에서 발표된 혁신들을 관통하는 공통의 맥이자, 우리의 접근을 이끄는 원칙입니다. AI의 미래는 가장 빠르게 움직이는 이들만이 아니라, 신뢰를 바탕으로 혁신할 수 있는 이들의 것이기 때문입니다.

Microsoft Security 솔루션에 대해 더 알아보려면 [공식 웹사이트](https://www.microsoft.com/en-us/security/business)를 방문하세요. 보안 관련 전문가 콘텐츠를 계속 받아보려면 [Security 블로그](https://www.microsoft.com/security/blog/)를 즐겨찾기에 추가하세요.
