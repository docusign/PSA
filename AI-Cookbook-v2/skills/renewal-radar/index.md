RR

# renewal-radar

ProcurementAutomationRead only

Lists auto-renewals due in 90 days with open notice windows. Runs weekly as a scheduled task.

### Why it is needed

Missed notice windows lock in renewals. Procurement needs the list before the window closes.

### Needs

-   A scheduler. Claude scheduled tasks are confirmed; other platforms need their own.

## Steps

1.  Get the filter fields with getAgreementFilterSkill.
2.  Filter for auto-renewal with notice dates in the next 90 days.
3.  Flag any notice window that has already opened.
4.  Return a table sorted by renewal date.

## Tools it calls

-   `getAgreementFilterSkill` · Exact filter fields and OData syntax
-   `getAllAgreements` · Agreement terms: expiry, renewal, governing law, payment terms

SKILL.md

**renewal-radar/SKILL.md**

\---
name: renewal-radar
description: Lists auto-renewals due in 90 days with open notice windows. Runs weekly as a scheduled task. Use with the Docusign connector.
---
# renewal-radar

Why: Missed notice windows lock in renewals. Procurement needs the list before the window closes.

Follows the docusign-agreements rules: read first, save drafts as created, approve before any write.

## Tools
- getAgreementFilterSkill
- getAllAgreements

## Steps
1. Get the filter fields with getAgreementFilterSkill.
2. Filter for auto-renewal with notice dates in the next 90 days.
3. Flag any notice window that has already opened.
4. Return a table sorted by renewal date.

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

## Related Procurement skills

[vendor-nda-gate](/PSA/AI-Cookbook-v2/skills/vendor-nda-gate/) — Checks for an existing NDA before drafting a new one.

[term-comparator](/PSA/AI-Cookbook-v2/skills/term-comparator/) — Compares payment, termination, liability and governing law across vendors in one table.

Source: /PSA/AI-Cookbook-v2/skills/renewal-radar/
