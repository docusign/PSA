# cURL Guide

## Set the Access Token

### macOS / Linux

```bash
export DOCUSIGN_ACCESS_TOKEN="paste-token-in-terminal-only"
```

### Windows PowerShell

```powershell
$env:DOCUSIGN_ACCESS_TOKEN = "paste-token-in-terminal-only"
```

## Run the Registration Command

```bash
curl --request POST \
  --url "{baseUrl}/v1/accounts/{accountId}/workflows/models" \
  --header "Authorization: Bearer ${DOCUSIGN_ACCESS_TOKEN}" \
  --header "Accept: application/json" \
  --header "Content-Type: application/json" \
  --data @model-registration.json
```

## Clean Up

### macOS / Linux

```bash
unset DOCUSIGN_ACCESS_TOKEN
```

### Windows PowerShell

```powershell
Remove-Item Env:DOCUSIGN_ACCESS_TOKEN
```

## Token Safety

- Do not put the token in the URL.
- Do not commit the token to source control.
- Do not save the token in your repository.
- Remove the environment variable after use.
