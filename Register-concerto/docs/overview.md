# Overview

Concerto model registration is the process of making a data model available to the Maestro "Send Data to CLM" workflow step.

## What Registration Involves

1. **Define a Concerto data model** — describe the fields your workflow will send to CLM.
2. **Convert the `.cto` model to Concerto metamodel JSON** — the API accepts the metamodel format.
3. **Submit the JSON to the account-scoped Maestro API endpoint** — a manual POST request.
4. **Use the registered model in Maestro** — select it in the "Send Data to CLM" step.

## What Registration Does NOT Do

- Create a Docusign account
- Enable IAM or configure authentication
- Create a Maestro workflow
- Map fields between systems
- Populate data in CLM

Registration only makes the model available as a schema that Maestro can reference.
