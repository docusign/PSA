# Skills

A skill is a SKILL.md file: what it does, what it reads and writes, what it needs, and the steps it follows. Install the core skill first. Team skills build on it.

## 1 · Install the core skill

### [docusign-agreements](/PSA/AI-Cookbook-v2/skills/docusign-agreements/)

Core · all teamsClaudeChatGPTCopilot StudioGemini

[Open and copy →](/PSA/AI-Cookbook-v2/skills/docusign-agreements/)

**What it does:** sets the read-first, approve-before-write rules, the tool order and the output format. **Why it is needed:** without it, assistants guess dates, mix up envelope and agreement data, and can send without asking.

## 2 · Team skills (18)

How skills and automations work

**Team skills** are skills grouped by the team that uses them: Sales, Procurement, HR, Legal, Finance & RevOps, CX FINS and IT & Admin. Each one is a SKILL.md you add alongside the core skill.

**Skill or automation?** A **skill** runs when you ask for it in chat. An **automation** runs on a schedule with nobody asking, so it needs a scheduler (Claude scheduled tasks are confirmed). Both follow the same rules, and any write still waits for your approval.

| Skill | Team | Type | What it does |
| --- | --- | --- | --- |
| [**signature-chaser**](/PSA/AI-Cookbook-v2/skills/signature-chaser/) | Sales | Skill | Lists envelopes waiting 3+ days and drafts a nudge for each signer.  
Reads: Envelope status, Recipients · Writes: nothing |
| [**deal-desk-assistant**](/PSA/AI-Cookbook-v2/skills/deal-desk-assistant/) | Sales | Skill | Builds an order form from the approved template as a draft and checks required fields.  
Reads: Templates · Writes: Drafts (saved as created) |
| [**renewal-brief**](/PSA/AI-Cookbook-v2/skills/renewal-brief/) | Sales | Skill | One-page account brief: terms, expiry, auto-renewal and governing law.  
Reads: Agreement terms, Agreement details · Writes: nothing |
| [**nudge-sender**](/PSA/AI-Cookbook-v2/skills/nudge-sender/) | Sales | Skill | Sends approved reminders to pending remote signers on an existing envelope.  
Reads: Envelope status, Recipients · Writes: Reminders (after approval) |
| [**vendor-nda-gate**](/PSA/AI-Cookbook-v2/skills/vendor-nda-gate/) | Procurement | Skill | Checks for an existing NDA before drafting a new one.  
Reads: Agreement terms, Templates · Writes: Drafts (saved as created) |
| [**renewal-radar**](/PSA/AI-Cookbook-v2/skills/renewal-radar/) | Procurement | Automation | Lists auto-renewals due in 90 days with open notice windows. Runs weekly as a scheduled task.  
Reads: Agreement terms · Writes: nothing |
| [**term-comparator**](/PSA/AI-Cookbook-v2/skills/term-comparator/) | Procurement | Skill | Compares payment, termination, liability and governing law across vendors in one table.  
Reads: Agreement terms, Agreement details · Writes: nothing |
| [**onboarding-orchestrator**](/PSA/AI-Cookbook-v2/skills/onboarding-orchestrator/) | HR | Skill | Finds the onboarding Maestro workflow, confirms inputs and triggers it after approval. Then tracks packet status.  
Reads: Maestro workflows, Workflow inputs, Envelope status · Writes: Maestro start (after approval) |
| [**offer-letter-sender**](/PSA/AI-Cookbook-v2/skills/offer-letter-sender/) | HR | Skill | Drafts an offer letter from the role template for review before anything is sent.  
Reads: Templates · Writes: Drafts (saved as created) |
| [**policy-ack-tracker**](/PSA/AI-Cookbook-v2/skills/policy-ack-tracker/) | HR | Automation | Finds policy acknowledgements still unsigned and groups them for a reminder list.  
Reads: Envelope status, Recipients · Writes: nothing |
| [**contract-intake**](/PSA/AI-Cookbook-v2/skills/contract-intake/) | Legal | Skill | Turns a contract request into the right CLM workflow with the required inputs.  
Reads: CLM workflows, Agreement terms · Writes: CLM start (after approval) |
| [**provision-sweep**](/PSA/AI-Cookbook-v2/skills/provision-sweep/) | Legal | Skill | Finds agreements by governing law, term or custom provision and flags partial results.  
Reads: Agreement terms · Writes: nothing |
| [**expiry-digest**](/PSA/AI-Cookbook-v2/skills/expiry-digest/) | Legal | Automation | Monthly digest of agreements expiring in the next 120 days, grouped by month, with the top three to review.  
Reads: Agreement terms · Writes: nothing |
| [**quarter-close-audit**](/PSA/AI-Cookbook-v2/skills/quarter-close-audit/) | Finance & RevOps | Skill | Checks that revenue documents are executed before quarter end and reports the gaps.  
Reads: Envelope status, Agreement terms · Writes: nothing |
| [**terms-outliers**](/PSA/AI-Cookbook-v2/skills/terms-outliers/) | Finance & RevOps | Skill | Flags agreements with payment terms longer than 45 days.  
Reads: Agreement terms · Writes: nothing |
| [**account-update-tracker**](/PSA/AI-Cookbook-v2/skills/account-update-tracker/) | CX FINS | Skill | Tracks account-update envelopes waiting on customer or staff signers, by step.  
Reads: Envelope status · Writes: nothing |
| [**mcp-access-audit**](/PSA/AI-Cookbook-v2/skills/mcp-access-audit/) | IT & Admin | Skill | Reviews connector set-up before rollout: account, brands, users and approval gates.  
Reads: Account settings, Brands, Users · Writes: nothing |
| [**envelope-health**](/PSA/AI-Cookbook-v2/skills/envelope-health/) | IT & Admin | Automation | Daily view of voided, declined and timed-out envelopes with likely causes.  
Reads: Envelope status · Writes: nothing |

Source: /PSA/AI-Cookbook-v2/skills/
