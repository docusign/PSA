# Security

## What This Tool Does NOT Do

- **No login or OAuth flow** — this tool never asks for or processes credentials.
- **No token collection** — access tokens are never entered into, stored by, or transmitted from this website.
- **No API calls** — the browser makes zero outbound requests to Docusign or any other service.
- **No analytics on user input** — account IDs and model content entered into the form are used only for local rendering of personalized instructions.
- **No client secrets or private keys** — these are never requested or referenced.

## How Tokens Are Handled

All generated instructions use environment variables or Postman placeholder variables for tokens:

- cURL commands reference `${DOCUSIGN_ACCESS_TOKEN}` (a shell environment variable).
- Postman collections use `{{accessToken}}` (a Postman variable).
- Users are instructed to clean up tokens after use.

## Account ID

The account ID is used solely to personalize generated URLs and commands. It is not a login credential and does not grant access to any Docusign resources on its own.

## Recommendations

- Obtain tokens through your organization's approved OAuth process.
- Never paste tokens into this website or any other web form.
- Do not commit tokens, secrets, or environment files to source control.
- Remove environment variables containing tokens after use.
- Redact tokens before sharing logs or screenshots.
