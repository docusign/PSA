ED

# expiry-digest

LegalAutomationRead only

Monthly digest of agreements expiring in the next 120 days, grouped by month, with the top three to review.

### Why it is needed

Expiries slip past owners. A standing digest puts them in front of legal before notice dates pass.

### Needs

-   A scheduler. Claude scheduled tasks are confirmed; other platforms need their own.

## Steps

1.  Filter expiry between today and +120 days.
2.  Group by month with owner and renewal type.
3.  Name the top 3 to review and why.

## Tools it calls

-   `getAllAgreements` · Agreement terms: expiry, renewal, governing law, payment terms

SKILL.md

**expiry-digest/SKILL.md**

\---
name: expiry-digest
description: Monthly digest of agreements expiring in the next 120 days, grouped by month, with the top three to review. Use with the Docusign connector.
---
# expiry-digest

Why: Expiries slip past owners. A standing digest puts them in front of legal before notice dates pass.

Follows the docusign-agreements rules: read first, save drafts as created, approve before any write.

## Tools
- getAllAgreements

## Steps
1. Filter expiry between today and +120 days.
2. Group by month with owner and renewal type.
3. Name the top 3 to review and why.

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

## Related Legal skills

[contract-intake](/PSA/AI-Cookbook-v2/skills/contract-intake/) — Turns a contract request into the right CLM workflow with the required inputs.

[provision-sweep](/PSA/AI-Cookbook-v2/skills/provision-sweep/) — Finds agreements by governing law, term or custom provision and flags partial results.

Source: /PSA/AI-Cookbook-v2/skills/expiry-digest/
