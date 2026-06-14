---
title: "[KO] Updating the taxonomy of failure modes in agentic AI systems: What a year of red teaming taught us"
date: 2026-06-04 19:14:42 +0000
categories: ["Agent 365"]
tags: ["frontier ai models"]
solution: agent-365
owners: ["akimcse"]
source_url: "https://www.microsoft.com/en-us/security/blog/2026/06/04/updating-taxonomy-failure-modes-agentic-ai-systems-year-red-teaming-taught-us/"
source_author: "Microsoft AI Red Team"
auto_generated: true
pin: false
---
> 본 글은 Microsoft Security Blog의 [Updating the taxonomy of failure modes in agentic AI systems: What a year of red teaming taught us](https://www.microsoft.com/en-us/security/blog/2026/06/04/updating-taxonomy-failure-modes-agentic-ai-systems-year-red-teaming-taught-us/) 글을 한국어로 번역·정리한 것입니다. 원문 작성자: Microsoft AI Red Team.
{: .prompt-info }

> ⚠️ 번역 엔진(Azure OpenAI) 미설정 — 원문 그대로 표시(테스트 스텁).

In this article
		

		
			
		
	
	
		
			- [Why the Taxonomy Needed Updating](#why-the-taxonomy-needed-updating)
- [Seven new failure modes](#seven-new-failure-modes)
- [Operational findings: What red teaming showed](#operational-findings-what-red-teaming-showed)
- [New mitigations](#new-mitigations)
- [What to do this quarter](#what-to-do-this-quarter)
		
	
	

When the Microsoft AI Red Team published the [Taxonomy of Failure Modes in Agentic AI Systems](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Taxonomy-of-Failure-Mode-in-Agentic-AI-Systems-Whitepaper.pdf) in April 2025, the goal was a shared vocabulary for a threat landscape that did not fit existing frameworks. The v1.0 taxonomy was largely forward-looking, built on practitioner interviews, cross-company threat modeling, and our own early operational experience. It identified novel failure modes unique to agentic systems (agent compromise, injection, impersonation, flow manipulation) alongside existing failure modes materially amplified in agentic contexts (memory poisoning, cross-domain prompt injection, human-in-the-loop bypass). 

Twelve months later, [the evidence base has shifted enough to warrant a v2.0](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/security/Taxonomy-of-Failure-Modes-in-Agentic-AI-Systems-v2-0.pdf). The update adds seven new failure mode categories, expands the mitigations section, and grounds the framework in 12 months of red team engagements against deployed agentic systems.

## Why the Taxonomy Needed Updating

Four developments drove the revision. 

Open-source agentic frameworks went mainstream faster than the security community was ready for. OpenClaw, launched in January 2026, accumulated over 336,000 GitHub stars and spawned more than 2,100 agents within 48 hours of release. A security audit conducted shortly after launch identified 512 vulnerabilities including CVE-2026-25253, a one-click RCE via WebSocket hijacking. Over 1,800 exposed instances were leaking API keys and credentials within the first week, and 336 malicious plugins were found in the skills marketplace, including credential stealers masquerading as trading bots. 

The MCP ecosystem matured — and accumulated vulnerabilities at scale. The Model Context Protocol became the de facto standard for connecting models to external tools. In 2025, 99 CVEs were published for MCP-related software, and tool poisoning moved from theoretical risk to live attack surface. 

Computer-use agents moved from research to production. Agents that observe and interact with graphical interfaces introduce attack surfaces with no analogue in earlier AI security work, and expose previously human-targeted attack patterns to LLMs. The original taxonomy lacked dedicated coverage for this capability class; operational experience made clear it requires its own category. 

Twelve months of red team operations provided empirical grounding. The v1.0 taxonomy was forward-looking. The v2.0 update is grounded in patterns observed across real engagements with findings that confirmed some predictions, falsified others, and surfaced failure modes that were not anticipated. 

## Seven new failure modes

1. Agentic Supply Chain Compromise. Agentic systems consume plugin registries, MCP servers, prompt templates, and third-party tool integrations, each a new supply chain ingestion point. Unlike traditional supply chain compromise, which delivers malicious code, a compromised agentic supply chain component injects natural-language instructions that alter agent behavior without touching any binary. This is a novel failure mode: the attack surface did not exist before agents began consuming natural-language tool definitions from third-party registries. 

2. Goal Hijacking. The original taxonomy covered agent compromise but did not sufficiently distinguish the mechanism of compromise from the strategic objective of redirecting the agent’s goal state. Goal hijacking captures a specific pattern, when adversarial instructions that appear aligned with legitimate task completion silently redirecting the agent’s terminal goal, without fully compromising the underlying agent. 

3. Inter-Agent Trust Escalation. Multi-agent architectures involve delegation chains where orchestrators pass tasks to other agents. This entry addresses privilege escalation that becomes possible when a compromised agent asserts false identity or inflates claimed permissions to an orchestrator that does not independently verify them. The pattern mirrors confused deputy problems in traditional software, but the confusion is induced through natural language rather than system calls. 

4. Computer Use Agent (CUA) Visual Attack. Agents operating through graphical interfaces can be manipulated through visual content that appears innocuous to humans but carries adversarial instructions for the agent. Attack patterns include hidden text rendered at non-human-readable scale, UI elements positioned outside the visible viewport, and images embedding prompt injection in content the agent is instructed to interpret. This failure mode has no meaningful precedent in v1.0. 

5. Session Context Contamination. Agentic sessions often span extended, multi-step interactions with context accumulating from prior steps. Session context contamination occurs when an adversary introduces data early in a session that biases the agent’s reasoning in subsequent steps, without triggering safety controls at any individual step. 

6. MCP / Plugin Abuse. The original taxonomy’s coverage of function compromise predated standardization around MCP and plugin protocols. This entry captures attack surfaces specific to those protocols: tool description poisoning, server-side instruction injection, cross-server instruction override (a malicious server overriding behavior of trusted servers), and abuse of protocol-level trust assumptions. 

7. Capability / Architecture Disclosure. This failure mode occurs when an agent reveals internal implementation details such as tool names and schemas, system-prompt structure, memory interfaces, or consent/HitL trigger logic, either on direct request or via paths such as XPIA. In single-turn chat, prompt leakage is mostly reputational. In agentic systems, it exposes operational primitives and turns black-box probing into a white-box exploit path. 

## Operational findings: What red teaming showed

Twelve months of engagements against deployed agentic systems produced several consistent patterns. 

HitL bypass was the most consistently exploited failure mode, at very high frequency. Red teamers achieved bypass through consent fatigue, manipulation of probabilistic invocation, and incremental escalation chains where no individual step clearly warranted review but the compound outcome did. Most significantly, several engagements demonstrated zero-click end-to-end chains starting from an external input with no human interaction beyond the initial agent invocation, achieving high-impact outcomes such as exfiltration or lateral movement. 

XPIA and memory poisoning were observed at high frequency and frequently combined. Cross-domain prompt injection delivered via external content remained the most reliable initial access vector. Memory poisoning via XPIA, where injected instructions seed the agent’s persistent memory for later retrieval, requires only a single successful injection, which the agent then propagates across subsequent sessions. 

Session context contamination and incremental escalation were highly effective and difficult to detect. Neither the contaminating input nor any individual escalation step is clearly anomalous in isolation. Detection requires behavioral analysis across the full session, something most systems did not have. 

Capability disclosure was a key enabler of follow-on attack paths. In many of our highest-impact attack chains, execution was predicated on extracting specific architecture or capability details from the system. This often required only asking the system directly, but it consistently exposed inconsistencies in guardrails and opened attack paths that would otherwise have required external reconnaissance. 

## New mitigations

Supply chain security for agentic components. Treat every external component an agent can consume as part of the software supply chain. SBOM generation for agent deployments inclusive of tool dependencies; signature and provenance verification for MCP servers and plugins before installation; registry scanning for hidden instructions in tool descriptions; version pinning with change monitoring for all external tool definitions. 

Zero-trust inter-agent architecture. For high-risk scenarios, agent identity should be cryptographically established, not assumed from position in a workflow. Every inter-agent message should carry a verifiable identity claim. Orchestrators should not grant elevated permissions to sub-agents based on self-asserted role. 

Consent architecture hardening. HitL controls must resist the specific patterns observed in red team operations: compound action decomposition before approval presentation, semantic summarization of agent-constructed descriptions to prevent description laundering, tiered approval requirements that scale with action reversibility and blast radius, deterministic HitL invocation, and anomaly detection on approval request frequency and pattern. 

Adversarial session hardening. Mitigating session context contamination requires treating the agent’s accumulated context as a security-relevant data structure. Controls include context provenance tracking, structured separation between trusted system context and untrusted retrieved content, session integrity monitoring for anomalous accumulation patterns, and bounded session contexts that limit how much external content can influence a session’s reasoning. 

## What to do this quarter

If you operate or defend an agentic system, the v2.0 additions translate to four concrete actions: 

- Inventory your supply chain. Generate an SBOM for every deployed agent that includes plugins, MCP servers, prompt templates, and tool descriptions alongside code dependencies. Pin versions; treat natural-language tool descriptions as code. 

- Verify agent identity cryptographically, not positionally. Issue attestable credentials at provisioning. Reject self-asserted role claims at orchestrator handoffs. 

- Add the seven new categories to your red-team coverage matrix. Treat CUA visual attacks, session context contamination, capability disclosure, and goal hijacking as mandatory test classes for any agent that touches production data or external surfaces. 

- Audit human-in-the-loop UX as a security control. Decompose compound actions, summarize approval prompts from the underlying tool calls (not from the agent’s own description), tier approvals by reversibility, and monitor approval frequency for consent-fatigue exploitation signals. 

If you are building agentic systems, the updated taxonomy is a threat modeling tool, not a compliance checklist. Take each failure mode category and ask whether it can occur in your system, under what conditions, and whether you have a control that would detect or prevent it. 

For red teamers: the seven new categories should be mandatory coverage areas. Zero-click HitL bypass chains, inter-agent trust escalation, and session context contamination will not be surfaced by model-level evaluation alone. They require system-level testing and multi-step attack chains evaluated across complete task flows. 

For security engineers: supply chain and zero-trust mitigations are architectural decisions, and difficult to retrofit. Building SBOM generation, tool provenance verification, and inter-agent authentication into your architecture from the start costs substantially less than adding them after deployment. 

The taxonomy is a living document. The failure modes added in v2.0 are the ones that twelve months of operational data made compelling enough to include. As agentic systems acquire new capabilities — persistent cross-session memory at scale, autonomous agent spawning, physical environment interaction — the failure mode surface will continue to expand. We will continue to update the taxonomy as the evidence base develops. 

[The updated whitepaper is available now](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/security/Taxonomy-of-Failure-Modes-in-Agentic-AI-Systems-v2-0.pdf). We welcome engagement from practitioners whose operational experience identifies failure modes or attack patterns not yet reflected in the taxonomy. 

The post [Updating the taxonomy of failure modes in agentic AI systems: What a year of red teaming taught us ](https://www.microsoft.com/en-us/security/blog/2026/06/04/updating-taxonomy-failure-modes-agentic-ai-systems-year-red-teaming-taught-us/) appeared first on [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog).
