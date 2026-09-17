# Prerequisites

Before registering a Concerto model, ensure you have:

1. **A Docusign account** with access to Maestro and CLM.
2. **An OAuth access token** obtained through your organization's approved process.
3. **Your account ID** found in the Docusign admin console.
4. **A Concerto model file** (`.cto`) describing the fields to send to CLM.
5. **A tool for making API requests:** Postman, cURL, or VS Code with terminal.

## Account ID

The account ID identifies the target Docusign account. It is not a login credential. It is a UUID visible in the Docusign admin console URL.

## Access Token

This guide does not ask for or collect access tokens. You must obtain a valid OAuth token through your organization's approved process before making the registration API call.
