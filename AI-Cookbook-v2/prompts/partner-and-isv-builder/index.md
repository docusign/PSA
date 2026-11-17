# Partner and ISV builder Partner onboarding

Ship an agent to your own customers, with each customer's admin in control.

## What you can do

-   Build with your allowlisted Integration Key
-   Reuse the core skill and team skills across customers
-   Use the platform setup for each tool

## What waits for you

-   Skip customer admin enablement
-   Run production without IK allowlisting

## Start with

[Build agents in the AI tool you use](/PSA/AI-Cookbook-v2/build/) · [Platform setup](/PSA/AI-Cookbook-v2/build/)

## Starter prompts

No starter prompts for this role. See the additional prompts below.

Additional prompts (6)

### Scope a partner build

AdditionalAgreement insights: discovery

Which Docusign MCP tools work on production accounts, and which need a developer or demo account? Cite the docs.

Tools: searchDocusignDocs

### Scope check

AdditionalAgreement insights: discovery

Which scopes are needed to read agreement terms and to create envelopes? Cite the docs.

Tools: searchDocusignDocs

### Design review

AdditionalAgreement insights: clauses and risk

Suggest best practices for an agent that reads agreement terms and flags clauses for legal review.

Tools: suggestBestPractices

### Trigger design

AdditionalWorkflows: Maestro and CLM

What trigger requirements would a partner app need to expose before a Maestro workflow can be started?

Tools: getWorkflowTriggerRequirements

### Allowlist request prep

AdditionaleSign: envelopes, recipients and templates

Draft the summary for an Integration Key allowlist request for \[PARTNER\], listing tools and scopes. Do not submit it.

Tools: searchDocusignDocs

### Operations design

AdditionaleSign: envelopes, recipients and templates

Suggest token refresh and approval-gate practices for an agent that runs unattended jobs.

Tools: suggestBestPractices

## Skills for this role

Install the core skill first, then add the team skills.

[docusign-agreements (core)](/PSA/AI-Cookbook-v2/skills/docusign-agreements/)

Source: /PSA/AI-Cookbook-v2/prompts/partner-and-isv-builder/
