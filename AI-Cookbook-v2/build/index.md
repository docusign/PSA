# Build agents

Choose where the agent should live. Both use the same agreement data, and both keep a human approval step.

Option A

### Build agents in Docusign

Best for admins and operations teams who want repeatable workflows that run inside Docusign on approved templates.

1.  Confirm your IAM subscription covers Maestro workflows.
2.  Upload agreements to Agreement Manager and wait for extraction.
3.  Build or import a workflow, set the Agreement Desk routing email, then Save, Review and Publish.
4.  Set the start method to From an API call so an assistant can start it.
5.  Test the trigger inputs before any real send.

**Ready assets:** renewal workflow import and document template from the sample agreement pack. Approval happens in the workflow's review steps.

Option B

### Build agents in the AI tool you use, with Docusign MCP

Best for teams already in Claude, ChatGPT, Copilot Studio or Gemini who want one agent that reads Docusign and works with calendar, mail or CRM too.

1.  Your admin enables MCP access for the account.
2.  Add the official connector (production), or a custom connector with your IK for demo.
3.  Install the core docusign-agreements skill.
4.  Add team skills, and paste the platform setup where the tool needs instructions.
5.  Run the connector test on the Connect page and confirm the tool call appears in the activity view.
6.  Publish to your team's channel once the write approvals behave as expected.

**Ready assets:** core skill, team skills, platform setup and the prompts by role.

|  | Build in Docusign | Build in your AI tool with MCP |
| --- | --- | --- |
| **Who builds** | Docusign admins and operations | Makers, AEs and ops leads in their own AI tool |
| **Where it runs** | Inside Docusign, on published workflows | In your AI tool, reading Docusign data |
| **Approval model** | Workflow review and routing steps | Instructions and approval gates you write |
| **Needs** | IAM subscription for Maestro workflows | Connector access and that tool's plan |
| **Good first build** | Renewal workflow | Renewal brief and signature chaser |

## Blueprints

Partner / Legal

### Renewal Desk

Weekly schedule. Filters agreements by expiry and renewal type, posts a digest.

Legal

### Contract Request Intake

A request arrives; the agent lists CLM workflows and starts the right one after approval.

HR, Copilot Studio

### HR Onboarding Agent

Chat request triggers a Maestro onboarding workflow after trigger requirements are confirmed; reports packet status.

Procurement

### Vendor Check Agent

Answers 'do we have an NDA and when does it expire' before a new one is drafted.

Sales leader and RevOps

### Stalled Deal Monitor

Daily scheduled job lists envelopes waiting 3+ days; drafts nudges for approval.

IT & Admin

### Account Audit Agent (read-only)

Starter agent: audits an account's templates, workflows and MCP settings. Reads only.

[Platform setup and prerequisites →](/PSA/AI-Cookbook-v2/build/platforms/)

Source: /PSA/AI-Cookbook-v2/build/
