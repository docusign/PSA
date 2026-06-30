# DocuSign Template Format Reference

## Request Body Structure
```json
{
    "name": "Template Name",
    "description": "Template Description",
    "shared": "false",
    "emailSubject": "Please sign this document",
    "status": "created",
    "documents": [...],
    "recipients": {
        "signers": [...],
        "carbonCopies": [...]
    }
}
```

## Documents Array
```json
{
    "documentBase64": "<base64_encoded_pdf>",
    "documentId": "1",  // String, not integer
    "fileExtension": "pdf",
    "name": "Document Name"
}
```

## Recipients Structure

### Signers
```json
{
    "recipientId": "1",  // String
    "roleName": "signer",
    "routingOrder": "1",  // String
    "tabs": {
        "signHereTabs": [...],
        "initialHereTabs": [...],
        "textTabs": [...],
        "checkboxTabs": [...],
        "radioGroupTabs": [...],
        "listTabs": [...],
        "dateTabs": [...],
        "numericalTabs": [...]
    }
}
```

### Carbon Copies
```json
{
    "recipientId": "2",
    "roleName": "cc",
    "routingOrder": "2"
}
```

## Tab Types and Properties

### Common Tab Properties
- `documentId`: String ("1", "2", etc.)
- `pageNumber`: String ("1", "2", etc.)
- `xPosition`: String coordinate
- `yPosition`: String coordinate
- `required`: "true" or "false" (String)
- `tabLabel`: Unique identifier for the tab

### SignHere Tab
```json
{
    "documentId": "1",
    "pageNumber": "1",
    "xPosition": "191",
    "yPosition": "148"
}
```

### InitialHere Tab
```json
{
    "documentId": "1",
    "pageNumber": "1",
    "xPosition": "191",
    "yPosition": "148"
}
```

### Text Tab
```json
{
    "documentId": "1",
    "pageNumber": "1",
    "xPosition": "153",
    "yPosition": "230",
    "width": 84,  // Integer
    "height": 23,  // Integer
    "font": "helvetica",
    "fontSize": "size14",
    "tabLabel": "text",
    "required": "false"
}
```

### Checkbox Tab
```json
{
    "documentId": "1",
    "pageNumber": "1",
    "xPosition": "75",
    "yPosition": "417",
    "tabLabel": "ckAuthorization"
}
```

### Radio Group Tab
```json
{
    "documentId": "1",
    "groupName": "radio1",
    "radios": [
        {
            "pageNumber": "1",
            "xPosition": "142",
            "yPosition": "384",
            "value": "option1",
            "required": "false"
        }
    ]
}
```

### List Tab (Dropdown)
```json
{
    "documentId": "1",
    "pageNumber": "1",
    "xPosition": "142",
    "yPosition": "291",
    "font": "helvetica",
    "fontSize": "size14",
    "tabLabel": "list",
    "required": "false",
    "listItems": [
        {"text": "Option 1", "value": "opt1"},
        {"text": "Option 2", "value": "opt2"}
    ]
}
```

### Date Tab
```json
{
    "documentId": "1",
    "pageNumber": "1",
    "xPosition": "153",
    "yPosition": "260",
    "width": 84,
    "font": "helvetica",
    "fontSize": "size14",
    "tabLabel": "date",
    "required": "false"
}
```

### Numerical Tab
```json
{
    "documentId": "1",
    "pageNumber": "1",
    "xPosition": "153",
    "yPosition": "260",
    "width": 84,
    "height": 23,
    "validationType": "Currency",  // or "Number"
    "font": "helvetica",
    "fontSize": "size14",
    "tabLabel": "numericalCurrency",
    "required": "false"
}
```

## Critical Conversion Rules

### 1. Data Type Conversions
- ALL IDs are STRINGS: `recipientId`, `documentId`, `routingOrder`
- ALL coordinates are STRINGS: `xPosition`, `yPosition`, `pageNumber`
- Boolean fields use STRINGS: `"true"` or `"false"` for `required`, `shared`
- Dimensions (`width`, `height`) remain as INTEGERS

### 2. Coordinate System Transformation
**From Dropbox Sign (80 DPI) to DocuSign (72 DPI):**
```python
# For all tabs:
docusign_x = round((dropbox_x * 0.9) - 100)
docusign_y = round(dropbox_y * 0.9)

# Additional Y-axis adjustments:
# SignHere tabs: subtract 21 from final Y
# InitialHere tabs: subtract 16 from final Y
```

### 3. Structure Mapping
- Dropbox `form_fields` → DocuSign `tabs` (grouped by type)
- Dropbox `signer` role → DocuSign `signers` array
- Dropbox flat recipient array → DocuSign nested `recipients.signers` and `recipients.carbonCopies`

### 4. Tab Type Mapping
| Dropbox Sign Type | DocuSign Tab Type |
|------------------|-------------------|
| signature | signHereTabs |
| initials | initialHereTabs |
| text | textTabs |
| checkbox | checkboxTabs |
| radio | radioGroupTabs |
| dropdown | listTabs |
| date_signed | dateTabs |
| text (with validation) | numericalTabs |

### 5. Special Considerations
- Group radio buttons by `group` field into `radioGroupTabs`
- Convert dropdown `options` to `listItems` with `text` and `value`
- Add `tabLabel` for form field identification
- Set `status: "created"` for draft templates
- Include `emailSubject` for signing requests
- Use `documentBase64` (not `document_base64`)

## Example Complete Template
```json
{
    "name": "Example Template",
    "description": "Migrated from Dropbox Sign",
    "shared": "false",
    "emailSubject": "Please sign this document",
    "status": "created",
    "documents": [
        {
            "documentBase64": "JVBERi0xLjQKJeLj...",
            "documentId": "1",
            "fileExtension": "pdf",
            "name": "Contract.pdf"
        }
    ],
    "recipients": {
        "signers": [
            {
                "recipientId": "1",
                "roleName": "signer",
                "routingOrder": "1",
                "tabs": {
                    "signHereTabs": [
                        {
                            "documentId": "1",
                            "pageNumber": "1",
                            "xPosition": "100",
                            "yPosition": "200"
                        }
                    ],
                    "textTabs": [
                        {
                            "documentId": "1",
                            "pageNumber": "1",
                            "xPosition": "150",
                            "yPosition": "250",
                            "width": 100,
                            "height": 20,
                            "tabLabel": "name",
                            "required": "true"
                        }
                    ]
                }
            }
        ],
        "carbonCopies": []
    }
}
``` 