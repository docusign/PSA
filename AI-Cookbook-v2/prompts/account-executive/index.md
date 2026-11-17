# Account executive B2B Sales

Know where a customer's agreement stands before the next call, and get order forms out without rework.

## What you can do

-   Look up agreement terms, expiry and renewal type
-   See who is holding up an envelope
-   Draft order forms and reminders as drafts

## What waits for you

-   Send, remind, void or trigger anything without your yes
-   See agreements your Docusign user cannot see

## Start with

[Renewal prep for an account](/PSA/AI-Cookbook-v2/prompts/account-executive/#account-executive-renewal-prep-for-an-account) · [renewal-brief](/PSA/AI-Cookbook-v2/skills/renewal-brief/) · [signature-chaser](/PSA/AI-Cookbook-v2/skills/signature-chaser/)

## Starter prompts

### Chase stalled signatures

StarterReads envelopes

List envelopes I sent in the last 60 days that are still waiting on others. Show recipient, sent date and days waiting. Highlight anything waiting 3+ days, oldest first. Draft a short, friendly nudge for each. Do not send reminders. Confirm with me before you send, remind, trigger or change anything.

Tools: getEnvelopes · waiting\_for\_others

### Order form draft from template

StarterCreates draft on approval

Find my templates matching 'order form'. Show the required fields for the best match and ask me for anything missing. Then create a draft envelope for \[customer, signer name, email\] saved as created, not sent, and summarize it. Confirm with me before you send, remind, trigger or change anything.

Tools: getTemplates · createEnvelope (status created)

### Renewal prep for an account

StarterReads agreements

Find every agreement with \[customer\]. For each, give type, status, expiration date, renewal type and governing law. Flag anything expiring in the next 120 days. If a value is missing, say so. Do not guess.

Tools: getEnvelopeVsAgreementSkill · getAllAgreements · getAgreementDetails

### Weekly close report

StarterReads envelopes

Which envelopes did I send that completed this week? Give a count, the list with recipients, and days from sent to completed where dates are available.

Tools: getEnvelopes · Completed

Additional prompts (8)

### Renewal pipeline

AdditionalAgreement insights: discovery

Show me all upcoming renewals for my accounts in the next 90 days.

Tools: getAllAgreements

### Account renewal view

AdditionalAgreement insights: discovery

What is renewing for \[CUSTOMER\] in the next 6 months? Show type, renewal date and notice period.

Tools: getAllAgreements

### Cross-account clause check

AdditionalAgreement insights: clauses and risk

\[CUSTOMER\] wants \[N\] seats at \[X\]% off. Does that conflict with any clause in our other customer agreements?

Tools: getAllAgreements · getAgreementDetails

### Custom terms review

AdditionalAgreement insights: clauses and risk

For \[CUSTOMER\], compare custom provisions with our standard terms and flag the differences. Do not give legal advice.

Tools: getAgreementDetails

### Confirm the workflow before any template fallback

AdditionalWorkflows: Maestro and CLM

List the Maestro workflows I can use for renewals and the inputs each one needs.

Tools: getWorkflowsList · getWorkflowTriggerRequirements

### Renewal trigger · writes

AdditionalWorkflows: Maestro and CLM

Start the renewal workflow for \[CUSTOMER\]: \[N\] seats, \[X\]% off, 1-year term, sent to \[EMAIL\]. Ask me for any missing input first. Confirm with me before you send, remind, trigger or change anything.

Tools: getWorkflowTriggerRequirements · triggerWorkflow

### Signing status by recipient

AdditionaleSign: envelopes, recipients and templates

Show the envelopes sent to \[CUSTOMER\] that are still open, and who has not signed yet.

Tools: getEnvelopes · listRecipients

### Draft from template · writes

AdditionaleSign: envelopes, recipients and templates

Create a draft order form for \[CUSTOMER\] from the \[TEMPLATE NAME\] template, saved as a draft and not sent. Show me the fields first. Confirm with me before you send, remind, trigger or change anything.

Tools: getTemplates · createEnvelope

## Skills for this role

Install the core skill first, then add the team skills.

[docusign-agreements (core)](/PSA/AI-Cookbook-v2/skills/docusign-agreements/) · [signature-chaser](/PSA/AI-Cookbook-v2/skills/signature-chaser/) · [deal-desk-assistant](/PSA/AI-Cookbook-v2/skills/deal-desk-assistant/) · [renewal-brief](/PSA/AI-Cookbook-v2/skills/renewal-brief/) · [nudge-sender](/PSA/AI-Cookbook-v2/skills/nudge-sender/)

Source: /PSA/AI-Cookbook-v2/prompts/account-executive/
