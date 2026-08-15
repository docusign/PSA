# Agent Studio 201 - Session Brief (Aug 13-14, 2026)

## What we built

### 1. Maestro workflow (step-by-step)
- Trigger: Agreement Desk request submitted
- Execute AI Agent: Vendor and Renewal Risk Analyst
- Multi Branch Rule on `risk_level`: LOW / MEDIUM / HIGH / Fallback

### 2. Agent outputs defined
- `risk_level` (text)
- `liability_cap` (text)
- `governing_law` (text)
- `term` (text)
- `discount` (text)

### 3. Agent prompt (Chat Message in Maestro step)
```
Analyze this vendor contract against our procurement risk checklist. Return risk_level, liability_cap, governing_law, term, and discount. Flag violations with severity and section reference.
```

### 4. Agent system instructions (6-point risk checklist)
- Role: Expert Risk and Compliance Assistant analyzing attached vendor contract
- Step 1: Document Analysis (vendor name, contract type, dates, key terms)
- Step 2: Six-point risk checklist:
  - Payment Terms: must be 50+ days
  - Renewal: auto-renewal is out-of-standard
  - Termination: must have Right to Terminate Without Cause
  - Liability: must have clear Liability Cap
  - IP: must not give away company IP rights
  - Change of Control: must have protection if vendor is acquired
- Step 3: Output five fields, classify risk_level (HIGH/MEDIUM/LOW based on violated rules)
- Step 4: Clean output rule (LOW with "No action required" if zero risks)

### 5. Agreement Desk intake form fields
- Vendor name
- Requester name
- Estimated annual spend
- Jurisdiction
- Category
- Contract term
- Proposed discount
- Upload contract (optional)

### 6. Branching logic
| Branch | Condition | Action |
|---|---|---|
| Low risk | `risk_level == "LOW"` | Change status → Approved for Signature |
| Medium risk | `risk_level == "MEDIUM"` | Assign owner + create approval request |
| High risk | `risk_level == "HIGH"` | Change status → Legal Review Required |
| Fallback | No valid data | Change status → Manual Review |

### 7. Dual-path design
- Document attached: agent reads contract, extracts all 5 fields
- No document: agent triages from intake fields only, returns "not specified" for fields it cannot extract

### 8. workshop.html created
- New page: `https://docusign.github.io/PSA/Agent-Studio-201/workshop.html`
- "Pick your scenario" toggle (NDA / Procurement) injected into page content
- Hides the Sales/Renewal persona toggle from procurement page
- No changes to existing NDA or procurement HTML files

### 9. 2_Hands_on_Flow.html updated
- Agent prompt in section 1.2 updated with new rules
- Chat Message references in sections 2.5 and 4.2 updated

## Test values

**LOW:**
Acme Cloud Services / Sarah Johnson / 200000 / Delaware / SaaS / 2 years / 10%

**MEDIUM:**
GlobalTech Solutions / Mark Chen / 500000 / Singapore / Professional Services / 18 months / 20%

**HIGH:**
RiskyVentures Ltd / James Patel / 1500000 / Cayman Islands / IT Infrastructure / 6 months / 40%

## Known issue
- Medium-risk sample PDF (`msa_medium_risk.pdf`) was being classified as LOW before the prompt update. Fixed by tightening MEDIUM rules (1x cap, missing DPA, asymmetric indemnity).

## Open question
- JSON output format in agent instructions may not be needed for Maestro workflow (Maestro binds outputs via defined agent output fields). Untested - try removing JSON requirement and verify outputs still map correctly.
