PA

# policy-ack-tracker

HRAutomationRead only

Finds policy acknowledgements still unsigned and groups them for a reminder list.

### Why it is needed

Compliance needs proof that everyone signed. Chasing from a spreadsheet is slow and error-prone.

### Needs

-   A scheduler. Claude scheduled tasks are confirmed; other platforms need their own.

## Steps

1.  Find envelopes for the named policy since the date.
2.  List unsigned recipients by manager.
3.  Draft reminders. Do not send.

## Tools it calls

-   `getEnvelopes` · Signing status, folders such as waiting\_for\_others, completed and voided
-   `listRecipients` · Who still has to act on an envelope

SKILL.md

**policy-ack-tracker/SKILL.md**

\---
name: policy-ack-tracker
description: Finds policy acknowledgements still unsigned and groups them for a reminder list. Use with the Docusign connector.
---
# policy-ack-tracker

Why: Compliance needs proof that everyone signed. Chasing from a spreadsheet is slow and error-prone.

Follows the docusign-agreements rules: read first, save drafts as created, approve before any write.

## Tools
- getEnvelopes
- listRecipients

## Steps
1. Find envelopes for the named policy since the date.
2. List unsigned recipients by manager.
3. Draft reminders. Do not send.

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

## Related HR skills

[onboarding-orchestrator](/PSA/AI-Cookbook-v2/skills/onboarding-orchestrator/) — Finds the onboarding Maestro workflow, confirms inputs and triggers it after approval. Then tracks packet status.

[offer-letter-sender](/PSA/AI-Cookbook-v2/skills/offer-letter-sender/) — Drafts an offer letter from the role template for review before anything is sent.

Source: /PSA/AI-Cookbook-v2/skills/policy-ack-tracker/
