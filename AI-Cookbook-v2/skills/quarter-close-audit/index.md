QA

# quarter-close-audit

Finance & RevOpsSkillRead only

Checks that revenue documents are executed before quarter end and reports the gaps.

### Why it is needed

Revenue recognition needs signed paper. Finding gaps in the last week of a quarter is too late.

### Needs

-   Nothing beyond the Docusign connector

## Steps

1.  List order forms and SOWs still open.
2.  Match them to executed agreements.
3.  Report gaps with names and dates.

## Tools it calls

-   `getEnvelopes` · Signing status, folders such as waiting\_for\_others, completed and voided
-   `getAllAgreements` · Agreement terms: expiry, renewal, governing law, payment terms

SKILL.md

**quarter-close-audit/SKILL.md**

\---
name: quarter-close-audit
description: Checks that revenue documents are executed before quarter end and reports the gaps. Use with the Docusign connector.
---
# quarter-close-audit

Why: Revenue recognition needs signed paper. Finding gaps in the last week of a quarter is too late.

Follows the docusign-agreements rules: read first, save drafts as created, approve before any write.

## Tools
- getEnvelopes
- getAllAgreements

## Steps
1. List order forms and SOWs still open.
2. Match them to executed agreements.
3. Report gaps with names and dates.

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

[terms-outliers](/PSA/AI-Cookbook-v2/skills/terms-outliers/) — Flags agreements with payment terms longer than 45 days.

Source: /PSA/AI-Cookbook-v2/skills/quarter-close-audit/
