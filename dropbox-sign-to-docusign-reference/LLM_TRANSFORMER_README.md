# LLM-Powered Template Transformer

## Overview

The LLM-powered transformer uses Azure OpenAI GPT-4 to intelligently convert Dropbox Sign templates to DocuSign format. This approach is **significantly more flexible and accurate** than rule-based transformation, especially for complex templates.

## Why Use LLM Transformation?

### Advantages Over Rule-Based Approach

1. **Handles Complexity**: Works seamlessly with templates containing hundreds or thousands of fields
2. **Intelligent Mapping**: Understands context and makes smart decisions about field types
3. **Zero Maintenance**: No need to update mapping rules when APIs change
4. **Edge Case Handling**: Automatically handles unusual field types and configurations
5. **Cost-Effective**: ~$0.001 per simple template, ~$0.05 for complex 1000-field templates

### When LLM Excels

- Templates with mixed field types (signatures, initials, text, dates, checkboxes)
- Complex conditional logic between fields
- Templates with custom validation rules
- Documents with multiple signers and routing orders
- Templates requiring business logic understanding

## Setup

### 1. Azure OpenAI Configuration

Add these to your `.env` file:

```env
# Azure OpenAI Configuration
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_API_KEY=your_azure_openai_api_key_here
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4
AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

### 2. Install Dependencies

```bash
pip install openai
```

## Usage

### Via Web UI

1. Connect to Dropbox Sign
2. Download a template
3. Click "Migrate to DocuSign" - the LLM transformer is used by default

### Via Command Line

```bash
# Migrate a specific template
cd dropboxsign-to-docusign
python src/llm_transformer.py 0931d9d4ec3c6dec4bc26de0975dd412d846e939
```

### Via API

```python
from src.llm_transformer import LLMTemplateTransformer

# Initialize transformer
transformer = LLMTemplateTransformer()

# Migrate a template
result = transformer.migrate_template(template_id)
print(f"Created DocuSign template: {result['templateId']}")
```

## How It Works

### 1. System Prompt Engineering

The transformer uses a comprehensive system prompt that includes:
- Field type mappings (signature → signHereTabs)
- Coordinate transformations (pixels → points)
- DocuSign API schema requirements
- Best practices for template structure

### 2. Transformation Process

```
Dropbox Sign JSON → LLM Analysis → DocuSign Payload → API Creation
```

1. **Read Template Data**: Load Dropbox Sign API response and PDF
2. **LLM Transformation**: GPT-4 converts to DocuSign format
3. **Validation**: Verify required fields and structure
4. **API Call**: Create template in DocuSign

### 3. Field Mapping Examples

| Dropbox Sign | DocuSign | Notes |
|--------------|----------|-------|
| `signature` | `signHereTabs` | Signature fields |
| `initials` | `initialHereTabs` | Initial fields |
| `text` | `textTabs` | Text input fields |
| `date` | `dateTabs` | Date picker fields |
| `checkbox` | `checkboxTabs` | Checkbox fields |
| `dropdown` | `listTabs` | Dropdown lists |

### 4. Coordinate Conversion

- Dropbox Sign: Pixels
- DocuSign: Points (1 pixel ≈ 0.75 points)
- LLM handles conversion automatically

## Example Transformation

### Input (Dropbox Sign)
```json
{
  "form_fields": [
    {
      "name": "Signature1",
      "type": "signature",
      "x": 168,
      "y": 319,
      "required": true
    }
  ]
}
```

### Output (DocuSign)
```json
{
  "recipients": {
    "signers": [{
      "tabs": {
        "signHereTabs": [{
          "tabLabel": "Signature1",
          "xPosition": "126",
          "yPosition": "239",
          "required": "true"
        }]
      }
    }]
  }
}
```

## Files Generated

For each migrated template:
- `dropbox_api_response.json` - Original Dropbox Sign data
- `template.pdf` - Downloaded PDF document
- `docusign_payload.json` - Transformed DocuSign payload
- `docusign_result.json` - DocuSign API response

## Error Handling

The transformer includes fallback to rule-based transformation if:
- Azure OpenAI is not configured
- LLM service is unavailable
- JSON parsing fails

## Cost Analysis

| Template Complexity | Fields | Approximate Cost |
|--------------------|--------|------------------|
| Simple | 1-10 | $0.001 |
| Medium | 10-100 | $0.01 |
| Complex | 100-1000 | $0.05 |
| Very Complex | 1000+ | $0.10 |

Compare to developer time: 1 hour of manual mapping = $100+ vs $0.05 for LLM

## Troubleshooting

### Common Issues

1. **Missing Azure OpenAI Config**
   - Ensure all `AZURE_OPENAI_*` variables are in `.env`
   - Verify endpoint URL format (must end with `/`)

2. **Authentication Errors**
   - Check API key is valid
   - Verify deployment name matches your Azure setup

3. **Transformation Failures**
   - Review `docusign_payload.json` for issues
   - Check console output for specific errors
   - Fallback to basic transformer will activate automatically

## Advanced Features

### Custom System Prompts

Modify the system prompt in `llm_transformer.py`:

```python
def create_system_prompt(self) -> str:
    return """Your custom instructions here..."""
```

### Temperature Tuning

Adjust creativity vs consistency:

```python
temperature=0.1  # Lower = more consistent (default)
temperature=0.7  # Higher = more creative
```

### Batch Processing

Process multiple templates:

```python
for template_id in template_ids:
    result = transformer.migrate_template(template_id)
    print(f"Migrated: {result['templateId']}")
```

## Future Enhancements

- [ ] Support for complex conditional logic
- [ ] Multi-document template handling
- [ ] Bulk migration with progress tracking
- [ ] Template validation before migration
- [ ] Custom field mapping rules via UI
- [ ] Support for other LLM providers (OpenAI, Anthropic)

## Support

For issues or questions:
1. Check the console output for detailed error messages
2. Review generated files in `templates/dropbox_sign/[template_id]/`
3. Verify Azure OpenAI configuration
4. Try with a simpler template first
5. Use basic transformer as fallback 