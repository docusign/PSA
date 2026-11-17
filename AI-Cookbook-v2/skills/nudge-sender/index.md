NS

# nudge-sender

SalesSkillWrites need approval

Sends approved reminders to pending remote signers on an existing envelope.

### Why it is needed

Reminders are the cheapest way to speed a deal. Sending them by hand is slow and easy to forget.

### Needs

-   Your approval for every write.

## Steps

1.  List pending signers with listRecipients. Skip embedded signers.
2.  Show recipients, subject and the expiry date.
3.  Wait for an explicit yes.
4.  Call sendReminder on the existing envelope. Never create a new one.

## Tools it calls

-   `getEnvelopes` · Signing status, folders such as waiting\_for\_others, completed and voided
-   `listRecipients` · Who still has to act on an envelope
-   `sendReminder` · Reminder to pending remote signers

SKILL.md

**nudge-sender/SKILL.md**

\---
name: nudge-sender
description: Sends approved reminders to pending remote signers on an existing envelope. Use with the Docusign connector.
---
# nudge-sender

Why: Reminders are the cheapest way to speed a deal. Sending them by hand is slow and easy to forget.

Follows the docusign-agreements rules: read first, save drafts as created, approve before any write.

## Tools
- getEnvelopes
- listRecipients
- sendReminder

## Steps
1. List pending signers with listRecipients. Skip embedded signers.
2. Show recipients, subject and the expiry date.
3. Wait for an explicit yes.
4. Call sendReminder on the existing envelope. Never create a new one.

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

[renewal-brief](/PSA/AI-Cookbook-v2/skills/renewal-brief/) — One-page account brief: terms, expiry, auto-renewal and governing law.

Source: /PSA/AI-Cookbook-v2/skills/nudge-sender/
