# Postman Guide

## Steps

1. Obtain an OAuth access token through your organization's approved process.
2. Open Postman.
3. Create a new POST request.
4. Set the URL: `{baseUrl}/v1/accounts/{accountId}/workflows/models`
5. Add headers:
   - `Authorization: Bearer <ACCESS_TOKEN>`
   - `Accept: application/json`
   - `Content-Type: application/json`
6. Select Body → raw → JSON.
7. Paste the model registration JSON.
8. Send the request.
9. Review the response (expect 2xx).
10. Verify the model in Maestro.

## Postman Collection

The website generates a downloadable Postman collection with:

- `{{baseUrl}}` variable
- `{{accountId}}` variable
- `{{accessToken}}` variable (placeholder only)
- The registration request pre-configured
- A basic response test

## Security

Do not commit or share your Postman environment file if it contains a real access token. Use Postman environment variables and keep token values local.
