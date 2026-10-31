---
title: "[KO] Inside a malicious Claude Code-branded extension and its persistent SSH backdoor"
date: 2026-10-31 01:02:57 +0000
categories: ["Agent 365"]
tags: ["frontier ai models", "supply chain attack"]
solution: agent-365
owners: ["akimcse"]
source_url: "https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/"
source_author: "Microsoft Security Research"
auto_generated: true
pin: false
---
> 본 글은 Microsoft Security Blog의 [Inside a malicious Claude Code-branded extension and its persistent SSH backdoor](https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/) 글을 한국어로 번역·정리한 것입니다. 원문 작성자: Microsoft Security Research.
{: .prompt-info }

> ⚠️ 번역 엔진(Azure OpenAI) 미설정 — 원문 그대로 표시(테스트 스텁).

In this article
		

		
			
		
	
	
		
			- [Attack chain overview](#attack-chain-overview)[Attack chain](#attack-chain)
- [Host reconnaissance collection](#host-reconnaissance-collection)
- [SSH authorization and tunnel identities](#ssh-authorization-and-tunnel-identities)
- [Protocol Tunneling (T1572): reverse SSH forwarding](#protocol-tunneling-t1572-reverse-ssh-forwarding)
- [Platform-specific startup persistence](#platform-specific-startup-persistence)
- [Mitigation and protection guidance](#mitigation-and-protection-guidance)[Immediate actions](#immediate-actions)
- [Remediation actions](#remediation-actions)
- [Follow-up Investigation and recovery](#follow-up-investigation-and-recovery)
- [Microsoft Defender XDR detections](#microsoft-defender-xdr-detections)
- [Threat intelligence reports](#threat-intelligence-reports)
- [Microsoft Defender XDR Threat analytics ](#microsoft-defender-xdr-threat-analytics)
- [Advanced hunting queries](#advanced-hunting-queries)
- [MITRE ATT&CK techniques](#mitre-att-ck-techniques)
- [Indicators of compromise (IOCs)](#indicators-of-compromise-iocs)
- [Learn More](#learn-more)
		
	
	

On October 29, 2026, Cursor reported that a tampered copy of Claude Code extension (anthropic.claude-code, versions 2.1.313 and 2.1.312) was available and served in the Cursor extension marketplace for a few hours to attempt a supply-chain attack on Cursor users. Cursor reports that it was live from about 2:27 AM to 1:35 PM Pacific Daylight Time (PDT). We have confirmed that the malicious packages found on Cursor marketplace were never published nor distributed from Microsoft Visual Studio Marketplace and from npm @antropic-ai/claude-code, which were not affected by this incident. Anthropic confirmed to Microsoft that their systems were not compromised and they did not develop the malicious package posted in Cursor marketplace. At this time, all evidence suggests that the incident is limited to Cursor marketplace.

Microsoft Threat Intelligence analyzed the injected JavaScript embedded in the malicious extension package. The injected loader runs when the extension module loads and attempts to add an attacker-controlled Secure Shell (SSH) key, enable the local SSH service, establish reverse SSH forwarding, configure persistence, and report host details. Successful remote access depends on host privileges, SSH configuration, and the attacker’s server configuration; however, the loader may still write keys and persistence artifacts even when tunnel access fails.

Organizations should identify systems that installed or automatically updated to this version from the Cursor marketplace, preserve evidence, remove confirmed malicious artifacts, review endpoint and network telemetry, and rotate credentials or revoke sessions when investigation indicates exposure. Microsoft customers can use the detections and hunting guidance in this post after the listed coverage and query validation gates are complete.

## Attack chain overview

A malicious artifact associated with the Cursor Marketplace incident included a JavaScript function that executed before the extension’s expected code. When the module loads, this function can use Node.js APIs to collect host information, modify files, and execute operating-system commands. The following sections describe capabilities and attempted actions based on our analysis of the injected code.

### Attack chain

The loader first collects host reconnaissance. It then attempts to install an SSH key, enable SSH, create a reverse tunnel, and configure persistence. A delayed callback subsequently attempts to send host details. The following sequence reflects code execution order; it does not prove that every step succeeded on every host.

- Module loading and reconnaissance collection. The injected function executes before normal extension initialization and collects host and user information.

- SSH access preparation. The loader appends an embedded public key and attempts to enable the local SSH service.

- Reverse forwarding. An embedded tunnel identity authenticates an outbound connection that requests forwarding to the workstation’s SSH port.

- Platform-specific persistence. Scripts and startup configuration are written to relaunch the connection.

- Host reconnaissance reporting. After the access and persistence setup attempts, a delayed callback attempts to transmit the previously collected host details and selected environment-variable names.

The loader uses embedded components and built-in system tools to establish persistent access without downloading another executable. It suppresses command output and silently catches errors to conceal failures and malicious activity, while the extension continues functioning normally to avoid alerting users.

### Host reconnaissance collection

The loader collects the hostname, username, operating system, architecture, home directory, working directory, and global Git email. It also looks for environment-variable names containing terms such as KEY, TOKEN, SECRET, PASS, AWS, or GCP, keeping up to forty matches.

The callback sends matching environment-variable names, not values. This reveals potentially sensitive configuration categories but does not demonstrate theft of the secrets stored in those variables.

Collection occurs during module loading. The collected details are retained for the delayed reporting callback described after the persistence stage.

### SSH authorization and tunnel identities

The loader uses two SSH identities with distinct roles. One public key authorizes access to the workstation’s user account, while a separate private key authenticates the outbound connection to the tunnel server. First, the loader checks the user’s authorized_keys file for the comment svc-telemetry. If the marker is missing, it appends an embedded Ed25519 public key. That creates an authorization entry for whoever holds the corresponding private key, subject to the local SSH server’s configuration.

Next, it decodes a separate private key for the outbound connection. The initial copy is written to a hidden temporary file named .stk_ followed by ten hexadecimal characters derived from the hostname and home directory. SSH receives that file through its -i option and connects using the remote account tunnel.

The public-key material is redacted but the format is similar to the following:

ssh-ed25519 [REDACTED PUBLIC KEY] svc-telemetry

### Protocol Tunneling (T1572): reverse SSH forwarding

The tunneling SSH process is launched with the command line containing the following arguments:

-N -R '*:0:localhost:22'

It requests a listening port on the remote SSH server and forwards connections through the tunnel to port 22 on the victim’s loopback interface. The remote port value 0 asks the server to allocate a port; it does not change the local target from port 22. The -N option tells SSH not to run a command on the tunnel server.

This design starts with an outbound connection from the workstation rather than waiting for a direct inbound connection to it. The loader disables ordinary host-key checking, bypasses the normal known-hosts file, sets keepalives, and avoids interactive prompts. On Unix-like systems it prefers autossh, falling back to ssh; on Windows it uses a hidden PowerShell loop. The loops wait sixty seconds after SSH exits before retrying.

A running SSH process does not necessarily mean the attacker gained access. Both the attacker’s server and the victim’s workstation must allow the connection, and server settings determine whether the tunnel is publicly reachable. Cursor reports that errors and administrator-permission requirements blocked SSH access on most macOS and Windows hosts. However, the malware could still attempt to plant its SSH key, establish persistence, and report host information.

### Platform-specific startup persistence

The loader writes platform-specific scripts and startup configuration outside the extension directory. The following table summarizes these mechanisms and their associated artifacts. The code attempts to configure persistence, but the presence of an artifact alone does not establish that the startup mechanism ran successfully.

On Unix-like systems, the .smt script reconstructs the persistent .smtk identity when it runs, then starts its own SSH retry loop. On Windows, the loader writes the identity and batch script directly.

The startup objects use names such as SysMon and com.apple.sysmond, which resemble monitoring components. Behind these names, their configured actions invoke the generated scripts that maintain reverse SSH forwarding.

## Mitigation and protection guidance

### Immediate actions

Run advanced hunting queries below to identify affected systems and investigate systems where users installed or automatically updated anthropic.claude-code version 2.1.313 and 2.1.312 through the Cursor Extension Marketplace. Review extension-installation records and correlate endpoint, network, file, process, and authentication telemetry with the published indicators. Preserve the extension package, modified SSH authorization files, generated keys and scripts, and startup configuration before cleanup. Isolate devices with evidence of loader execution or backdoor installation.

### Remediation actions

After evidence collection, check the affected user’s ~/.ssh/authorized_keys on macOS and Linux for the attacker-controlled key labeled svc-telemetry. On Windows, check both %USERPROFILE%\.ssh\authorized_keys and C:\ProgramData\ssh\administrators_authorized_keys, where present. Confirm the key against the fingerprint in Indicators of Compromise before removing the exact unauthorized entry. Preserve unrelated SSH keys and legitimate remote-development configuration. A missing marker alone should not replace review of the installation, process, network, and persistence evidence.

Remove the trojanized extension and confirmed malicious persistence after evidence collection. Inspect each startup object’s configured action before removal; names alone are not sufficient to distinguish malicious objects from legitimate monitoring software.

- macOS: Unload and remove the malicious user LaunchAgent at ~/Library/LaunchAgents/com.apple.sysmond.plist and remove its associated ~/.config/.smt script and ~/.config/.smtk identity.

- Linux: Remove the malicious user-crontab @reboot entry referencing ~/.config/.smt, preserving unrelated entries, and remove the associated script and ~/.config/.smtk identity.

- Windows: Remove the malicious SysMon scheduled task, the Startup-folder sysmon.cmd fallback, and associated %USERPROFILE%\.config\smt.cmd and %USERPROFILE%\.config\smtk files.

- All applicable platforms: Stop confirmed malicious SSH and retry processes and remove their temporary .stk_ identity files after collection.

Cursor published platform-specific checks and remediation scripts in its [security notice](https://cursor.com/blog/claude-code-extension-security-notice). Review the scripts and execution requirements before use, then verify that no listed artifacts remain. Cleanup does not replace investigation of device activity during the exposure window.

Removing or updating the extension does not remove artifacts written outside its installation directory. Remove confirmed unauthorized SSH keys, tunnel identities, scripts, and startup entries separately. Cursor’s reported server takedown does not remove artifacts already present on a device.

### Follow-up Investigation and recovery

Review telemetry after the extension loaded for SSH key acceptance, tunnel processes, local SSH sessions, command execution, and file activity. Rotate credentials and revoke sessions from a known-clean device when telemetry indicates credential access or when device trust cannot be restored. Rebuild the device when required by the investigation and verify that the tunnel and startup artifacts do not return after login or restart.

To reduce the risk of malicious extensions and extension-based supply chain attacks, organizations using Cursor should apply the relevant controls in [Cursor’s security-hardening guidance](https://cursor.com/docs/enterprise/security-hardening), including restricting extensions to approved publishers and configuring an extension installation cooldown to delay installation of newly published versions. These measures can help limit exposure to malicious releases.

### Microsoft Defender XDR detections

Microsoft Defender XDR customers can refer to the list of applicable detections below. Microsoft Defender XDR coordinates detection, prevention, investigation, and response across endpoints, identities, email, and apps to provide integrated protection against attacks like the threat discussed in this blog.

Customers with provisioned access can also use [Microsoft Security Copilot in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-in-microsoft-365-defender) to investigate and respond to incidents, hunt for threats, and protect their organization with relevant threat intelligence.

### Threat intelligence reports

Microsoft customers can use the following reports in Microsoft products to get the most up-to-date information about the threat actor, malicious activity, and techniques discussed in this blog. These reports provide intelligence, protection information, and recommended actions to prevent, mitigate, or respond to associated threats found in customer environments.

### Microsoft Defender XDR Threat analytics 

[Activity Profile: Malicious Claude Code branded extension v2.1.313 contains a persistent SSH backdoor](https://security.microsoft.com/threatanalytics3/19626f84-68aa-40bc-a18d-10eab01e2ffb)

### Advanced hunting queries

The following queries use the Microsoft Defender XDR advanced hunting schema and the time range selected in the portal. A result is an investigative lead, not proof of compromise.

Connections to the reported infrastructure

Find network events involving the reported IP address during the last 30 days, including the process responsible for each connection.

DeviceNetworkEvents
 | where Timestamp > ago(30d)
 | where RemoteIP == "134.209.82.225"
     or RemoteUrl has "134.209.82.225"
 | project Timestamp,
           DeviceName,
           InitiatingProcessFileName,
           InitiatingProcessCommandLine,
           RemoteIP,
           RemotePort,
           RemoteUrl

Reported malicious file and persistence artifacts

Find file events matching the reported SHA-256 hash, artifact filenames, or filename prefix during the last 30 days. Filename matches are hunting leads and require investigation.

DeviceFileEvents
 | where Timestamp > ago(30d)
 | where SHA256 == "ecb58cb29078d9646ad1dcdbe51526f2d9cfea06be5fb2ab183e8ecc3ab6bf15"
     or FileName in~ (
         ".smt",
         ".smtk",
         "smt.cmd",
         "smtk",
         "sysmon.cmd",
         "com.apple.sysmond.plist"
     )
     or FileName startswith ".stk_"
 | project Timestamp,
           DeviceName,
           ActionType,
           FolderPath,
           FileName,
           SHA256,
           InitiatingProcessFileName,
           InitiatingProcessCommandLine

SHA-256 values might not be populated for every file event. The filename and prefix conditions provide additional hunting leads.

Possible Windows scheduled-task persistence

Find scheduled-task creation events whose additional fields contain both reported terms, SysMon and smt, during the last 30 days.

DeviceEvents
 | where Timestamp > ago(30d)
 | where ActionType == "ScheduledTaskCreated"
 | where AdditionalFields has "SysMon"
     and AdditionalFields has "smt"
 | project Timestamp,
           DeviceName,
           AccountName,
           AdditionalFields,
           InitiatingProcessFileName,
           InitiatingProcessCommandLine

Possible macOS LaunchAgent persistence

Find plist-property modification events whose FolderPath matches the reported com.apple.sysmond.plist artifact.

DeviceEvents
 | where ActionType == "PlistPropertyModified"
 | where FolderPath has "com.apple.sysmond.plist"

### MITRE ATT&CK techniques

The following mappings describe behaviors implemented or attempted by the analyzed loader, not confirmed execution on every affected host. They do not establish attribution to a particular threat actor.

### Indicators of compromise (IOCs)

The following indicators are associated with the publicly analyzed JavaScript sample. The remote address is defanged. Contextual strings and paths require behavioral correlation and should not be treated as conclusive evidence of compromise on their own.

References

- Cursor, [Security notice — malicious version of Anthropic.claude-code (2.1.312 and 2.1.313) identified in the Cursor VS Code Extension Marketplace](https://cursor.com/blog/claude-code-extension-security-notice). Accessed October 30, 2026

## Learn More

For the latest security research from the Microsoft Threat Intelligence community, check out the [Microsoft Threat Intelligence Blog](https://aka.ms/threatintelblog).

To get notified about new publications and to join discussions on social media, follow us on [LinkedIn](https://www.linkedin.com/showcase/microsoft-threat-intelligence), [X (formerly Twitter)](https://x.com/MsftSecIntel), and [Bluesky](https://bsky.app/profile/threatintel.microsoft.com).

To hear stories and insights from the Microsoft Threat Intelligence community about the ever-evolving threat landscape, listen to the [Microsoft Threat Intelligence podcast](https://thecyberwire.com/podcasts/microsoft-threat-intelligence).

Review our documentation to learn more about our real-time protection capabilities and see how to enable them within your organization.  

- Learn more about [securing Copilot Studio agents with Microsoft Defender](https://learn.microsoft.com/en-us/defender-cloud-apps/ai-agent-protection) 

- Evaluate your AI readiness with our latest [Zero Trust for AI workshop](https://microsoft.github.io/zerotrustassessment/).

- [Microsoft 365 Copilot AI security documentation](https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-ai-security)

- [How Microsoft discovers and mitigates evolving attacks against AI guardrails](https://www.microsoft.com/en-us/security/blog/2024/04/11/how-microsoft-discovers-and-mitigates-evolving-attacks-against-ai-guardrails/)

- [Prompt injection protection in Microsoft Defender for Office 365 ](https://learn.microsoft.com/en-us/defender-office-365/step-by-step-guides/prompt-injection-protection-defender-for-office-365)– official documentation of the prompt injection protection in Microsoft Defender for Office 365.

- [How Microsoft discovers and mitigates evolving attacks against AI guardrails | Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2024/04/11/how-microsoft-discovers-and-mitigates-evolving-attacks-against-ai-guardrails/)

- [Manipulating AI memory for profit: The rise of AI Recommendation Poisoning | Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/02/10/ai-recommendation-poisoning/) – a related example of an AI-era technique observed in email traffic

- [Defending the inbox against prompt injection attacks | Microsoft Defender for Office 365 Blog ](https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/defending-the-inbox-against-prompt-injection-attacks/4534636)– feature announcement introducing prompt injection protection in Microsoft Defender for Office 365.

- Learn how Microsoft is reimagining the SOC for the agentic era with [ISOC in Microsoft Defender](https://www.microsoft.com/security/blog/2026/09/23/reimagining-the-soc-for-the-agentic-era-in-microsoft-defender/)

The post [Inside a malicious Claude Code-branded extension and its persistent SSH backdoor](https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/) appeared first on [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog).
