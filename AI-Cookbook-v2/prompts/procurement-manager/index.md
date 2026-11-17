# Procurement manager Procurement

Know which vendor NDAs and contracts exist, when they renew, and how the terms compare.

## What you can do

-   Check for an existing NDA before a new one is drafted
-   List auto-renewals and open notice windows
-   Compare payment, termination and governing law across vendors

## What waits for you

-   Send an NDA without approval
-   Give a legal view on a clause

## Start with

[Do we already have an NDA?](/PSA/AI-Cookbook-v2/prompts/procurement-manager/#procurement-manager-do-we-already-have-an-nda-with-vendor) · [vendor-nda-gate](/PSA/AI-Cookbook-v2/skills/vendor-nda-gate/) · [renewal-radar](/PSA/AI-Cookbook-v2/skills/renewal-radar/)

## Starter prompts

### Do we already have an NDA with \[vendor\]?

StarterReads agreements

Show any NDA with \[vendor\]: type, status, effective and expiration dates, and governing law. If none exists, say so and stop. Do not create one.

Tools: getEnvelopeVsAgreementSkill · getAllAgreements

### Auto-renewals in the next 90 days

StarterReads agreements

List agreements that auto-renew in the next 90 days. Show counterparty, renewal notice date and flag any where the notice window has already opened. Sort by notice date.

Tools: getAgreementFilterSkill · getAllAgreements

### Vendor NDA draft from approved template

StarterCreates draft on approval

Show the approved mutual NDA template and its required fields. Create a draft envelope for \[vendor, contact, email\] saved as created, not sent, and show me the summary first. Confirm with me before you send, remind, trigger or change anything.

Tools: getTemplates · createEnvelope (status created)

### Compare vendor terms

StarterReads agreements

Compare payment terms, governing law and termination provisions across our agreements with \[vendor A\], \[vendor B\] and \[vendor C\] in a table. Mark any field you could not find.

Tools: getAllAgreements · getAgreementDetails

Additional prompts (8)

### Existing NDA check

AdditionalAgreement insights: discovery

Do we already have an NDA with \[VENDOR\]? Show type, status, effective and expiry dates, and governing law.

Tools: getEnvelopeVsAgreementSkill · getAllAgreements

### Vendor footprint

AdditionalAgreement insights: discovery

List all agreements with \[VENDOR\] grouped by type, with expiry dates.

Tools: getAllAgreements

### Renewal and price risk

AdditionalAgreement insights: clauses and risk

Scan our vendor MSAs for auto-renewal terms and price-increase caps. List each vendor with its cap.

Tools: getAllAgreements · getAgreementDetails

### Vendor terms comparison

AdditionalAgreement insights: clauses and risk

Compare payment terms, termination and liability cap across \[VENDOR A\], \[VENDOR B\] and \[VENDOR C\]. Mark any field not found.

Tools: getAgreementDetails

### Workflow inventory

AdditionalWorkflows: Maestro and CLM

Which Maestro workflows handle vendor onboarding, and what inputs does each need?

Tools: getWorkflowsList · getWorkflowTriggerRequirements

### Onboarding trigger · writes

AdditionalWorkflows: Maestro and CLM

Start the vendor onboarding workflow for \[VENDOR\] with the inputs I confirm. Confirm with me before you send, remind, trigger or change anything.

Tools: getWorkflowTriggerRequirements · triggerWorkflow

### Template discovery

AdditionaleSign: envelopes, recipients and templates

Show our vendor NDA templates and the fields each one needs.

Tools: getTemplates

### Draft NDA · writes

AdditionaleSign: envelopes, recipients and templates

Create a mutual NDA draft for \[VENDOR CONTACT, EMAIL\] from the approved template, saved as a draft and not sent. Confirm with me before you send, remind, trigger or change anything.

Tools: getTemplates · createEnvelope

## Skills for this role

Install the core skill first, then add the team skills.

[docusign-agreements (core)](/PSA/AI-Cookbook-v2/skills/docusign-agreements/) · [vendor-nda-gate](/PSA/AI-Cookbook-v2/skills/vendor-nda-gate/) · [renewal-radar](/PSA/AI-Cookbook-v2/skills/renewal-radar/) · [term-comparator](/PSA/AI-Cookbook-v2/skills/term-comparator/)

Source: /PSA/AI-Cookbook-v2/prompts/procurement-manager/
