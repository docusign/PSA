SC

# signature-chaser

SalesSkillRead only

Lists envelopes waiting 3+ days and drafts a nudge for each signer.

### Why it is needed

Stalled signatures are the fastest revenue leak. Reps forget to chase, and the nudge sits in a notes app.

### Needs

-   Nothing beyond the Docusign connector

## Steps

1.  Call getEnvelopes with folder waiting\_for\_others, sent in the last 60 days.
2.  Keep envelopes waiting 3 days or more, oldest first.
3.  Group by signer with listRecipients.
4.  Draft a nudge for each. Never send.

## Tools it calls

-   `getEnvelopes` · Signing status, folders such as waiting\_for\_others, completed and voided
-   `listRecipients` · Who still has to act on an envelope

SKILL.md

**signature-chaser/SKILL.md**

\---
name: signature-chaser
description: Lists envelopes waiting 3+ days and drafts a nudge for each signer. Use with the Docusign connector.
---
# signature-chaser

Why: Stalled signatures are the fastest revenue leak. Reps forget to chase, and the nudge sits in a notes app.

Follows the docusign-agreements rules: read first, save drafts as created, approve before any write.

## Tools
- getEnvelopes
- listRecipients

## Steps
1. Call getEnvelopes with folder waiting\_for\_others, sent in the last 60 days.
2. Keep envelopes waiting 3 days or more, oldest first.
3. Group by signer with listRecipients.
4. Draft a nudge for each. Never send.

Works with (install by platform)

| Platform | How to install | Support |
| --- | --- | --- |
| **Claude** | Upload the skill folder under Skills. Automations run as scheduled tasks. | Native |
| **GitHub Copilot / VS Code** | Place the folder in .github/skills and add the MCP server to the workspace. | Native |
| **Gemini CLI** | Place the folder in .gemini/skills. | Native (CLI) |
| **ChatGPT** | Upload if your plan shows Skills; otherwise paste into Project or GPT instructions. | Reported |
| **Microsoft Copilot Studio** | Paste the body into agent Instructions and add the Docusign connector as a tool. Upload where offered. | Pasted instructions; upload reported |
| **Gemini Enterprise** | Paste the body into the agent instructions. | Pasted instructions |
| **Perplexity / Slackbot** | Save the compact version as a saved prompt or channel instruction. No folder upload. | Not confirmed |

## Related Sales skills

[deal-desk-assistant](/PSA/AI-Cookbook-v2/skills/deal-desk-assistant/) — Builds an order form from the approved template as a draft and checks required fields.

[renewal-brief](/PSA/AI-Cookbook-v2/skills/renewal-brief/) — One-page account brief: terms, expiry, auto-renewal and governing law.

[nudge-sender](/PSA/AI-Cookbook-v2/skills/nudge-sender/) — Sends approved reminders to pending remote signers on an existing envelope.

Source: /PSA/AI-Cookbook-v2/skills/signature-chaser/
