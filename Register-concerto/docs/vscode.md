# VS Code / Terminal Guide

## Workflow

1. **Save the model** as `model.cto`.
2. **Convert** to `model-registration.json` using the Concerto CLI or the JSON template.
3. **Open the terminal** in VS Code (`Ctrl+\`` or `Cmd+\``).
4. **Set the access token** as an environment variable.
5. **Run the cURL command** to register the model.
6. **Review the response** (expect 2xx with model details).
7. **Clean up** — remove the environment variable.
8. **Verify** the model in Maestro.

## Converting the Model

```bash
npx @accordproject/concerto-cli compile --model model.cto --target JSONSchema
```

Or download the pre-built JSON template from the Convert step in the web guide.

## Token Handling

Set the token only in your local terminal session. Never commit it, save it in a file within the repository, or include it in URLs.
