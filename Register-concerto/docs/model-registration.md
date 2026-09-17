# Model Registration

## Creating the Model

A Concerto model (`.cto` file) defines the fields that a Maestro workflow sends to CLM.

### Sample Model

```cto
namespace DataToCLM@1.0.0

concept DataToCLM {
  o String EnvelopeId
}
```

### Common Field Types

- `String` — text values
- `Integer` — whole numbers
- `DateTime` — date and time values
- `Boolean` — true/false values
- `Double` — decimal numbers

## Converting to JSON

The API accepts Concerto metamodel JSON, not raw `.cto` syntax.

### Option A: Concerto CLI

```bash
npx @accordproject/concerto-cli compile --model model.cto --target JSONSchema
```

### Option B: JSON Template

```json
{
  "payload": {
    "$class": "concerto.metamodel@1.0.0.Model",
    "decorators": [],
    "namespace": "DataToCLM@1.0.0",
    "imports": [],
    "declarations": [
      {
        "$class": "concerto.metamodel@1.0.0.ConceptDeclaration",
        "name": "DataToCLM",
        "isAbstract": false,
        "properties": [
          {
            "$class": "concerto.metamodel@1.0.0.StringProperty",
            "name": "EnvelopeId",
            "isArray": false,
            "isOptional": false
          }
        ]
      }
    ]
  }
}
```

Validate this template against your actual model before submitting.

## API Endpoint

```
POST /v1/accounts/{accountId}/workflows/models
```

An older or internal registration form may use a `/declarations` endpoint. Confirm which endpoint your environment expects.
