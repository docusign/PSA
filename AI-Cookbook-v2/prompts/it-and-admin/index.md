# IT and admin Set-up

Roll out MCP access safely, and spot failed or timed-out envelopes early.

## What you can do

-   Check the connector set-up for the account
-   Review brands and users
-   Report failed, declined and timed-out envelopes daily

## What waits for you

-   Change tenant or MCP settings from the assistant
-   Grant access to people outside your policy

## Start with

[mcp-access-audit](/PSA/AI-Cookbook-v2/skills/mcp-access-audit/) · [envelope-health](/PSA/AI-Cookbook-v2/skills/envelope-health/)

## Starter prompts

No starter prompts for this role. See the additional prompts below.

Additional prompts (6)

### Account set-up

AdditionalAgreement insights: discovery

Show the account name and the brands configured on it.

Tools: getAccount · getBrands

### User review

AdditionalAgreement insights: discovery

List active users on the account and their roles.

Tools: getUsers

### Workflow usage audit

AdditionalWorkflows: Maestro and CLM

List all published Maestro workflows and flag any that have not been started in 30 days.

Tools: getWorkflowsList · getWorkflowInstancesList

### Trigger readiness

AdditionalWorkflows: Maestro and CLM

Which workflows use the From an API call start method, and which cannot be triggered by an assistant?

Tools: getWorkflowsList · getWorkflowTriggerRequirements

### Health check

AdditionaleSign: envelopes, recipients and templates

Summarize envelope volume by status for the last 30 days.

Tools: getEnvelopes

### Failure review

AdditionaleSign: envelopes, recipients and templates

List envelopes voided or declined this week, with the sender for each.

Tools: getEnvelopes

## Skills for this role

Install the core skill first, then add the team skills.

[docusign-agreements (core)](/PSA/AI-Cookbook-v2/skills/docusign-agreements/) · [mcp-access-audit](/PSA/AI-Cookbook-v2/skills/mcp-access-audit/) · [envelope-health](/PSA/AI-Cookbook-v2/skills/envelope-health/)

Source: /PSA/AI-Cookbook-v2/prompts/it-and-admin/
