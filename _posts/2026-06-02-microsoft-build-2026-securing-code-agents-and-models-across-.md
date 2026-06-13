---
title: "[KO] Microsoft Build 2026: Securing code, agents, and models across the development lifecycle"
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

> ⚠️ 번역 엔진(Azure OpenAI) 미설정 — 원문 그대로 표시(테스트 스텁).

In this article
		

		
			
		
	
	
		
			- [Secure your code](#secure-your-code)
- [Secure your agents](#secure-your-agents)
- [Trust agents with your data](#trust-agents-with-your-data)
- [Secure your models](#secure-your-models)
- [Trust starts with security](#trust-starts-with-security)
		
	
	

Today, developers and security teams are caught in growing tension. AI is accelerating development and introducing new issues around insecure code, opaque models, data exposure, and compliance. Add the challenges of shadow AI and tool sprawl and the result is a widening gap between innovation and control. As developers move faster, security teams struggle to keep up with visibility, governance, and oversight. The resulting friction across the development lifecycle is forcing a tradeoff between speed and safety that doesn’t need to exist. Security needs to move upstream to become part of how developers actually work: built into their day-to-day tools and connected to the tools security teams use.

[At Microsoft Build 2026](https://build.microsoft.com/en-US/home), we are announcing new security tools and capabilities to give developers clear guidance in real time, scale with the complexity of tasks, and provide security teams with a consistent view across the full lifecycle so innovation can move fast and securely without the business losing control. Learn more about our solutions to help secure your code, secure your agents, and secure your models.

## Secure your code

Today’s headlines reflect the tension around the power of AI models and the potential threat they pose when used to find and exploit vulnerabilities. It is forcing a shift as security teams look for solutions to help them safely harness the power of these models. At the same time, developers want to use these same models to efficiently identify real, exploitable risk and remediate it within their flow of work. That’s why we developed the Microsoft Security multi-model agentic scanning harness (codename MDASH) and added native integration between [Microsoft Defender](https://www.microsoft.com/en-us/security/business/microsoft-defender) and GitHub Code Security (part of the former GitHub Advanced Security suite) to help both security and developer teams identify and close gaps early.

### Discover and validate exploitable vulnerabilities with codename MDASH

The new Microsoft Security multi-model agentic scanning harness (codename MDASH) is available in an expanded preview for eligible organizations and now includes integration with [Microsoft Defender](https://www.microsoft.com/en-us/security/business/microsoft-defender). This new agentic security system orchestrates a pipeline of more than 100 specialized AI agents using an ensemble of models to discover, validate, and prove exploitability across codebases written in popular programming languages.

This approach is unique in the industry. Our multi-model agentic scanning harness uses a configurable panel of models, ranging from state-of-the-art (SOTA) models as the heavy reasoners, to more cost-effective models for high-volume operations. This allows us to trade speed, recall, and cost, and minimize dependency on any specific model.

The combination of multiple models, hundreds of agents, and over 100 trillion signals a day helps identify real risk over theoretical noise, to help teams focus on what can be exploited. The strategic implication is clear: AI vulnerability discovery has crossed from research curiosity into production-grade defense at enterprise scale, and the durable advantage lies in the agentic system around the model rather than any single model itself. [MDASH](https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-tops-leading-industry-benchmark/#how-capable-is-codename-mdash) recently jumped roughly 10% in less than three weeks to a new CyberGym industry benchmark score of 96.55%.

“At Accenture, we’re always looking toward the next frontier in protecting our clients and our enterprise. What Microsoft is building with MDASH reflects a meaningful shift from reactive, rule-based scanning to agentic systems that can reason across complex codebases like a skilled security researcher,” says Kris Burkhardt, Chief Information Security Officer at Accenture. Accenture is one of a select group of [Security partners and Microsoft Intelligent Security Association (MISA) members](https://aka.ms/MDASHengagedpartners) that are engaged in the preview to shape MDASH and accelerate agentic AI vulnerability discovery.

Our partner engagements reflect a shared focus on moving from reactive detection to proactive identification of exploitable risk. “We’re seeing cyber threats evolve rapidly, with AI accelerating both the scale and sophistication of attacks. Microsoft’s investment in MDASH reflects a strong commitment to helping organizations stay ahead of this curve. Based on our early discussions and exposure to the innovation, we see strong potential for MDASH to simplify and strengthen SecOps, helping organizations operate with greater resilience and confidence,” says Morgan Adamski, Principal and Deputy Platform Leader of Cyber, Data, and Tech Risk at PwC US.

Together, we are partnering across the industry to use leading models paired with our platforms and expertise to deliver protection at scale. “We’re excited to work with Microsoft on MDASH because it addresses one of the most pressing challenges our customers face: reducing the time between discovering a vulnerability and taking meaningful action. Microsoft’s role as a trusted security vendor matters here—customers need innovation, but they also need confidence, governance, and a partner they can rely on. Our early experience with MDASH has been encouraging, and we see real opportunity for it to help organizations modernize how they approach vulnerability discovery and remediation,” says Jason Rader, Insight CISO.  

Reach out to your [Microsoft account representative](https://info.microsoft.com/ww-landing-security-generic-contact-me.html?culture=en-us&country=us) for more information on the expanded preview of codename MDASH.

### Prioritize and remediate code vulnerabilities with Microsoft Defender and GitHub Code Security

While codename MDASH identifies and validates what’s truly exploitable, the [integration between Microsoft Defender and GitHub Code Security](https://learn.microsoft.com/en-us/azure/defender-for-cloud/github-advanced-security-overview) (part of the former GitHub Advanced Security suite), now generally available, brings runtime context into development and security workflows so that teams can prioritize and address risks early minimizing the impact to human resources. Vulnerabilities discovered in code are automatically enriched with real production signals, such as internet exposure and data sensitivity to inform prioritization. Developers can then remediate issues using AI-assisted fixes that are generated, assigned, and validated through GitHub Copilot Autofix and the GitHub Copilot cloud agent.

To support responsible, coordinated disclosure of findings that represent both real and potential vulnerabilities, role-based access controls ensure that only authorized individuals can view and act on them. Together, the production signal enrichment, AI-assisted remediation, and secure handling of findings within a single workflow help security and developer teams focus on real risk and enable teams to act quickly.

[Learn more about agentic developer SecOps](https://aka.ms/AgenticDevSecOps)

## Secure your agents

Agents are quickly becoming a new layer of the application stack. As developers build agents and move them into production, they need the tools to ship fast without sacrificing security, including built-in identity, governance, and safety testing. Security teams have overlapping needs: visibility into what’s running, control over what agents can access, and consistent governance across clouds and endpoints. Microsoft is delivering new solutions to help.

### Build secure agents from day one

At [Build 2026](https://build.microsoft.com/en-US/home), Microsoft is introducing new capabilities to help developers build secure, enterprise-ready agents by default. With the general availability of the [Agent 365 SDK](https://learn.microsoft.com/en-us/microsoft-365/agents-sdk/agents-sdk-overview), developers can integrate controls directly into their development workflows, bringing observability, access controls, and compliance enforcement into how agents are designed and deployed. This enables teams to build custom agents for any AI platform that are compliant, and enterprise-ready, and compose well with Agent 365.

Security extends beyond development and into how agents run. On Windows, the [Microsoft Execution Container (MXC)](https://github.com/microsoft/mxc) SDK provides OS-level control over agent execution, giving developers and IT teams the ability to define containment and policy, applied by the OS through isolation technologies such as process and session isolation. [Windows 365 for Agents](https://learn.microsoft.com/en-us/windows-365/agents/introduction-windows-365-for-agents), now generally available, enables you to run any agent in a fully isolated, policy-governed Cloud PC. Native Windows integration with Agent 365 provides a common foundation for observability, security, and governance, including built-in Intune capabilities to set policies that govern agent runtime execution and control how agents operate.

These [new capabilities](https://blogs.windows.com/windowsdeveloper/?p=57808) are now in early preview.

### Observe, govern, and secure agents at scale with Agent 365—now including local agents

As agents proliferate across environments, gaining visibility and control over them becomes critical. [Agent 365](https://www.microsoft.com/en-us/microsoft-agent-365) introduces new capabilities to manage agent sprawl and risk, including an Agent 365 Agent Registry that surfaces unmanaged local agents discovered by [Microsoft Defender](https://www.microsoft.com/en-us/security/business/microsoft-defender), [Microsoft Entra](https://www.microsoft.com/en-us/security/business/microsoft-entra), and [Microsoft Intune](https://www.microsoft.com/en-ie/security/business/microsoft-intune)—all working together. The registry supports more than 20 types of local agents, including coding agents, AI desktop applications, and both local and remote Model Context Protocol (MCP) servers. From there, Intune policies can be used to block common execution methods for OpenClaw agents.

Security teams also need the ability to defend against emerging threats without slowing developer productivity. Microsoft Defender, Entra, and Intune work together to provide the visibility, runtime protections, and context needed to manage agent risk without slowing developer productivity. Defender enables analysts to investigate agent activity using advanced hunting and provides an exposure graph that helps teams understand how agents are connected across the network. Preview of these capabilities coming soon.

Protecting data is foundational to securing agents at scale. [Microsoft Purview](https://www.microsoft.com/en-ie/security/business/microsoft-purview) controls to prevent data exfiltration, Data Security Posture Management risk discovery, and agentic risk detection for coding agents Claude Code, GitHub Copilot, OpenAI Codex, and OpenClaw. This enables visibility on how local agents access sensitive data, runtime protections for risky prompts, and insights into unsafe agent behaviors. [Microsoft Purview Audit](https://www.microsoft.com/en-ie/security/business/risk-management/microsoft-purview-audit) also logs all agent activity for full traceability. Preview of these capabilities coming soon.

[These capabilities are now in preview](https://techcommunity.microsoft.com/blog/microsoft-security-blog/securing-the-new-risk-surface-local-agents-claws-and-open-runtimes/4524602)

## Trust agents with your data

Developers also need direct, real-time insight into data security posture and risk signals associated with the agents they build. With Purview data risk signals embedded in the Foundry Control Plane, generally available, these signals provide guidance to developers on where to enforce protections before sensitive data is exposed. For example, Purview flags in real time when an agent surfaces sensitive financial data during testing and guides developers to mask or restrict access before deployment.

To further reduce risk, Purview introduces runtime data loss prevention (DLP) for agent prompts in Foundry, in preview with Agent 365. This capability detects, blocks, and audits sensitive data before it is processed by the agent, ensuring that sensitive information never reaches AI models.

[Learn more about Microsoft Purview for developers](https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-purview-enables-developers-with-strong-data-security-across-ai-apps-an/4524626)

## Secure your models

Before AI reaches production, teams need to verify that the models they depend on are safe. Now developers can inspect model artifacts, whether platform-native or bring-your-own, with [Defender AI model scanning](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-model-security?pivots=defender-portal), in preview. To help close gaps early model Defender AI model scanning detects and blocks potentially vulnerable or compromised models across registries, workspaces, and CI/CD pipelines to verify model integrity before deployment.

## Trust starts with security

There should never be a choice between innovation and safety.

The capabilities announced today span the full development lifecycle: discovering what’s exploitable, governing what’s running, protecting the data AI depends on, and verifying that agents behave as intended before they reach production. Microsoft security is embedded directly into the platforms and workflows developers already use, supporting innovation across [Microsoft Foundry](https://azure.microsoft.com/en-us/products/ai-foundry), [Copilot Studio](https://www.microsoft.com/en-us/microsoft-365-copilot/microsoft-copilot-studio), GitHub, and open-source frameworks, and bringing discovery and governance to shadow AI.

But real progress in AI depends on more than breakthrough capabilities—it depends on whether organizations can trust the systems they are building and deploying. That is the common thread across the innovations announced at [Build 2026](https://build.microsoft.com/en-US/home) and the principle guiding our approach. Because the future of AI will belong not just to those who move fastest, but to those who can innovate with trust.

To learn more about Microsoft Security solutions, visit our [website.](https://www.microsoft.com/en-us/security/business) Bookmark the [Security blog](https://www.microsoft.com/security/blog/) to keep up with our expert coverage on security matters. Also, follow us on LinkedIn ([Microsoft Security](https://www.linkedin.com/showcase/microsoft-security/)) and X ([@MSFTSecurity](https://twitter.com/@MSFTSecurity)) for the latest news and updates on cybersecurity. To learn more about how security is built into the Windows platform, explore the [Windows Security book](https://learn.microsoft.com/en-us/windows/security/book/) and [Windows Server Security book](https://aka.ms/ws2025securitybook).

The post [Microsoft Build 2026: Securing code, agents, and models across the development lifecycle](https://www.microsoft.com/en-us/security/blog/2026/06/02/microsoft-build-2026-securing-code-agents-and-models-across-the-development-lifecycle/) appeared first on [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog).
