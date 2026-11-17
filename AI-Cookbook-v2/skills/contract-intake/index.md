CI

# contract-intake

LegalSkillWrites need approval

Turns a contract request into the right CLM workflow with the required inputs.

### Why it is needed

Intake is where contract requests stall. A standard starter removes back-and-forth.

### Needs

-   CLM workflows (CLM and IAM setup).
-   Your approval for every write.

## Steps

1.  Identify the contract type.
2.  List CLM workflows and pick the match.
3.  Collect inputs. Resolve documents from existing agreements.
4.  Start after approval.

## Tools it calls

-   `getClmWorkflowDefinitions` · List CLM workflow definitions
-   `startClmWorkflow` · Start a CLM workflow by name
-   `getAllAgreements` · Agreement terms: expiry, renewal, governing law, payment terms

SKILL.md

**contract-intake/SKILL.md**

\---
name: contract-intake
description: Turns a contract request into the right CLM workflow with the required inputs. Use with the Docusign connector.
---
# contract-intake

Why: Intake is where contract requests stall. A standard starter removes back-and-forth.

Follows the docusign-agreements rules: read first, save drafts as created, approve before any write.

## Tools
- getClmWorkflowDefinitions
- startClmWorkflow
- getAllAgreements

## Steps
1. Identify the contract type.
2. List CLM workflows and pick the match.
3. Collect inputs. Resolve documents from existing agreements.
4. Start after approval.

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

[provision-sweep](/PSA/AI-Cookbook-v2/skills/provision-sweep/) — Finds agreements by governing law, term or custom provision and flags partial results.

[expiry-digest](/PSA/AI-Cookbook-v2/skills/expiry-digest/) — Monthly digest of agreements expiring in the next 120 days, grouped by month, with the top three to review.

Source: /PSA/AI-Cookbook-v2/skills/contract-intake/
