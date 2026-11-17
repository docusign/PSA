# HR operations HR

Get new-hire paperwork and policy sign-offs moving without chasing people one by one.

## What you can do

-   Show each onboarding packet, who is holding it and how long
-   List policy acknowledgements still unsigned
-   Draft offer letters as drafts
-   Start the onboarding workflow after you confirm inputs

## What waits for you

-   Trigger a workflow or send an offer without your yes
-   Make hiring or pay decisions

## Start with

[Onboarding status board](/PSA/AI-Cookbook-v2/prompts/hr-operations/#hr-operations-onboarding-status-board) · [onboarding-orchestrator](/PSA/AI-Cookbook-v2/skills/onboarding-orchestrator/) · [policy-ack-tracker](/PSA/AI-Cookbook-v2/skills/policy-ack-tracker/)

## Starter prompts

### Onboarding status board

StarterReads envelopes

Show every onboarding packet sent in the last 14 days. For each new hire, list who still needs to sign, which step they are on, and days outstanding. Highlight anything over 5 days.

Tools: getEnvelopes · waiting\_for\_others

### Offer letter draft from template

StarterCreates draft on approval

List my offer letter templates and their required fields. Prepare a draft envelope for \[candidate, email, role, start date\] saved as created, not sent, and show it to me. Confirm with me before you send, remind, trigger or change anything.

Tools: getTemplates · createEnvelope (status created)

### Start the onboarding workflow

StarterRuns workflow on approval

List the Maestro workflows available to me. Show the inputs the onboarding workflow needs for \[employee name\]. Confirm the inputs with me, then wait for my yes before triggering it. Confirm with me before you send, remind, trigger or change anything.

Tools: getWorkflowsList · getWorkflowTriggerRequirements · triggerWorkflow

### Policy acknowledgements not yet signed

StarterReads envelopes

Which employees have not yet signed the \[policy name\] acknowledgement sent on or after \[date\]? Group by status and give a reminder-ready list. Do not send reminders.

Tools: getEnvelopes · search\_text

Additional prompts (9)

### Onboarding paperwork status

AdditionalAgreement insights: discovery

Show the onboarding agreements sent this month and their status.

Tools: getAllAgreements

### Document checklist

AdditionalAgreement insights: discovery

Summarize which onboarding documents are in use for a \[ROLE\] hire and which are missing.

Tools: getAllAgreements

### Clause inventory

AdditionalAgreement insights: clauses and risk

Which employment agreements have a custom non-compete or notice clause? Quote each clause and name the agreement.

Tools: getAllAgreements · getAgreementDetails

### Missing signed offers

AdditionalAgreement insights: clauses and risk

Which offer letters have a start date that has passed without a signed copy on file?

Tools: getAllAgreements

### Workflow inventory

AdditionalWorkflows: Maestro and CLM

List the onboarding workflows available and the inputs each one needs.

Tools: getWorkflowsList · getWorkflowTriggerRequirements

### Run status

AdditionalWorkflows: Maestro and CLM

Show the onboarding workflow runs for \[NEW HIRE\] and the step they are on.

Tools: getWorkflowInstancesList

### Onboarding status board

AdditionaleSign: envelopes, recipients and templates

Show onboarding envelopes sent in the last 14 days: who still needs to sign and how many days each has been out.

Tools: getEnvelopes · listRecipients

### Offer draft · writes

AdditionaleSign: envelopes, recipients and templates

Create an offer letter draft for \[CANDIDATE, EMAIL, ROLE, START DATE\] from the offer template, saved as a draft and not sent. Confirm with me before you send, remind, trigger or change anything.

Tools: getTemplates · createEnvelope

### Recipient change · writes

AdditionaleSign: envelopes, recipients and templates

Change the recipient on the \[ENVELOPE NAME\] envelope from \[OLD EMAIL\] to \[NEW EMAIL\]. Confirm with me before you send, remind, trigger or change anything.

Tools: updateEnvelopeRecipients

## Skills for this role

Install the core skill first, then add the team skills.

[docusign-agreements (core)](/PSA/AI-Cookbook-v2/skills/docusign-agreements/) · [onboarding-orchestrator](/PSA/AI-Cookbook-v2/skills/onboarding-orchestrator/) · [offer-letter-sender](/PSA/AI-Cookbook-v2/skills/offer-letter-sender/) · [policy-ack-tracker](/PSA/AI-Cookbook-v2/skills/policy-ack-tracker/)

Source: /PSA/AI-Cookbook-v2/prompts/hr-operations/
