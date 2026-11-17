# Finance and revenue ops Renewal management

Confirm revenue documents are executed before close and flag unusual payment terms.

## What you can do

-   List agreements executed this quarter, with totals by type
-   Find payment terms longer than 45 days
-   List revenue documents still waiting on signers

## What waits for you

-   Change billing or invoicing
-   Restate revenue figures; always check the source

## Start with

[Signed this quarter](/PSA/AI-Cookbook-v2/prompts/finance-and-revenue-ops/#finance-and-revenue-ops-signed-this-quarter) · [quarter-close-audit](/PSA/AI-Cookbook-v2/skills/quarter-close-audit/) · [terms-outliers](/PSA/AI-Cookbook-v2/skills/terms-outliers/)

## Starter prompts

### Signed this quarter

StarterReads agreements

List agreements executed since \[quarter start date\] with counterparty, type, value if captured and effective date. Total by type. Mark any fields missing.

Tools: getAllAgreements · status COMPLETE

### Payment terms longer than 45 days

StarterReads agreements

Find agreements with payment terms of 60 days or more. Show counterparty, term, renewal date and status.

Tools: getAllAgreements · payment\_terms\_due\_date in (SIXTY\_DAYS, NINETY\_DAYS, OVER\_NINETY\_DAYS)

### Revenue documents waiting on signers

StarterReads envelopes

List envelopes tied to order forms, SOWs or amendments that are still waiting on any signer. Group by who is holding each one up.

Tools: getEnvelopes · waiting\_for\_others

Additional prompts (7)

### Signed value by customer

AdditionalAgreement insights: discovery

Total the contract value signed this quarter by counterparty. Show the working before the totals.

Tools: getAllAgreements

### Execution list

AdditionalAgreement insights: discovery

List agreements executed since \[DATE\] with effective date and value, if captured.

Tools: getAllAgreements

### Payment terms outliers

AdditionalAgreement insights: clauses and risk

Find agreements with payment terms of 60 days or more. Show counterparty, renewal date and status.

Tools: getAllAgreements

### Data gaps

AdditionalAgreement insights: clauses and risk

Which agreements have an annual value but no total value captured? Flag them for correction.

Tools: getAllAgreements

### Open workflow runs

AdditionalWorkflows: Maestro and CLM

List workflow runs that are still open, with the step each one is on.

Tools: getWorkflowInstancesList

### Revenue documents at risk

AdditionaleSign: envelopes, recipients and templates

List order forms and SOWs still waiting on any signer, grouped by who is holding them up.

Tools: getEnvelopes

### Signed copy retrieval

AdditionaleSign: envelopes, recipients and templates

Show the signed PDF for \[AGREEMENT NAME\] for the revenue file.

Tools: listEnvelopeDocuments

## Skills for this role

Install the core skill first, then add the team skills.

[docusign-agreements (core)](/PSA/AI-Cookbook-v2/skills/docusign-agreements/) · [quarter-close-audit](/PSA/AI-Cookbook-v2/skills/quarter-close-audit/) · [terms-outliers](/PSA/AI-Cookbook-v2/skills/terms-outliers/)

Source: /PSA/AI-Cookbook-v2/prompts/finance-and-revenue-ops/
