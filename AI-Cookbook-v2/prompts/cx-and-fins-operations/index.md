# CX and FINS operations CX FINS

Move account updates and account openings through without missing fields or stalled steps.

## What you can do

-   Show account-update envelopes stuck on a step
-   List account openings with missing fields or signers

## What waits for you

-   Contact customers
-   Change customer data in your systems

## Start with

[Account-update envelopes stuck](/PSA/AI-Cookbook-v2/prompts/cx-and-fins-operations/#cx-and-fins-operations-account-update-envelopes-stuck) · [account-update-tracker](/PSA/AI-Cookbook-v2/skills/account-update-tracker/)

## Starter prompts

### Account-update envelopes stuck

StarterReads envelopes

List account-update envelopes sent in the last 30 days that are still waiting on a customer or staff signer. Group by step and days outstanding. Highlight anything over 5 days.

Tools: getEnvelopes · search\_text 'account'

### Account-opening packets with missing fields

StarterReads agreements

For account-opening agreements sent this month, list any with blank required fields or missing signers. Show counts by status. Do not contact customers.

Tools: getAllAgreements · getAgreementDetails

Additional prompts (7)

### Account documents

AdditionalAgreement insights: discovery

Show the agreements on file for \[CUSTOMER\] and their status.

Tools: getAllAgreements

### Data completeness

AdditionalAgreement insights: discovery

Which account-opening agreements have no expiration date recorded?

Tools: getAllAgreements

### Custom terms check

AdditionalAgreement insights: clauses and risk

Summarize custom provisions in our account-opening agreements against the standard set. Flag differences.

Tools: getAgreementDetails

### Workflow inventory

AdditionalWorkflows: Maestro and CLM

List the Maestro workflows for account updates and the inputs each one needs.

Tools: getWorkflowsList · getWorkflowTriggerRequirements

### Run status

AdditionalWorkflows: Maestro and CLM

Show the running account-update workflow instances and the step each one is on.

Tools: getWorkflowInstancesList

### Stuck account updates

AdditionaleSign: envelopes, recipients and templates

Show account-update envelopes waiting on a signer for more than 5 days, with the recipient for each.

Tools: getEnvelopes · listRecipients

### Reminder · writes

AdditionaleSign: envelopes, recipients and templates

Send a reminder to the recipient on \[ENVELOPE NAME\] and tell me when it expires. Confirm with me before you send, remind, trigger or change anything.

Tools: sendReminder

## Skills for this role

Install the core skill first, then add the team skills.

[docusign-agreements (core)](/PSA/AI-Cookbook-v2/skills/docusign-agreements/) · [account-update-tracker](/PSA/AI-Cookbook-v2/skills/account-update-tracker/)

Source: /PSA/AI-Cookbook-v2/prompts/cx-and-fins-operations/
