# Tool names

| Tool | Use it for | Gotcha |
| --- | --- | --- |
| `getEnvelopeVsAgreementSkill` Verified | Route a request to agreements, envelopes or both | Call first, before getAllAgreements or getEnvelopes |
| `getAgreementFilterSkill` Verified | Exact filter fields and OData syntax | Call before any filtered getAllAgreements |
| `getAllAgreements` Verified | Agreement terms: expiry, renewal, governing law, payment terms | Filters: eq, gt, ge, lt, le, in, and only. Max 20 per page |
| `getAgreementDetails` Verified | Full record for one agreement | Needs agreementId |
| `getEnvelopes` Verified | Signing status, folders such as waiting\_for\_others, completed and voided | Needs from\_date or envelope IDs; defaults to 30 days |
| `getTemplates` Verified | Find the template before any send or draft | Never assume a template; the user must name it |
| `createEnvelope` Verified | Draft (status created) or send from a template or remote URL | Use status created for drafts; documents cannot be added later |
| `createEnvelopeFromTemplate` Verified | Template-based envelope that sends to recipients | Sends. Do not use for drafts |
| `updateEnvelopeRecipients` Verified | Change recipients on an in-flight envelope | Write action; confirm first |
| `sendReminder` Verified | Reminder to pending remote signers | After approval only; embedded signers are skipped |
| `listRecipients` Verified | Who still has to act on an envelope | Check before reminders |
| `getWorkflowsList` Verified | List Maestro workflows (active or paused) | Ask CLM or Maestro first |
| `getWorkflowTriggerRequirements` Verified | Inputs a Maestro workflow needs | Call before triggerWorkflow |
| `triggerWorkflow` Verified | Start a Maestro workflow instance | Only workflows with start method From an API call |
| `getWorkflowInstancesList` Verified | Status of running Maestro instances | Needs workflowId |
| `getClmWorkflowDefinitions` Verified | List CLM workflow definitions | CLM only; paged with cursor |
| `startClmWorkflow` Verified | Start a CLM workflow by name | Exact definition name; documents need an href |
| `getAccount · getBrands · getUsers` Verified | Admin checks: account, brands, users | Read only |
| `searchDocusignDocs` Verified | Search Developer Center docs | Public docs |

Source: /PSA/AI-Cookbook-v2/reference/tools/
