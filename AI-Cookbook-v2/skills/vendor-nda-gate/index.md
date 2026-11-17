NG

# vendor-nda-gate

ProcurementSkillWrites need approval

Checks for an existing NDA before drafting a new one.

### Why it is needed

Duplicate NDAs waste legal time and slow vendor onboarding.

### Needs

-   Your approval for every write.

## Steps

1.  Search agreements for the vendor.
2.  If a valid NDA exists, stop and report its dates.
3.  Otherwise draft from the approved mutual NDA template, status created.
4.  Ask for approval before anything is sent.

## Tools it calls

-   `getAllAgreements` · Agreement terms: expiry, renewal, governing law, payment terms
-   `getTemplates` · Find the template before any send or draft
-   `createEnvelope` · Draft (status created) or send from a template or remote URL

SKILL.md

**vendor-nda-gate/SKILL.md**

\---
name: vendor-nda-gate
description: Checks for an existing NDA before drafting a new one. Use with the Docusign connector.
---
# vendor-nda-gate

Why: Duplicate NDAs waste legal time and slow vendor onboarding.

Follows the docusign-agreements rules: read first, save drafts as created, approve before any write.

## Tools
- getAllAgreements
- getTemplates
- createEnvelope

## Steps
1. Search agreements for the vendor.
2. If a valid NDA exists, stop and report its dates.
3. Otherwise draft from the approved mutual NDA template, status created.
4. Ask for approval before anything is sent.

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

[renewal-radar](/PSA/AI-Cookbook-v2/skills/renewal-radar/) — Lists auto-renewals due in 90 days with open notice windows. Runs weekly as a scheduled task.

[term-comparator](/PSA/AI-Cookbook-v2/skills/term-comparator/) — Compares payment, termination, liability and governing law across vendors in one table.

Source: /PSA/AI-Cookbook-v2/skills/vendor-nda-gate/
