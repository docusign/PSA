OO

# onboarding-orchestrator

HRSkillWrites need approval

Finds the onboarding Maestro workflow, confirms inputs and triggers it after approval. Then tracks packet status.

### Why it is needed

New hires wait on paperwork. The workflow runs the steps, and this skill keeps HR in control of inputs.

### Needs

-   Maestro workflows (IAM subscription).
-   Your approval for every write.

## Steps

1.  List Maestro workflows and pick the onboarding one.
2.  Get trigger requirements and confirm every input.
3.  Trigger only after approval. Workflows must use the From an API call start method.
4.  Report who still needs to sign.

## Tools it calls

-   `getWorkflowsList` · List Maestro workflows (active or paused)
-   `getWorkflowTriggerRequirements` · Inputs a Maestro workflow needs
-   `triggerWorkflow` · Start a Maestro workflow instance
-   `getEnvelopes` · Signing status, folders such as waiting\_for\_others, completed and voided

SKILL.md

**onboarding-orchestrator/SKILL.md**

\---
name: onboarding-orchestrator
description: Finds the onboarding Maestro workflow, confirms inputs and triggers it after approval. Then tracks packet status. Use with the Docusign connector.
---
# onboarding-orchestrator

Why: New hires wait on paperwork. The workflow runs the steps, and this skill keeps HR in control of inputs.

Follows the docusign-agreements rules: read first, save drafts as created, approve before any write.

## Tools
- getWorkflowsList
- getWorkflowTriggerRequirements
- triggerWorkflow
- getEnvelopes

## Steps
1. List Maestro workflows and pick the onboarding one.
2. Get trigger requirements and confirm every input.
3. Trigger only after approval. Workflows must use the From an API call start method.
4. Report who still needs to sign.

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

[offer-letter-sender](/PSA/AI-Cookbook-v2/skills/offer-letter-sender/) — Drafts an offer letter from the role template for review before anything is sent.

[policy-ack-tracker](/PSA/AI-Cookbook-v2/skills/policy-ack-tracker/) — Finds policy acknowledgements still unsigned and groups them for a reminder list.

Source: /PSA/AI-Cookbook-v2/skills/onboarding-orchestrator/
