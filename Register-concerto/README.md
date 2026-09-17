# Docusign Concerto Model Registration Guide

A static instructional website that guides users through manually registering a Concerto data model in their Docusign account for use with Maestro workflows.

**This tool does not log users in and does not register models automatically. It generates step-by-step instructions and commands that users execute manually using their own approved Docusign authentication.**

## What It Does

- Explains what Concerto model registration is and why it's needed
- Helps users create and customize a `.cto` model file
- Provides a JSON metamodel template for the registration API
- Generates personalized Postman, cURL, and VS Code instructions based on the user's environment and account ID
- Includes downloadable files (model, JSON payload, Postman collection)
- Covers troubleshooting for common API error codes

## What It Does NOT Do

- Log users in or collect credentials
- Make any API calls from the browser
- Store tokens, secrets, or private keys
- Execute model registration automatically
- Collect analytics on user input

## Run Locally

```bash
npm install
npm run dev
```

Open [http://localhost:5173/Register-concerto/](http://localhost:5173/Register-concerto/)

## Build

```bash
npm run build
```

Output is in `dist/`.

## Test

```bash
npx vitest run
```

## Type Check

```bash
npx tsc -b
```

## Deploy to GitHub Pages

1. Push to the `main` branch of a GitHub repository named `Register-concerto`.
2. Enable GitHub Pages in the repository settings (Source: GitHub Actions).
3. The `.github/workflows/deploy.yml` workflow will build, test, and deploy automatically.

The site will be available at `https://<org>.github.io/Register-concerto/`.

## Tech Stack

- Vite + React + TypeScript
- DSIndigo font (Docusign brand)
- Vitest + Testing Library
- GitHub Actions for CI/CD

## Endpoint Assumptions

The default registration endpoint used is:

```
POST /v1/accounts/{accountId}/workflows/models
```

Environment base URLs:
- **Demo:** `https://demo.services.docusign.net`
- **Stage:** `https://stage.services.docusign.net`
- **Production:** `https://services.docusign.net`

### Items Requiring Confirmation

- Verify the registration endpoint path (`/v1/accounts/{accountId}/workflows/models`) is correct for all environments.
- Confirm whether a `/declarations` endpoint variant exists and under what conditions it should be used.
- Validate the Concerto metamodel JSON structure against the current API schema.
- Confirm the Concerto CLI compile command produces the exact format expected by the API.

## Documentation

See the `docs/` directory:

- [Overview](docs/overview.md)
- [Prerequisites](docs/prerequisites.md)
- [Model Registration](docs/model-registration.md)
- [Postman Guide](docs/postman.md)
- [cURL Guide](docs/curl.md)
- [VS Code Guide](docs/vscode.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Security](docs/security.md)
