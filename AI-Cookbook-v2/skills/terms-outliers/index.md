TO

# terms-outliers

Finance & RevOpsSkillRead only

Flags agreements with payment terms longer than 45 days.

### Why it is needed

Long payment terms affect cash flow and forecasting, and they often hide in old contracts.

### Needs

-   Nothing beyond the Docusign connector

## Steps

1.  Filter payment terms in the 60+ day values.
2.  Table with counterparty, term and renewal date.

## Tools it calls

-   `getAllAgreements` · Agreement terms: expiry, renewal, governing law, payment terms

SKILL.md

**terms-outliers/SKILL.md**

\---
name: terms-outliers
description: Flags agreements with payment terms longer than 45 days. Use with the Docusign connector.
---
# terms-outliers

Why: Long payment terms affect cash flow and forecasting, and they often hide in old contracts.

Follows the docusign-agreements rules: read first, save drafts as created, approve before any write.

## Tools
- getAllAgreements

## Steps
1. Filter payment terms in the 60+ day values.
2. Table with counterparty, term and renewal date.

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

## Related Finance & RevOps skills

[quarter-close-audit](/PSA/AI-Cookbook-v2/skills/quarter-close-audit/) — Checks that revenue documents are executed before quarter end and reports the gaps.

Source: /PSA/AI-Cookbook-v2/skills/terms-outliers/
