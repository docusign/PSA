OL

# offer-letter-sender

HRSkillWrites need approval

Drafts an offer letter from the role template for review before anything is sent.

### Why it is needed

Offer letters are high-stakes. A draft review step prevents wrong salary or start-date errors.

### Needs

-   Your approval for every write.

## Steps

1.  Pick the offer template for the role.
2.  Fill required fields from the candidate record.
3.  Save as a draft with status created.
4.  Show the summary. Send only on yes.

## Tools it calls

-   `getTemplates` · Find the template before any send or draft
-   `createEnvelope` · Draft (status created) or send from a template or remote URL

SKILL.md

**offer-letter-sender/SKILL.md**

\---
name: offer-letter-sender
description: Drafts an offer letter from the role template for review before anything is sent. Use with the Docusign connector.
---
# offer-letter-sender

Why: Offer letters are high-stakes. A draft review step prevents wrong salary or start-date errors.

Follows the docusign-agreements rules: read first, save drafts as created, approve before any write.

## Tools
- getTemplates
- createEnvelope

## Steps
1. Pick the offer template for the role.
2. Fill required fields from the candidate record.
3. Save as a draft with status created.
4. Show the summary. Send only on yes.

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

[policy-ack-tracker](/PSA/AI-Cookbook-v2/skills/policy-ack-tracker/) — Finds policy acknowledgements still unsigned and groups them for a reminder list.

Source: /PSA/AI-Cookbook-v2/skills/offer-letter-sender/
