---
title: "[KO] ​​​​What’s new in Microsoft Security: July 2026"
date: 2026-07-30 16:00:00 +0000
categories: ["Agent 365"]
tags: ["in the loop", "microsoft agent 365"]
solution: agent-365
owners: ["akimcse"]
source_url: "https://www.microsoft.com/en-us/security/blog/2026/07/30/whats-new-in-microsoft-security-july-2026/"
source_author: "Alym Rayani"
auto_generated: true
pin: false
---
> 본 글은 Microsoft Security Blog의 [​​​​What’s new in Microsoft Security: July 2026](https://www.microsoft.com/en-us/security/blog/2026/07/30/whats-new-in-microsoft-security-july-2026/) 글을 한국어로 번역·정리한 것입니다. 원문 작성자: Alym Rayani.
{: .prompt-info }

> ⚠️ 번역 엔진(Azure OpenAI) 미설정 — 원문 그대로 표시(테스트 스텁).

Every organization needs security that protects end to end with the speed and scale of AI. Microsoft’s vision is simple: security should be ambient and autonomous, just like the AI it protects.

As organizations scale AI and expand across environments, security teams need protection that covers every surface. This month’s updates help security and IT teams secure their AI environments, use AI to defend at speed and scale, and strengthen the foundations that AI-powered operations depend on. Here’s what’s new:

## Project Perception brings agentic defense to security operations

[Project Perception](https://blogs.microsoft.com/blog/2026/07/27/rethinking-security-for-the-age-of-ai/), newly announced, is a coordinated system of specialized agents, cybersecurity-focused models, and enterprise-wide signals that transform how security operates. The agents work as a team: red team agents expose weaknesses, blue team agents investigate cyberthreats, and green agents harden what’s found. These multi-agent autonomous workflows work as a team to operate in continuous loops to execute end-to-end security workflows.

[Learn more about Project Perception](https://blogs.microsoft.com/blog/2026/07/27/rethinking-security-for-the-age-of-ai/)

## Microsoft Defender secures the full AI attack surface, from inbox to cloud

Expanded [Microsoft Defender](https://www.microsoft.com/en-us/security/business/microsoft-defender) protections are designed to reduce risks associated with day-to-day AI interactions, from email inboxes to cloud agent environments. New [prompt injection protection](https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/defending-the-inbox-against-prompt-injection-attacks/4534636) in Microsoft Defender, now in preview, identifies and isolates emails containing malicious AI instructions before delivery, reducing the risk of prompt injection attacks reaching the inbox. Unified Defender posture and runtime protection for cloud agents in [Microsoft Agent 365](https://www.microsoft.com/en-us/microsoft-agent-365) consolidates security posture assessment and runtime protection for Microsoft Foundry, Microsoft Copilot Studio, and third party-managed agents, helping teams reduce AI-specific risk across the agent estate.

### Accelerate detection, prioritization, and response with AI embedded in SecOps workflows

Security teams can accelerate detection, prioritization, and response to cyberthreats with AI embedded directly into security operations (SecOps) workflows through Microsoft Defender. Threat intelligence enhancements, including [Microsoft Defender Threat Intelligence](https://www.microsoft.com/en-us/security/business/siem-and-xdr/microsoft-defender-threat-intelligence) convergence and an enhanced Threat Intelligence Agent, bring more out-of-the-box intelligence and automation into the unified SecOps workflow, so teams can move from summary to action.

### Strengthen the cloud, code, and identity foundations AI depends on

Microsoft Defender is strengthening the foundational protections that AI-era operations depend on across cloud, code, and identity. Cloud Security Posture Management [extends coverage to serverless containers](https://aka.ms/mdc-serverless-posture), giving teams visibility and continuous posture assessment across containerized workloads running on Azure Container Apps, Azure Container Instances, and Amazon Web Services Elastic Container Service (AWS ECS) on Fargate. New interconnected experiences between Defender and Microsoft Entra empower the security operations center (SOC) to disable compromised identities directly using a role-based access control (RBAC) mode that maintains least privilege. [Microsoft Defender Experts services are also expanding](https://aka.ms/blackhat-services): Microsoft Defender Experts Threat Intelligence delivers human-led, curated insight into the cyberthreats most relevant to each organization, and Microsoft Defender Experts MDR extends expert-run detection and response beyond the Microsoft estate into third-party and multicloud signals through [Microsoft Sentinel](https://www.microsoft.com/en-us/security/business/siem-and-xdr/microsoft-sentinel-siem).

## Microsoft Entra strengthens identity across the AI-powered enterprise

### Strengthen identity foundations for AI-powered operations

New capabilities in [Microsoft Entra](https://www.microsoft.com/en-us/security/business/microsoft-entra) are designed to strengthen the identity foundations that AI-powered operations depend on. Tenant governance helps organizations discover, manage, and govern tenants across their environment with centralized policies and cross-tenant delegated administration. Microsoft Entra ID is [making passkeys the default authentication experience](https://www.microsoft.com/en-us/security/blog/2026/07/13/microsoft-entra-id-security-updates-passkeys-are-the-default-authentication-method-in-entra-id/), which helps reduce reliance on SMS and voice, strengthens phishing-resistant security, and makes for an easier transition away from Microsoft-provided telecom delivery, which will retire in 2027. Through new interconnected Entra and Defender experiences, identity and access management and SOC teams share user experience, RBAC, and agentic workflows that eliminate product seams so identity and security operations can work together.

### Protect sensitive data in motion across software as a service (SaaS) and AI apps with Microsoft Purview and Microsoft Entra

Microsoft Purview [now integrates](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/protect-sensitive-data-in-motion-across-saas-and-ai-apps-with-microsoft-purview-/4529310) with Microsoft Entra Internet Access to extend data security to the network layer, enabling real-time protection of sensitive data shared with unmanaged cloud and AI apps over the network. For example, when an employee attempts to upload sensitive customer data or proprietary information, including text and files, into shadow AI apps, sharing is detected and blocked before the data is leaked from the organization. Organizations now have a unified Microsoft solution to gain visibility into where organizational data is shared externally, to detect and block sensitive data in transit, and to enable consistent data protection across their environment without relying on third-party solutions.

## Microsoft Purview strengthens data security, compliance, and investigation for AI

A new Microsoft Purview Data Loss Prevention (DLP) for Microsoft 365 Copilot protection, available in preview, now gives data security teams [greater control over how Copilot leverages email content](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about#block-external-email-from-being-processed-preview), given external sources can introduce sensitive, third-party, or unvetted information that organizations may not want to rely on. Now admins can exclude emails from external senders from being referenced, summarized, or used as grounding data for Copilot. For example, with this DLP policy in place, an employee working with an external collaborator can still rely on Copilot to leverage internal insights, while external conversations are automatically excluded from Copilot-generated responses. With the native integration between [Microsoft Purview](https://www.microsoft.com/en-us/security/business/microsoft-purview) and Microsoft 365 Copilot, organizations can extend controls to AI interactions with minimal additional configuration, resulting in a more predictable and policy-aligned AI environment.

A new centralized Microsoft Purview Insider Risk Management alert experience simplifies the prioritization of the most pressing data risks by bringing [agentic alert triage, enriched user details, and expanded analysis capabilities](https://techcommunity.microsoft.com/blog/microsoft-security-blog/introducing-a-unified-alert-experience-for-microsoft-purview-insider-risk-manage/4530714) (such as notes infused on the Insider Risk Management case) into a single view. Helping power this experience, the [Data Security Triage Agent](https://aka.ms/InsiderRiskInvestigations) includes an advanced AI reasoning layer, now generally available, that performs deeper, multi-step analysis across user, device, and data activity signals to surface the incidents most likely to require investigation while reducing noise. Analysts can filter across classic and Data Security Triage Agent attributes on a single page, preview agent summaries and user details without switching views, and document findings while the system automatically records status changes and escalations to maintain a clear investigation history. Together, the Insider Risk Management alert experience and Data Security Triage Agent help security teams investigate faster and with greater confidence.

## Advanced endpoint management now broadly available

As of July 1, 2026, the capabilities of the [Microsoft Intune Suite](https://www.microsoft.com/en-us/security/business/microsoft-intune) are included in Microsoft 365 E5, with select capabilities also available in Microsoft 365 E3, bringing advanced endpoint management to more organizations without added cost. IT and security teams can now apply advanced endpoint management capabilities to reduce standing admin rights, modernize certificate management, resolve issues quickly, streamline app delivery, and bring AI into workflows with Microsoft Security Copilot in Intune. Together, these capabilities strengthen the endpoint foundations that AI-powered operations depend on. [See everything that’s now included in your plan](https://techcommunity.microsoft.com/blog/microsoftintuneblog/advanced-microsoft-intune-capabilities-now-available-in-microsoft-365-e3-and-e5/4529335) and how to start putting it to work.

## Stay In the Loop

[Microsoft Security](https://www.microsoft.com/en-us/security) is focused on delivering innovations across our portfolio, along with research-driven insights and reports for the security community. [In the Loop posts](https://www.microsoft.com/en-us/security/blog/tag/in-the-loop/) are your reliable source of what’s new across Microsoft Security and what it means for your security strategy. Check back for the next drop.

To learn more about Microsoft Security solutions, visit our [website.](https://www.microsoft.com/en-us/security/business) Bookmark the [Security blog](https://www.microsoft.com/security/blog/) to keep up with our expert coverage on security matters. Also, follow us on LinkedIn ([Microsoft Security](https://www.linkedin.com/showcase/microsoft-security/)) and X ([@MSFTSecurity](https://twitter.com/@MSFTSecurity)) for the latest news and updates on cybersecurity.

The post [​​​​What’s new in Microsoft Security: July 2026](https://www.microsoft.com/en-us/security/blog/2026/07/30/whats-new-in-microsoft-security-july-2026/) appeared first on [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog).
