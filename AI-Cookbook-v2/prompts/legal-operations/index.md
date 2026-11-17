# Legal operations Unified Legal

Find the terms, deadlines and non-standard clauses that matter, quickly and with the source cited.

## What you can do

-   Find agreements by governing law, term or custom provision
-   Build a 120-day expiry digest with owners
-   Summarize non-standard provisions against standard terms
-   Start a CLM intake after you approve the inputs

## What waits for you

-   Give legal advice or approve exceptions
-   Start a CLM workflow without your yes

## Start with

[Governing law check](/PSA/AI-Cookbook-v2/prompts/legal-operations/#legal-operations-governing-law-check) · [provision-sweep](/PSA/AI-Cookbook-v2/skills/provision-sweep/) · [expiry-digest](/PSA/AI-Cookbook-v2/skills/expiry-digest/)

## Starter prompts

### Governing law check

StarterReads agreements

Find agreements governed by \[State/Country\]. Then summarize the rest by governing law. The filter cannot say 'not equal', so exclude matches in the summary. Say clearly if results are partial.

Tools: getAgreementFilterSkill · getAllAgreements

### Expiring contracts digest (120 days)

StarterReads agreements

List agreements expiring between today and 120 days from now. Include counterparty, type, renewal type, notice date if captured, and owner. Group by month. End with the top 3 I should look at first and why.

Tools: getAllAgreements · provisions/expiration\_date

### Start a CLM workflow for an intake

StarterRuns workflow on approval

List the CLM workflows I can start. For a mutual NDA with \[counterparty\], show the inputs the workflow needs and ask me for missing ones. Confirm with me before you send, remind, trigger or change anything.

Tools: getClmWorkflowDefinitions · startClmWorkflow

### Non-standard provisions

StarterReads agreements

For \[customer or vendor\], summarize custom provisions captured in Agreement Manager and compare them with standard terms (term, termination, liability, governing law). Flag differences. Do not give legal advice.

Tools: getAllAgreements · getAgreementDetails

Additional prompts (8)

### Governing law search

AdditionalAgreement insights: discovery

Find agreements where governing law is \[STATE\]. Show counterparty and expiry date.

Tools: getAgreementFilterSkill · getAllAgreements

### Expiry watch

AdditionalAgreement insights: discovery

List agreements expiring in the next 120 days with owner and renewal type.

Tools: getAllAgreements

### Clause search

AdditionalAgreement insights: clauses and risk

Find every agreement with a custom provision named \[CLAUSE NAME\]. Show the wording and the agreement it sits in.

Tools: getAllAgreements · getAgreementDetails

### Liability exposure

AdditionalAgreement insights: clauses and risk

Which agreements have a liability cap below \[AMOUNT\], or no cap recorded?

Tools: getAllAgreements

### CLM workflow inventory

AdditionalWorkflows: Maestro and CLM

List the CLM workflows I can start and the inputs each one needs.

Tools: getClmWorkflowDefinitions

### CLM intake · writes

AdditionalWorkflows: Maestro and CLM

Start a CLM intake for a mutual NDA with \[COUNTERPARTY\]. Ask me for any missing input first. Confirm with me before you send, remind, trigger or change anything.

Tools: startClmWorkflow

### Template discovery

AdditionaleSign: envelopes, recipients and templates

Show the NDA templates and the fields each one requires.

Tools: getTemplates

### Signer status

AdditionaleSign: envelopes, recipients and templates

For \[AGREEMENT NAME\], list each recipient and their signing status.

Tools: getEnvelopes · listRecipients

## Skills for this role

Install the core skill first, then add the team skills.

[docusign-agreements (core)](/PSA/AI-Cookbook-v2/skills/docusign-agreements/) · [contract-intake](/PSA/AI-Cookbook-v2/skills/contract-intake/) · [provision-sweep](/PSA/AI-Cookbook-v2/skills/provision-sweep/) · [expiry-digest](/PSA/AI-Cookbook-v2/skills/expiry-digest/)

Source: /PSA/AI-Cookbook-v2/prompts/legal-operations/
