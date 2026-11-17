RB

# renewal-brief

SalesSkillRead only

One-page account brief: terms, expiry, auto-renewal and governing law.

### Why it is needed

Gives the AE the contract facts before a renewal call, so nobody guesses terms in front of the customer.

### Needs

-   Nothing beyond the Docusign connector

## Steps

1.  Route the request with getEnvelopeVsAgreementSkill.
2.  Find all agreements for the account.
3.  Extract expiry, renewal type and governing law.
4.  Flag anything due in 120 days.

## Tools it calls

-   `getEnvelopeVsAgreementSkill` · Route a request to agreements, envelopes or both
-   `getAllAgreements` · Agreement terms: expiry, renewal, governing law, payment terms
-   `getAgreementDetails` · Full record for one agreement

SKILL.md

**renewal-brief/SKILL.md**

\---
name: renewal-brief
description: One-page account brief: terms, expiry, auto-renewal and governing law. Use with the Docusign connector.
---
# renewal-brief

Why: Gives the AE the contract facts before a renewal call, so nobody guesses terms in front of the customer.

Follows the docusign-agreements rules: read first, save drafts as created, approve before any write.

## Tools
- getEnvelopeVsAgreementSkill
- getAllAgreements
- getAgreementDetails

## Steps
1. Route the request with getEnvelopeVsAgreementSkill.
2. Find all agreements for the account.
3. Extract expiry, renewal type and governing law.
4. Flag anything due in 120 days.

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

## Related Sales skills

[signature-chaser](/PSA/AI-Cookbook-v2/skills/signature-chaser/) — Lists envelopes waiting 3+ days and drafts a nudge for each signer.

[deal-desk-assistant](/PSA/AI-Cookbook-v2/skills/deal-desk-assistant/) — Builds an order form from the approved template as a draft and checks required fields.

[nudge-sender](/PSA/AI-Cookbook-v2/skills/nudge-sender/) — Sends approved reminders to pending remote signers on an existing envelope.

Source: /PSA/AI-Cookbook-v2/skills/renewal-brief/
