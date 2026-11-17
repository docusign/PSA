# Troubleshooting

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| **No agreements visible** | Connected to production, or Agreement Manager still extracting | Reconnect with sandbox credentials. Wait 3–5 minutes per document. Ask: What Docusign account am I connected to? |
| **Agreement fields blank or partial** | Extraction still running, or unsupported file | Click Re-analyze and wait five minutes. |
| **Workflow not listed** | Workflow is in Draft | Open the workflow under Workflows and Publish. Wait about 60 seconds. |
| **Agent cannot find templates** | No templates in the sandbox | Import the template from the sample agreement pack under Document Templates. |
| **Envelope send fails** | Required fields empty, or sandbox email restriction | Try a different recipient. Compare with a manual send using the same values. |
| **Old data returned** | Agent reuses earlier chat results | Ask it to refresh agreements from Docusign. |
| **Workflow says started but did not run** | Trigger inputs did not match required fields | Check the trigger inputs in the activity map, or run the workflow manually in Maestro. |
| **No tools/call in the activity map** | Generative orchestration off, or instructions allow answering from memory | Turn on generative orchestration. Require an MCP call for any live Docusign state. Republish. |
| **Agent missing from Teams or M365 Copilot** | Channel off, not published, or tenant approval pending | Confirm the channel is on and published. Ask your tenant admin to approve. Allow propagation time. |

Source: /PSA/AI-Cookbook-v2/reference/troubleshooting/
