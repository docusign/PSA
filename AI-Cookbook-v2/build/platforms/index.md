# Platform setup

Only what each platform needs on top of the core skill.

Claude · Skills, scheduled tasks, custom connector for demo

Upload the zipped docusign-agreements folder under Skills. Add a scheduled task for weekly jobs (for example, Monday 9am: run signature-chaser and post the list). Demo accounts need a custom connector with your Integration Key. Official connector points to production.

Claude-only: Skills upload and scheduled tasks.

ChatGPT · Project or GPT instructions

Enable the Docusign app. Paste the body of docusign-agreements (without the front matter) into the Project instructions.

Starter prompts: Which of my envelopes are waiting on a signer? · Do we have an NDA with \[vendor\]? · What expires in the next 120 days?

Microsoft Copilot Studio · Agent description, instructions, generative orchestration

Name: Sales Agent. Description: Sales agent that uses the Docusign MCP connector to act on agreements, envelopes, templates and workflows for Account Executives managing renewals and contract workflows.

Turn on Generative orchestration (Settings → Generative AI). Add the Docusign MCP connector under Tools → Model Context Protocol. Demo connector is for demo accounts only.

Test with the activity map on. Every answer should show a tools/call. Publish, then add the Microsoft 365 and Teams channel.

Platform-only: agent instructions, orchestration toggle, activity-map check, Teams channel.

Gemini Enterprise · Agent instructions

Connect the Docusign connector to the agent. Paste the body of docusign-agreements into the agent instructions.

Add: 'Use calendar or mail context only to identify the counterparty. Read agreement data only from Docusign.'

Platform-only: agent instruction add-on for mail and calendar context.

Perplexity and Slackbot · Saved instructions

Use the official connector. Save this as a saved prompt or channel instruction:

Use the Docusign connector. Read-only questions run directly. Ask me to confirm before sending, reminding, voiding or triggering anything. Drafts must be saved as created, not sent. If a value is missing or results are partial, say so. Lead with the answer, then a short table.

Platform-only: compact saved instruction (these surfaces take no skill folder).

## Who builds what

### Customers: in-house builders

**Build agents for your own company in Copilot Studio, Claude or your own code.**

Start with the official connector in your AI platform. Custom agents use your own allowlisted IK and your own approval step.

### Partners and ISVs

**Build agents for your customers: leasing, renewal desks, vertical apps.**

Your agent uses your allowlisted IK. Each customer signs in with their own account and their admin enables MCP, so one agent serves many customers.

### No-code power users

**Ops leads in legal, sales, procurement, HR and FINS.**

Official connector in Claude, a skill and a scheduled task. No IK needed.

## Prerequisites

| You need | Customers | Partners / ISVs | Why |
| --- | --- | --- | --- |
| **Docusign account (developer account for demo)** | Production account | Developer account, then production | Demo endpoint uses test data |
| **Integration Key with secret and redirect URIs** | Only for custom agents | Yes | Identifies your app |
| **IK allowlist request for production** | Custom agents only | Yes, before go-live | Required for your own agent or platform (reported) |
| **Admin enables MCP (Admin → Integrations → MCP Connections)** | Yes | Each customer admin | Server-side kill switch |
| **IAM or CLM entitlements** | For Maestro and CLM tools | Per customer plan | Tools depend on plan |
| **Approval step** | Build it for jobs and custom agents | Build it | Chat assistants prompt automatically |
| **Token strategy (OAuth or JWT)** | Refresh logic for unattended jobs | Per-customer sign-in | JWT tokens last 8 hours (reported) |

Source: /PSA/AI-Cookbook-v2/build/platforms/
