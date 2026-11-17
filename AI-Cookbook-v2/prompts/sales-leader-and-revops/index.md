# Sales leader and RevOps B2B Sales

See which deals are signed, stalled or waiting on the customer, without building a report by hand.

## What you can do

-   Count signed agreements and envelopes by period
-   List stalled signatures by owner
-   Summarize what changed this week

## What waits for you

-   Change deal records or forecasts
-   Chase signers directly

## Start with

[Weekly close report](/PSA/AI-Cookbook-v2/prompts/account-executive/#account-executive-weekly-close-report) · [quarter-close-audit](/PSA/AI-Cookbook-v2/skills/quarter-close-audit/) · [signature-chaser](/PSA/AI-Cookbook-v2/skills/signature-chaser/)

## Starter prompts

No starter prompts for this role. See the additional prompts below.

Additional prompts (8)

### Monthly execution trend

AdditionalAgreement insights: discovery

How many agreements did we execute each month this year? Show the monthly count and total.

Tools: getAllAgreements

### High-value signings

AdditionalAgreement insights: discovery

Which agreements signed last quarter have a total value over \[AMOUNT\]? List counterparty and date.

Tools: getAllAgreements

### Compliance gap report

AdditionalAgreement insights: clauses and risk

Which of my customers are missing a DPA or AI addendum? Order by annual value.

Tools: getAllAgreements

### Renewal exceptions

AdditionalAgreement insights: clauses and risk

Which renewals in the next 120 days have a non-standard renewal type? List them with the agreement name.

Tools: getAllAgreements

### In-flight workflow status

AdditionalWorkflows: Maestro and CLM

Show the renewal workflow runs started this month: which step each is on, who is acting, and what is blocked.

Tools: getWorkflowInstancesList

### Workflow usage check

AdditionalWorkflows: Maestro and CLM

Which workflows have not been started in the last 30 days?

Tools: getWorkflowsList · getWorkflowInstancesList

### Stalled signatures by owner

AdditionaleSign: envelopes, recipients and templates

Which envelopes have been waiting on a signer for more than 7 days? Group them by owner.

Tools: getEnvelopes

### Drafts that never left the desk

AdditionaleSign: envelopes, recipients and templates

List envelopes created as drafts this week that have not been sent.

Tools: getEnvelopes

## Skills for this role

Install the core skill first, then add the team skills.

[docusign-agreements (core)](/PSA/AI-Cookbook-v2/skills/docusign-agreements/) · [signature-chaser](/PSA/AI-Cookbook-v2/skills/signature-chaser/) · [deal-desk-assistant](/PSA/AI-Cookbook-v2/skills/deal-desk-assistant/) · [renewal-brief](/PSA/AI-Cookbook-v2/skills/renewal-brief/) · [nudge-sender](/PSA/AI-Cookbook-v2/skills/nudge-sender/)

Source: /PSA/AI-Cookbook-v2/prompts/sales-leader-and-revops/
