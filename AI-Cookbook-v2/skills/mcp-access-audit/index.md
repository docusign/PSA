MA

# mcp-access-audit

IT & AdminSkillRead only

Reviews connector set-up before rollout: account, brands, users and approval gates.

### Why it is needed

Admins need a checklist before a new team gets MCP access. This produces it in one pass.

### Needs

-   Nothing beyond the Docusign connector

## Steps

1.  Read account information.
2.  Summarize brands and users.
3.  Check MCP is enabled and approval gates are set.
4.  Return a checklist. Read only.

## Tools it calls

-   `getAccount` · See tool reference
-   `getBrands` · See tool reference
-   `getUsers` · See tool reference

SKILL.md

**mcp-access-audit/SKILL.md**

\---
name: mcp-access-audit
description: Reviews connector set-up before rollout: account, brands, users and approval gates. Use with the Docusign connector.
---
# mcp-access-audit

Why: Admins need a checklist before a new team gets MCP access. This produces it in one pass.

Follows the docusign-agreements rules: read first, save drafts as created, approve before any write.

## Tools
- getAccount
- getBrands
- getUsers

## Steps
1. Read account information.
2. Summarize brands and users.
3. Check MCP is enabled and approval gates are set.
4. Return a checklist. Read only.

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

[envelope-health](/PSA/AI-Cookbook-v2/skills/envelope-health/) — Daily view of voided, declined and timed-out envelopes with likely causes.

Source: /PSA/AI-Cookbook-v2/skills/mcp-access-audit/
