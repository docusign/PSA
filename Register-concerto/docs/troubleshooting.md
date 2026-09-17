# Troubleshooting

## Common Error Codes

| Code | Meaning | What to Check |
|------|---------|---------------|
| 400 | Bad Request | Invalid JSON syntax or model structure. Validate your JSON file. |
| 401 | Unauthorized | Missing, expired, or invalid token. Get a fresh token. |
| 403 | Forbidden | Insufficient account access or permissions. Contact your admin. |
| 404 | Not Found | Wrong environment URL, account ID, or endpoint path. |
| 409 | Conflict | Model/version already exists. Increment the version or delete the existing model. |
| 429 | Rate Limited | Too many requests. Wait and retry. |
| 5xx | Server Error | Temporary issue. Wait and retry. Check the Docusign status page. |

## General Tips

- Validate JSON before sending (`jq .` or a JSON linter).
- Ensure `Content-Type: application/json` is set.
- Check that your token hasn't expired.
- Verify the base URL is reachable from your network.
- Never share authorization headers or tokens in logs or screenshots.
