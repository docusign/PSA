AU

# account-update-tracker

CX FINSSkillRead only

Tracks account-update envelopes waiting on customer or staff signers, by step.

### Why it is needed

Account updates are compliance-sensitive and time-bound. Stuck steps cost customers their service.

### Needs

-   Nothing beyond the Docusign connector

## Steps

1.  Find account-update envelopes from the last 30 days.
2.  Group by step and days outstanding.
3.  Flag anything over 5 days. Read only.

## Tools it calls

-   `getEnvelopes` · Signing status, folders such as waiting\_for\_others, completed and voided

SKILL.md

**account-update-tracker/SKILL.md**

\---
name: account-update-tracker
description: Tracks account-update envelopes waiting on customer or staff signers, by step. Use with the Docusign connector.
---
# account-update-tracker

Why: Account updates are compliance-sensitive and time-bound. Stuck steps cost customers their service.

Follows the docusign-agreements rules: read first, save drafts as created, approve before any write.

## Tools
- getEnvelopes

## Steps
1. Find account-update envelopes from the last 30 days.
2. Group by step and days outstanding.
3. Flag anything over 5 days. Read only.

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

Source: /PSA/AI-Cookbook-v2/skills/account-update-tracker/
