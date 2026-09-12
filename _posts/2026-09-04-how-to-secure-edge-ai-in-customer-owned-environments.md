---
title: "[KO] How to secure edge AI in customer-owned environments"
date: 2026-09-04 19:10:10 +0000
categories: ["Agent 365"]
tags: ["frontier ai models"]
solution: agent-365
owners: ["akimcse"]
source_url: "https://www.microsoft.com/en-us/security/blog/2026/09/04/secure-edge-ai-customer-owned-environments/"
source_author: "Shayak Lahiri"
auto_generated: true
pin: false
---
> 본 글은 Microsoft Security Blog의 [How to secure edge AI in customer-owned environments](https://www.microsoft.com/en-us/security/blog/2026/09/04/secure-edge-ai-customer-owned-environments/) 글을 한국어로 번역·정리한 것입니다. 원문 작성자: Shayak Lahiri.
{: .prompt-info }

> ⚠️ 번역 엔진(Azure OpenAI) 미설정 — 원문 그대로 표시(테스트 스텁).

In this article
		

		
			
		
	
	
		
			- [Edge AI changes the trust model for AI systems](#edge-ai-changes-the-trust-model-for-ai-systems)
- [Constrain model actions through deterministic mediation](#constrain-model-actions-through-deterministic-mediation)
- [Establish trust before releasing sensitive assets](#establish-trust-before-releasing-sensitive-assets)
- [Verify runtime before releasing sensitive assets](#verify-runtime-before-releasing-sensitive-assets)
- [Verify artifacts that shape model behavior](#verify-artifacts-that-shape-model-behavior)
- [Next steps](#next-steps)
		
	
	

Edge AI moves model execution, model IP, customer data, and system authority into infrastructure the customer owns and operates. That changes who must verify the stack before sensitive assets are released.

[Edge AI](https://learn.microsoft.com/en-us/azure/azure-local/overview) includes AI systems where inference runs on or near the device, sensor, or other local environments where data is produced and acted on, rather than relying entirely on a centralized cloud service. It is chosen for cost, model selection, sovereignty, latency, and disconnected operation.

## Edge AI changes the trust model for AI systems

In Cloud AI, separate companies own and attest the hardware, platform, and model weights. Edge AI deployments often place customers in control of more of the AI stack. This changes the security model because the customer is now responsible for establishing trust across the environment where the AI operates.

In Edge AI, attacks such as prompt injection, model tampering, or malicious firmware updates can occur in the same environment that stores the model, customer data, credentials, and access to physical systems. This shifts trust decisions that were previously handled by cloud providers to the customer. Both the model provider and the customer now share risk: the provider’s models run on customer-owned infrastructure, while the customer must protect the systems, data, and models operating in that environment.

What changes with Edge AI?

- Customers operate more of the AI stack.

- AI systems can be influenced by prompts, retrieval data, agent instructions, and runtime inputs.

- Models, credentials, and data can live in environments outside the provider’s direct control.

- Traditional software security controls alone are not enough.

What should organizations do?

- Verify runtimes using attestation.

- Verify AI artifacts using provenance.

- Constrain model actions through mediation.

- Bind and release sensitive assets only to trusted environments.

Our [post on threat modeling for AI systems](https://aka.ms/aithreatmodeling) covers safety and security issues related to the underlying model. These concerns apply to Edge AI as well. Edge AI adds another question: before releasing weights, keys, or data, what evidence shows the runtime and loaded components can be trusted?

### Why Edge AI increases exposure

An Edge AI deployment may include models, prompts, agents, retrieval data, policies, local data stores, and update mechanisms running on infrastructure outside the provider’s cloud environment.

This moves sensitive AI assets and decision logic into potentially hostile environments. Attackers may have physical access to devices, local access to model artifacts, opportunities to tamper with retrieval data or tool configurations, compromise model supply chain and more direct paths from model behavior to real-world consequences.

Disconnected Edge deployments cannot rely on live cloud detection, policy updates, or revocation. They must maintain local verification and enforcement when cloud connectivity is unavailable. Risky AI operations should run only where hardware can protect assets and provide acceptable evidence. Otherwise, the operation should be deferred or revalidated.

### Why AI changes the security problem

Unlike conventional software, AI models can be influenced by untrusted content while still using legitimate interfaces and credentials. This article focuses on the security response: architectures that constrain model actions and protect the model, credentials, and data around it.

Traditional software executes code developers ship. AI systems can change behavior based on prompts, retrieval data, agent instructions, and other runtime inputs. Protecting code alone is no longer sufficient; organizations must also establish trust in the data, context, and actions surrounding the model.

- Prompt injection can change model behavior. Assume prompt injection will occur, whether direct or indirect. Inputs can affect systems  just like executable code because the context window itself acts as an instruction surface. Traditional controls such as signed binaries and code integrity checks were not designed to address this risk.

- Trusted data is not always safe data. Traditional vulnerability management does not map cleanly to “data as code,” such as a poisoned retrieval document. Origin signatures can prove where data came from, but they do not prove that the content is safe for an AI system to interpret.

- AI behavior is not fully deterministic. The same input may produce different outputs, and small context changes can significantly alter behavior. This limits the effectiveness of techniques such as signature detection and fuzzing. Grounding and tuning improve reliability, but they cannot enforce an acceptable risk boundary. At the authority boundaries it mediates, deterministic policy can still constrain actions when alignment, prompt-injection defenses, or content filters fail to stop an unsafe instruction.

Prompt injection, MCP, multi-agent systems, and computer-use agents on Edge expose different surfaces of these problems. Tool calls are delegated authority, agent output is untrusted input, and screen state is input, not authorization.

These characteristics mean organizations cannot rely on traditional software security controls alone. They also need to verify the environment where AI runs and constrain the actions an AI system is permitted to take.

## Constrain model actions through deterministic mediation

Model output should recommend actions, not authorize them. A deterministic mediator outside the model enforces policy by allowlisting actions, scoping arguments, limiting frequency, and releasing credentials only when approved. The mediator is a logical boundary, not another model. It may be provided by the platform or integrated by the customer.

In this pattern, the mediator and its credentials are protected and attested. Mediation bounds what the model can do but does not guarantee that every permitted action is safe; high-consequence or irreversible actions require independent approval, an interlock, or fail-safe behavior.

## Establish trust before releasing sensitive assets

Organizations must establish trust in the environment where AI runs and in the artifacts that shape AI behavior. Sensitive assets face two theft vectors: at-rest theft from stored artifacts and keys, and runtime theft while a compromised process holds them decrypted. Before release, the verifier asks two questions:

- Do I trust this runtime and the platform on which I am about to execute this workload?

- Do I trust these components, such as model weights, tool descriptors, agent definitions, and retrieval indexes, because I trust the system in which they were built and delivered?

Attestation answers the runtime question. Provenance answers the component question. Verifier policy requires both. Either question alone leaves a gap: an approved runtime can load a poisoned artifact, while a trusted artifact can run on a compromised platform. In this trust model, the build system that produced an artifact is treated as another runtime whose evidence is evaluated, and the chain continues until it reaches hardware the verifier accepts. Evidence comes from across the hardware, firmware, runtime, model, integration, and customer layers. It serves different relying parties: customers containing model behavior, publishers protecting model IP, and integrators validating the supply chain. The verifier combines that evidence to gate release.

## Verify runtime before releasing sensitive assets

This pattern evaluates a runtime by whether it is measurable, can report its state, and matches an approved baseline before sensitive assets are released.

Confidential compute provides one way to do this. Without end-to-end confidential computing, a privileged host or unprotected accelerator path may be able to read or modify decrypted weights, credentials, and data. GPU/NPU drivers and DMA extend the trusted computing base beyond ordinary application-security visibility. Where confidential computing covers that path within the platform’s documented threat model, protected memory and hardware-rooted attestation can support release to an approved runtime. This is designed to protect assets from host access; it does not constrain a steered model’s actions through authorized interfaces. Those vectors need additional controls.

Because system state can change after deployment, release is treated as a renewable lease that expires when fresh evidence no longer matches the approved state. Physical controls address what measurement cannot see.

In this pattern, evidence gates scheduler placement, storage, identity, and credential release. Bind credentials to the approved runtime and action scope to reduce the risk that credential theft enables bulk exfiltration; otherwise, evidence does not enforce trust.

## Verify artifacts that shape model behavior

Runtime trust proves only that the platform is acceptable; it does not prove that the artifacts loaded into it are trustworthy. A clean runtime can still execute a poisoned artifact.

That is why artifact trust has to be evaluated separately. Because these artifacts shape model behavior, accepting one into the system is more than data transfer. Creation, distribution, deployment, and use can each introduce a tampered artifact.

Model IP can extend beyond weights to provider-owned components that handle them; those components may warrant the same evidence-gated release.

In this pattern, approved components and updates enter through a trusted build environment; on-site changes appear as measurement drift rather than silently becoming a new baseline.

Each artifact should carry evidence of its origin, build pipeline, and input integrity. The verifier evaluates that evidence before accepting it. Provenance should chain to hardware and be produced inside a measured, policy-approved runtime. Signatures establish origin and integrity but may not show whether the producing runtime met verifier policy. Provenance helps responders reconstruct what happened: which model acted on which data, in what runtime, and under which policy.

## Next steps

Bottom line: Edge AI changes the trust model for AI systems. Customers operate more of the stack, AI behavior is influenced by runtime inputs, and sensitive assets run in environments outside the provider’s direct control. Attestation, provenance, mediation, and evidence-based release help establish trust before models, data, and credentials are exposed.

Edge AI pushes security controls into devices, gateways, vehicles, factories, hospitals, retail spaces, and other customer environments.

For depth on the agent case, see our [post on defense in depth for autonomous AI agents](https://aka.ms/agenticdefense). Map sensitive assets, the runtimes and artifacts that can access them, and the party responsible for each release decision. Then define the evidence and policy required at every boundary. At the Edge, security should be architectural: anchored at hardware, enforced at every action.

The post [How to secure edge AI in customer-owned environments](https://www.microsoft.com/en-us/security/blog/2026/09/04/secure-edge-ai-customer-owned-environments/) appeared first on [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog).
