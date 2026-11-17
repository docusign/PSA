PS

# provision-sweep

LegalSkillRead only

Finds agreements by governing law, term or custom provision and flags partial results.

### Why it is needed

Legal teams answer 'where do we have X?' questions after a policy change, fast and with evidence.

### Needs

-   Nothing beyond the Docusign connector

## Steps

1.  Build an equality-only OData filter.
2.  For 'not' questions, exclude matches in the summary.
3.  Flag partial results.
4.  Summarize outliers. No legal advice.

## Tools it calls

-   `getAgreementFilterSkill` · Exact filter fields and OData syntax
-   `getAllAgreements` · Agreement terms: expiry, renewal, governing law, payment terms

SKILL.md

**provision-sweep/SKILL.md**

\---
name: provision-sweep
description: Finds agreements by governing law, term or custom provision and flags partial results. Use with the Docusign connector.
---
# provision-sweep

Why: Legal teams answer 'where do we have X?' questions after a policy change, fast and with evidence.

Follows the docusign-agreements rules: read first, save drafts as created, approve before any write.

## Tools
- getAgreementFilterSkill
- getAllAgreements

## Steps
1. Build an equality-only OData filter.
2. For 'not' questions, exclude matches in the summary.
3. Flag partial results.
4. Summarize outliers. No legal advice.

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

[expiry-digest](/PSA/AI-Cookbook-v2/skills/expiry-digest/) — Monthly digest of agreements expiring in the next 120 days, grouped by month, with the top three to review.

Source: /PSA/AI-Cookbook-v2/skills/provision-sweep/
