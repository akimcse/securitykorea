---
title: "[KO] ​​​​What’s new in Microsoft Security: November 2026"
date: 2026-11-05 17:00:00 +0000
categories: ["Agent 365"]
tags: ["in the loop", "microsoft agent 365"]
solution: agent-365
owners: ["akimcse"]
source_url: "https://www.microsoft.com/en-us/security/blog/2026/11/05/whats-new-in-microsoft-security-november-2026/"
source_author: "Alym Rayani"
auto_generated: true
pin: false
---
> 본 글은 Microsoft Security Blog의 [​​​​What’s new in Microsoft Security: November 2026](https://www.microsoft.com/en-us/security/blog/2026/11/05/whats-new-in-microsoft-security-november-2026/) 글을 한국어로 번역·정리한 것입니다. 원문 작성자: Alym Rayani.
{: .prompt-info }

> ⚠️ 번역 엔진(Azure OpenAI) 미설정 — 원문 그대로 표시(테스트 스텁).

Endpoint administrators need to keep elevated access accountable at scale. Security teams also need a clearer view of expert-led protection and a simpler way to deploy SQL Server protection in Azure Government. As AI agents gain access to business data and tools, organizations need ways to limit their authority and adapt protection as risk changes. This month’s [Microsoft Intune](https://www.microsoft.com/en-us/security/business/microsoft-intune?msockid=0809c913f8cc65b61b61deeaf9876412) and [Microsoft Defender](https://www.microsoft.com/en-us/security/business/microsoft-defender) updates introduce capabilities across these areas, alongside new Secure AI capabilities for agent access. A recent Secure Now update in [Microsoft Security Exposure Management](https://www.microsoft.com/en-us/security/business/siem-and-xdr/microsoft-security-exposure-management?msockid=0809c913f8cc65b61b61deeaf9876412) also connects information on recent threats to focused initiatives for reducing exposure. 

Here’s what’s new:  

## Limit agent authority to the task with Dynamic Permissions 

### Give agents task-scoped authority and adapt access as risk changes 

As agents gain access to business data and tools, organizations need ways to manage what each agent is allowed to do. Dynamic Permissions provides an agent its own permissions and authority, scoped to its current task and for only as long as the task requires. As the agent works, Dynamic Agent Risk assesses whether the agent’s authority aligns with changing behavior and context. Dynamic Conditional Access can then respond proportionately by narrowing permissions, restricting access to resources, or requiring human approval for higher-impact actions. Together, these capabilities are designed to help organizations tailor agent authority before an agent acts and adjust access as risk changes. [See how security can respond](https://www.microsoft.com/en-us/security/blog/2026/10/19/agents-are-your-newest-insiders-security-must-move-at-their-speed/) when an agent steps outside its task. 

## Contain local AI agents with Microsoft Execution Containers

### Apply least-privilege boundaries to help limit access on Windows

Microsoft Execution Containers (MXC), now generally available, gives organizations an operating system-enforced containment layer for AI agents, designed to limit what an agent can access. Rather than relying on the agent to behave within intended boundaries, MXC applies least-privilege controls across files, networks, processes, and user interactions, with additional isolation options for higher-risk scenarios. Organizations can tune and validate policies before enforcing them broadly, while upcoming integration with Microsoft Intune, [Microsoft Entra](https://www.microsoft.com/en-us/security/business/microsoft-entra), and [Microsoft Agent 365](https://www.microsoft.com/en-us/microsoft-agent-365) is intended to extend governance and attribution across the enterprise. Discover more about this [policy-driven containment for AI agents](https://blogs.windows.com/windowsdeveloper/2026/10/07/microsoft-execution-containers-policy-driven-containment-for-ai-agents/).

## Scale least privilege with Microsoft Intune Endpoint Privilege Management

### Expand least-privilege scenarios with new system settings support and simpler tenant onboarding

[Microsoft Intune Endpoint Privilege Management](https://www.microsoft.com/en-us/security/business/endpoint-management/microsoft-intune-endpoint-privilege-management?msockid=0809c913f8cc65b61b61deeaf9876412) continues to expand the tasks standard users can complete without broad administrator rights. With new system settings support, standard users can change IPv4, IPv6, and DNS server values on their device’s network adapters through Endpoint Privilege Management, while administrators determine how those changes are elevated. For user-confirmed changes, administrators can require a business justification, Windows authentication, or both before the change is applied. Along with tenant onboarding updates, these improvements support organizations as they get started with and expand their use of Endpoint Privilege Management. Explore how to get started with [system settings](https://learn.microsoft.com/en-us/intune/epm/manage-system-settings) support in Endpoint Privilege Management.

[Get started with Microsoft Intune Endpoint Privilege Management](https://www.microsoft.com/en-us/security/business/endpoint-management/microsoft-intune-endpoint-privilege-management?msockid=0809c913f8cc65b61b61deeaf9876412)

## Simplify security operations with Defender Experts

### See what Defender Experts are investigating in a consolidated experience

As threats move faster and security environments grow more complex, security teams need to quickly understand what matters and when to act. New [Microsoft Defender Experts MDR](https://www.microsoft.com/en-us/security/business/services/microsoft-defender-experts-mdr?msockid=0809c913f8cc65b61b61deeaf9876412#Overview) experiences in the Microsoft Defender portal bring ongoing expert work into focus with a consolidated overview page with updated navigation and visibility into hunts. Teams can review active and completed hunts, see findings from Defender Experts, and identify items that may require follow-up. [Learn more about the new Defender Experts MDR experiences.](https://techcommunity.microsoft.com/blog/microsoft-defender-experts/bringing-defender-experts-protection-and-proactive-hunting-into-focus/4538006)

[Get around-the-clock defense with Microsoft Defender Experts MDR](https://www.microsoft.com/en-us/security/business/services/microsoft-defender-experts-mdr?msockid=0809c913f8cc65b61b61deeaf9876412#Overview)

## Extend protection and discover local agents with Microsoft Defender

### Simplify deployment and expand SQL protection

The enhanced agent for Defender for SQL Servers on machines is now generally available for resource- and subscription-level enablement in Azure Government cloud. The enhanced agent uses existing SQL infrastructure, eliminating the need to deploy the Azure Monitor Agent for this scenario. Security teams can spend less time on deployment and extend protection across their SQL Server environments. [Learn more about the enhanced agent ](https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes#enhanced-agent-for-defender-for-sql-servers-on-machines-is-fully-available-in-azure-government-cloud)and how to get started.

### Discover local AI agents and their configured MCPs on Windows and macOS

On endpoints, Microsoft Defender is extending discovery capabilities for supported local AI agents and their configured model context protocols (MCPs) across Windows and macOS. Now generally available, Defender discovers more than 50 supported local AI agents by observing their activity and brings the agent, device, account, and configured MCP context together to help security teams understand local AI agent activity in their environment. [Learn more about local agents](https://aka.ms/LocalAgentDiscovery).

[Explore Microsoft Defender solutions](https://www.microsoft.com/en-us/security/business/microsoft-defender)

## Improve security posture with Microsoft Security Exposure Management 

### Prioritize foundational security controls with Secure Now 

AI-enabled attacks can take advantage of familiar weaknesses, including excessive permissions, unprotected authentication flows, and exposed systems. [Secure Now](https://www.microsoft.com/en-us/security/blog/2026/09/17/from-guidance-to-action-security-fundamentals-that-materially-reduce-risk/) now pairs information about recent threats with focused initiatives across security domains. Security teams can use that context to identify foundational controls that need attention, review the recommended actions, and prioritize work intended to reduce exposure. The update helps connect information about observed attack patterns with security improvements teams can consider in their own environments. 

[Learn more about Microsoft Security Exposure Management](https://www.microsoft.com/en-us/security/business/siem-and-xdr/microsoft-security-exposure-management)

## Learn how to address agentic AI’s security challenges 

### From agentic inventory and observability to stopping AI runtime threats 

An inventory is only the starting point for managing Al agent risk. Organizations also need to consider ownership, limits on what agents can access, how risk is reassessed as agents operate, and protections against emerging threats. “Don’t Leave AI Exposed” provides security professionals, IT administrators, and developers with actionable guidance on managing risk across the agent lifecycle. [Download the guide](https://info.microsoft.com/ww-landing-dont-leave-ai-exposed.html?lcid=en-us) for considerations spanning agent inventory, ownership, access, monitoring, and runtime protection.

## Stay in the Loop 

Security teams need a clear account of what is changing across the portfolio and where those changes can strengthen their operations. In the Loop brings together the latest Microsoft Security updates and their implications for your security strategy. [Explore earlier editions](https://www.microsoft.com/en-us/security/blog/tag/in-the-loop/) and check back for the next drop. 

See Microsoft Security innovations in action at [Microsoft Ignite](https://ignite.microsoft.com/), November 17-20, 2026, in San Francisco or online.

To learn more about Microsoft Security solutions, visit our [website.](https://www.microsoft.com/en-us/security/business) Bookmark the [Security blog](https://www.microsoft.com/security/blog/) to keep up with our expert coverage on security matters. Also, follow us on LinkedIn ([Microsoft Security](https://www.linkedin.com/showcase/microsoft-security/)) and X ([@MSFTSecurity](https://twitter.com/@MSFTSecurity)) for the latest news and updates on cybersecurity.

The post [​​​​What’s new in Microsoft Security: November 2026](https://www.microsoft.com/en-us/security/blog/2026/11/05/whats-new-in-microsoft-security-november-2026/) appeared first on [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog).
