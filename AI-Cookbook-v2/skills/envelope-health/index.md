EH

# envelope-health

IT & AdminAutomationRead only

Daily view of voided, declined and timed-out envelopes with likely causes.

### Why it is needed

Failed sends often go unnoticed for days. A daily health check catches them early.

### Needs

-   A scheduler. Claude scheduled tasks are confirmed; other platforms need their own.

## Steps

1.  List envelopes in the last 24 hours with status Voided, Declined or TimedOut.
2.  Group by likely cause.
3.  Suggest one follow-up per group.

## Tools it calls

-   `getEnvelopes` · Signing status, folders such as waiting\_for\_others, completed and voided

SKILL.md

**envelope-health/SKILL.md**

\---
name: envelope-health
description: Daily view of voided, declined and timed-out envelopes with likely causes. Use with the Docusign connector.
---
# envelope-health

Why: Failed sends often go unnoticed for days. A daily health check catches them early.

Follows the docusign-agreements rules: read first, save drafts as created, approve before any write.

## Tools
- getEnvelopes

## Steps
1. List envelopes in the last 24 hours with status Voided, Declined or TimedOut.
2. Group by likely cause.
3. Suggest one follow-up per group.

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

## Related IT & Admin skills

[mcp-access-audit](/PSA/AI-Cookbook-v2/skills/mcp-access-audit/) — Reviews connector set-up before rollout: account, brands, users and approval gates.

Source: /PSA/AI-Cookbook-v2/skills/envelope-health/
