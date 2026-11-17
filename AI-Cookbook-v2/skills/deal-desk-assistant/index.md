DD

# deal-desk-assistant

SalesSkillWrites need approval

Builds an order form from the approved template as a draft and checks required fields.

### Why it is needed

Reps rebuild order forms by hand. A missing field delays signature by days.

### Needs

-   Your approval for every write.

## Steps

1.  Find the approved order-form template with getTemplates.
2.  List required fields and ask for any missing ones.
3.  Create the envelope with status created, not sent.
4.  Show a summary. Send only after an explicit yes.

## Tools it calls

-   `getTemplates` · Find the template before any send or draft
-   `createEnvelope` · Draft (status created) or send from a template or remote URL

SKILL.md

**deal-desk-assistant/SKILL.md**

\---
name: deal-desk-assistant
description: Builds an order form from the approved template as a draft and checks required fields. Use with the Docusign connector.
---
# deal-desk-assistant

Why: Reps rebuild order forms by hand. A missing field delays signature by days.

Follows the docusign-agreements rules: read first, save drafts as created, approve before any write.

## Tools
- getTemplates
- createEnvelope

## Steps
1. Find the approved order-form template with getTemplates.
2. List required fields and ask for any missing ones.
3. Create the envelope with status created, not sent.
4. Show a summary. Send only after an explicit yes.

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

[signature-chaser](/PSA/AI-Cookbook-v2/skills/signature-chaser/) — Lists envelopes waiting 3+ days and drafts a nudge for each signer.

[renewal-brief](/PSA/AI-Cookbook-v2/skills/renewal-brief/) — One-page account brief: terms, expiry, auto-renewal and governing law.

[nudge-sender](/PSA/AI-Cookbook-v2/skills/nudge-sender/) — Sends approved reminders to pending remote signers on an existing envelope.

Source: /PSA/AI-Cookbook-v2/skills/deal-desk-assistant/
