# Speaker Notes - Bengaluru Meetup: Docusign Manage Workshop
**Runtime:** ~65–75 min | **Audience:** Implementation-partner architects & developers + cross-functional business stakeholders

---

## Before the session

Attendees do ingestion (Stage 1), extraction (Stage 2), and agent setup (Stage 3) live - nothing to pre-run. Your checklist is just access and tools.

- **Your machine:** Node + npm installed, `@docusign/agreement-cli@1.1.0-beta` installed globally - run `docusign` to confirm it's on PATH
- **Demo account:** logged into `apps-d.docusign.com`, Agreement Manager enabled, CLI (open beta) access on the account
- **Workshop resources:** downloaded and unzipped - `workshop-resources/` folder ready with the manifest, training docs, and ingest contracts
- **Copilot Studio access:** Microsoft 365 / Copilot Studio environment ready to create a blank agent in Stage 3
- Have the lab page open: https://docusign.github.io/PSA/Bengaluru-meetup/2_Hands_on_Flow.html
- Have `apps-d.docusign.com` open in a second tab

---
## Stage 0 · Before you begin (5 min)

**Goal:** Set the scene - why agreements matter as data, not just documents.

### What to say

> "At Fontara, procurement is buried in vendor contracts and PDFs - and you're here to change that.
>
> The procurement team owns thousands of vendor agreements, MSAs, SOWs, and NDAs, all stored as flat PDFs across shared drives and inboxes. The documents are signed and safe, but the agreement data the business cares about is locked inside.
>
> That means nobody can answer the questions leaders actually ask: Which contracts auto-renew next quarter? Which vendors are on payment terms longer than 45 days? Where are we missing a price-increase cap? What is our total committed spend with this supplier? Today, every question means a human opening files one by one and reading them manually.
>
> Over the next hour, you are going to change that with Docusign, AI, and MCP. You will treat agreements as data, not just documents - automated, repeatable, and scalable. Not by hand."
### Pattern to land
> Ingest once → Extract with AI → Expose via MCP → Deploy agents everywhere

### Prereqs check - step by step (attendees do this, you verify)

**0.4.1 - Node + npm + CLI**
```
node -v && npm -v
```
- Two version numbers (e.g. `v20.x.x` and `10.x.x`)? Good, skip the install.
- "command not found"? Install Node.js LTS from nodejs.org first, then re-run.
```
npm i -g @docusign/agreement-cli@1.1.0-beta
```
```
docusign
```
- `docusign` with no arguments should print the help/command list - confirms the CLI is on PATH. If it errors, the install didn't complete.

**0.4.2 - Accounts and access**
- Each attendee needs a Docusign developer/demo account with Agreement Manager and CLI (open beta) access enabled
- For Stage 3: a Microsoft 365 / Copilot Studio environment where they can create agents and add MCP tools

**0.4.3 - Download workshop resources**
- Download and unzip `workshop-resources.zip` into their working directory
- Confirm they have:
  - `workshop-resources/agreement-manager-manifest.json`
  - `workshop-resources/files/train/` (7 sample agreements)
  - `workshop-resources/files/ingest/` (4 contracts)

**0.4.4 - Import and Publish the Workflow**
- Go to `apps-d.docusign.com` → Agreements → Workflows → **Import**
- Upload `Fontara Renewal Order Form.zip` from `workshop-resources/workflow/`
- Open the imported workflow → update the **Agreement Desk routing email** to a valid mailbox → **Save** → **Review** → **Publish**
- **Must be Published, not Draft** - the MCP agent in Stage 3 can only trigger Published workflows. If it's in Draft when they reach Scenario B, nothing will work.

**Unlock the stages**
- Tick all 4 prereq checkboxes on the lab page - the modal auto-pops and unlocks Stages 1-4
- If the modal doesn't appear: confirm all 4 checkboxes are ticked (scroll up to check)

---

## Stage 1 · Docusign CLI + Agreement CLI (15 min)

**Goal:** Show that agreement configuration and bulk ingestion is code - repeatable, version-controlled, partner-deliverable.

### Talk track - opening (say this before running the first command)
> "Right now, if you want to set up Agreement Manager for a client - define their agreement types, their custom fields, map everything together - you'd click through the UI, manually, for every account. That doesn't scale.
>
> What we're going to do instead is define all of that as a JSON manifest. Three agreement types, nine custom pharma fields, training documents, all of it. One file. And then we'll deploy it with a single CLI command.
>
> The same manifest you test in a dev account today? You hand it to the client, point it at production, run the same command. Done. No re-clicking, no re-configuring, no human error."

### The four Docusign CLI value points (land at least two of these)
- **Custom configuration** - extend Agreement Manager with custom agreement types and fields, defined as code in the manifest
- **Extraction testing** - validate Iris extraction accuracy against ground-truth values *before* deploying to production (`ds agm test`)
- **Multi-account deployment** - build the configuration package once, deploy it to multiple production accounts
- **Bulk ingestion via CLI** - ingest agreements plus metadata at scale from a local or network directory

> "This is the Docusign CLI - it is in open beta. The command prefix is `docusign agm` or the short form `ds agm`. Everything we run today is one of those commands."

### How the manifest works - what to explain while running 1.3

The manifest (`agreement-manager-manifest.json`) is a single JSON file that describes everything Agreement Manager needs to understand Fontara's procurement contracts. Walk through these three concepts as you copy it in:

**1. Custom agreement types** - three types defined, each with an `aiDefinition`:
- `Clinical Trial Supply Agreement` - manufacture/supply of investigational drug products under GMP. Trained on 3 sample documents.
- `CRO Services Agreement` - contract research org for trial management, patient recruitment, site monitoring. Trained on 2 sample documents.
- `Medical Device Supply Agreement` - supply of medical devices with regulatory compliance. Trained on 2 sample documents.

The `aiDefinition` is the instruction to Iris - it tells the model exactly what language, structure, and roles distinguish this agreement type from generic categories like "Miscellaneous". This is why it says "must NOT be confused with License, Subscription, or other broad categories" - without that, Iris would bucket pharma contracts into generic types and extraction accuracy drops.

**2. Custom fields** - 9 fields across the 3 types, each with:
- A `fieldType` (Number, in all 9 cases here)
- An `aiDefinition` telling Iris exactly what to look for and where (pricing sections, schedules, exhibits)
- `examples` - 3 ground-truth examples per field showing real clause text and the confirmed extracted value. This is the training signal.

| Field | Type | Mapped to |
|---|---|---|
| `Pharma - Clinical Batch Size (units)` | Number | Clinical Trial Supply |
| `Pharma - Cost Per Unit (USD)` | Number | Clinical Trial Supply |
| `Pharma - Required Shelf Life (months)` | Number | Clinical Trial Supply |
| `Pharma - Total Study Budget (USD)` | Number | CRO Services |
| `Pharma - Number of Clinical Sites` | Number | CRO Services |
| `Pharma - Patient Enrollment Target` | Number | CRO Services |
| `Pharma - Annual Device Purchase Value (USD)` | Number | Medical Device Supply |
| `Pharma - FDA Device Classification` | Number | Medical Device Supply |
| `Pharma - Consignment Inventory Period (days)` | Number | Medical Device Supply |

**3. Standard fields** - on top of custom fields, each type also enables built-in Docusign fields: Payment Terms, Governing Law, Renewal, Termination Notice. These come free - no custom definition needed.

> "The manifest is the complete specification of what Fontara's Agreement Manager should know. Agreement types, custom fields, training examples, standard field mappings - all in one file. That's what `agm upload` reads and deploys."

---

### How training docs work - what to explain while copying `files/train/`

The `files/train/` folder contains 7 sample agreements - representative documents for each type (3 Clinical Trial Supply, 2 CRO Services, 2 Medical Device Supply). These are what Iris uses to learn the extraction patterns defined in the manifest.

The link between training docs and the manifest is in the `docs` array on each agreement type:
```json
"docs": [
  "Clinical Trial Supply Agreement - Sample 1.docx",
  "Clinical Trial Supply Agreement - Sample 2.docx",
  "Clinical Trial Supply Agreement - Sample 3.docx"
]
```
`agm upload` reads this, finds the matching files in `files/train/`, and uploads them as the AI training corpus for that type. More representative training docs = higher extraction confidence on real contracts.

> "Think of these as the ground truth. You're showing Iris what a Clinical Trial Supply Agreement looks like - the language, the structure, the clause patterns - before you ask it to read Fontara's real vendor contracts."

---

### How ingest works - what to explain during 1.5

The `files/ingest/` folder contains 4 real-world-style contracts - the "legacy repository":
- `Clinical Trial Supply Agreement - Contract 1.docx`
- `Clinical Trial Supply Agreement - Contract 2.docx`
- `Contract Research Organization (CRO) Services Agreement - Contract 1.docx`
- `Medical Device Supply Agreement - Contract 1.docx`

These are the documents you want to turn into structured data. `docusign agm ingest` uploads them to Agreement Manager, where Iris reads each one, matches it to the correct custom agreement type using the `aiDefinition`, and populates the custom and standard fields.

The `--dry-run` flag is worth showing first - it previews what will be uploaded without touching the account. Then the real ingest runs with `--bypass` to skip interactive confirmation.

> "This is the moment the legacy repository becomes structured data. Four files, one command. In production, this could be 400 files. Same command."

---

### Step by step

**Pre-session: install and confirm the CLI (do this before the room fills)**
```
npm i -g @docusign/agreement-cli@1.1.0-beta
```
```
docusign
```
- `docusign` with no arguments prints the help/command list - confirms the CLI is on PATH
- Attendees run the same install in prereq step 0.2, so they arrive with this done

---

**1.1 - Authenticate**
```
docusign auth login
```
```
docusign auth test
```
- Opens browser-based OAuth (PKCE). Each attendee uses their own Docusign demo account - no shared credentials
- On a headless machine: `docusign auth login --no-browser` prints a URL to open manually
- Expect: `Authentication is valid`

---

**1.2 - Create a working folder and scaffold the workspace**
```
mkdir ~/docusign-workshop && cd ~/docusign-workshop
```
```
docusign scaffold -w demo-workspace -p demo-project -f agreement-manager
```
- **Must `cd` first** - scaffold creates `demo-workspace/` inside whatever directory the terminal is currently in. Skip this and it lands in home directory
- Creates: `demo-workspace/demo-project/agreement-manager/` with `configs/`, `files/train/`, `files/test/`, `tests/`
- Say: "This is the project layout the CLI expects. `configs/` holds the manifest. `files/train/` holds the sample docs Iris learns from."

---

**1.3 - Download workshop resources and copy into the scaffold**
```
curl -L https://github.com/docusign/PSA/raw/main/Bengaluru-meetup/workshop-resources.zip -o workshop-resources.zip && unzip -q workshop-resources.zip && rm workshop-resources.zip
```
```
cp workshop-resources/agreement-manager-manifest.json demo-workspace/demo-project/agreement-manager/configs/agreement-manager-manifest.json
```
```
cp workshop-resources/files/train/* demo-workspace/demo-project/agreement-manager/files/train/
```
- Copies 1 manifest + 7 training docs into the scaffold
- Say: "The manifest is the spec - 3 agreement types, 9 custom fields, training examples. The 7 docs are what Iris learns from."

---

**1.4 - Get catalog and upload the manifest**
```
cd demo-workspace && docusign agm get catalog
```
```
docusign agm upload --bypass
```
- `agm get catalog` creates `standard-catalog.json` and `custom-catalog.json`. Upload reads both to avoid conflicts with existing types/fields already in the account
- `agm upload --bypass` does everything in one command: creates custom fields → creates agreement types → maps fields to types → uploads 7 training docs → kicks off AI training
- AI training runs async. Fields and types appear in the UI immediately; extraction confidence improves as Iris processes the training docs
- Say: "Fields created, types created, training uploaded, AI kicked off. One command. Not a PS ticket, not an afternoon in the UI."

---

**1.5 - Test Iris extraction accuracy against ground truth**
```
docusign agm test generate-test-template --prefill-extractions
```
```
docusign agm test run
```
- `generate-test-template --prefill-extractions` creates a test file pre-filled with Iris extraction results from the 7 training docs - your ground-truth baseline to validate against
- `agm test run` uploads the 7 training docs to Agreement Manager, runs Iris extraction on each, and compares results against the ground-truth values. Prints a pass/fail accuracy report per field
- **Why 7 agreements appear in Agreement Manager after this step:** `agm test run` sends training docs to Iris for a live extraction pass - they land in Agreement Manager as part of the test. This is expected and correct
- Say: "Before we hand this manifest to any client, we verify Iris is actually finding the right values. Green per field means the manifest and training docs are working."

---

**1.6 - Bulk ingest the real contracts**
```
cd ..
```
```
docusign agm ingest --directory workshop-resources/files/ingest --dry-run
```
```
echo "y" | docusign agm ingest --bypass --directory workshop-resources/files/ingest
```
- `--dry-run` first: previews which 4 files will be uploaded and what types they will map to - show this output before running the real ingest
- Real ingest: uploads the 4 contracts from `files/ingest/` to Agreement Manager. Iris reads each, matches to the correct custom type using `aiDefinition`, and populates all custom and standard fields
- **After this step: 11 agreements total in Agreement Manager** - 7 from `agm test run` in step 1.5 + 4 from ingest here. Both sets are expected and correct
- Say: "Four files, one command. In production this is 4,000 files from Salesforce, SharePoint, or a legacy document repository. Same command."

### Talk track - what to emphasise (say this after `docusign agm upload` completes)
> "Everything you just saw - fields created, agreement types created, training uploaded, AI kicked off - that was one command. Not a ticket to the PS team, not an afternoon in the UI.
>
> This is the developer value story. Implementation time drops by over 40% compared to manual configuration. You can version-control this manifest in Git, run it through CI, promote it from dev to prod, replicate it across client accounts.
>
> What you're handing a client isn't just a configured Docusign account - it's a repeatable, auditable asset. That's the difference between a one-time implementation and a scalable practice."

---

## Stage 2 · AI Extraction in Agreement Manager (10 min)

**Goal:** Show static PDFs becoming structured, queryable data.

### Talk track - opening (say this as you switch to Agreement Manager)
> "The contracts we just ingested are no longer flat PDFs. Docusign Iris - our agreement AI - has read every one of them and extracted structured data: the custom fields we defined in the manifest, plus standard fields like payment terms, governing law, and renewal dates. Iris also pulls out parties, obligations, key dates, and clause history. This all happens in the background, once, at ingestion time. Nobody opened a single file."

### Step by step

**2.1 - Navigate to Agreement Manager**
- Go to `apps-d.docusign.com` → **Agreements** tab → **Completed** in the left nav
- You should see **11 agreements**: 7 from `agm test run` in Stage 1 (training docs Iris ran live extraction on) + 4 from the real ingest
- Say: "Eleven total. Seven are the training samples Iris used to verify extraction accuracy in Stage 1. Four are the real vendor contracts we ingested. All processed by Iris in the background - nobody opened a single file."

**2.2 - Verify agreement types are correctly applied**
- Each agreement should show its custom type - **Clinical Trial Supply Agreement**, **CRO Services Agreement**, or **Medical Device Supply Agreement** - NOT "Miscellaneous"
- If any shows as Miscellaneous: the `aiDefinition` in the manifest is the tuning lever
- Say: "The manifest defined these types and told Iris what language distinguishes a Clinical Trial Supply from a CRO Services agreement. That is why nothing landed in Miscellaneous."

**2.3 - Open a contract and show the extraction panel**
- Open any agreement → right-hand details panel shows extracted fields alongside the PDF
- Spotlight one custom field per agreement type:
  - **Clinical Trial Supply** - `Pharma - Clinical Batch Size (units)`: batch volume commitment at a glance
  - **CRO Services** - `Pharma - Total Study Budget (USD)`: full CRO spend visibility without digging through Exhibit B
  - **Medical Device Supply** - `Pharma - FDA Device Classification`: regulatory classification extracted, no manual tagging
- Also point out standard fields: **Payment Terms**, **Governing Law**, **Renewal**, **Termination Notice** - extracted automatically on every contract, no custom definition needed
- Say: "Every field came from either the manifest or Docusign's standard field library. Iris found the value in the contract text and populated it."

**2.4 - If a field is blank**
- Click **Re-analyze** on that document and wait up to 5 minutes
- Blank means extraction is still running or that clause genuinely is not present in this contract
- Say: "Re-analyze re-runs Iris on this document. If the clause is not there, the field stays blank - which is also accurate information."

> "This pre-processing is what makes Stage 3 fast. When the agent answers a question in 10 seconds, it is not re-reading the PDFs. It is querying structured data Iris already extracted - faster, token-efficient, and permission-aware."

### Fields to highlight
| Agreement type | Show this field | Why it matters |
|---|---|---|
| Clinical Trial Supply | `Pharma - Clinical Batch Size (units)` | Batch volume commitments |
| CRO Services | `Pharma - Total Study Budget (USD)` | Full CRO spend visibility |
| Medical Device Supply | `Pharma - FDA Device Classification` | Regulatory compliance at a glance |

### Standard fields
Also point out: Payment Terms, Governing Law, Renewal, Termination Notice - extracted automatically on top of custom fields.

### Talk track - what to emphasise
> "Procurement now has payment terms, governing law, termination notice, and renewal dates extracted automatically - without any manual review - across the entire corpus. Every contract is now queryable data. This is exactly what feeds the agent in Stage 3. And because Iris governs access at the Docusign layer, an agent built on this data can only ever surface agreements the user is already permissioned to see."

---

## Stage 3 · MCP via Microsoft Copilot Studio (30 min)

**Goal:** Natural language queries against the whole vendor corpus. Show the "agent as procurement analyst" moment.

### Opening talk track - say this before anyone opens Copilot Studio

> "We are going to use Copilot Studio for this exercise because it gives everyone a fast, no-code way to build and test an agent. But I want to be clear - Copilot Studio is just one surface. The Docusign MCP server is a standard MCP endpoint. That means you can connect it to any MCP-compatible client: Claude, Cursor, VS Code, a custom-built internal tool, anything your team is already using. If you are building a custom application and you want it to have Docusign intelligence, you point it at the same MCP server and the same 30+ tools are available to you. What we are building today is the pattern. The surface you deploy it on is your choice."

Key points to land:
- Copilot Studio is the demo vehicle, not the only option
- MCP is an open standard - works with any MCP-compatible host (Claude Desktop, Cursor, custom apps, etc.)
- Docusign also has a production MCP server for when you are ready to go live
- The agreement intelligence comes from Iris pre-processing in Agreement Manager - the MCP server just exposes it

### Setup check before starting
You're running Stage 3 live alongside attendees - no pre-built agent. Everyone creates the blank agent and connects the Docusign MCP Demo connector together. Make sure before starting:
- Everyone has access to `copilotstudio.microsoft.com`
- Everyone is authenticated to their Docusign demo account (`apps-d.docusign.com`)
- The Fontara Renewal Order Form workflow was imported and **Published** at the end of 3.1
- Activity map is ON in the Test pane before running any prompts

---

### Step by step - creating the agent

**3.1 - Sign in to Copilot Studio and create a blank agent**
1. Go to `copilotstudio.microsoft.com`
2. Click **Create** → **Agent** (from blank)
3. Name it: **Fontara Procurement Agent**

**3.2 - Paste the description**

Copy-paste into the **Description** field:
```
Procurement agent that uses the Docusign MCP Demo connector to act on agreements, envelopes, templates, and workflows, for procurement teams managing vendor contracts, renewals, and obligations.
```

**3.2b - Enable Generative AI orchestration**
- In the agent settings, confirm **Generative orchestration** is turned **On**
- Without this: the agent ignores MCP tools and answers from its training data only - every prompt will show no `tools/call` in the activity map

**3.3 - Paste the system instructions**

Copy-paste into the **Instructions** field:
```
You are the Procurement Agent for Fontara, a B2B company. The procurement team manages a portfolio of vendor contracts - MSAs, SOWs, NDAs, supply agreements, and device contracts.

You help procurement teams complete all agreement tasks - getting insights from agreements, tracking envelopes and recipient information, sending reminders, using templates to create agreements, triggering workflows, etc. - using the Docusign MCP Demo connector. Treat Docusign as the source of truth for any live agreement, envelope, renewal, pricing, or clause question.

Behavior rules

1. Prefer Docusign MCP tools. For any question about envelopes, recipients, templates, signers, agreements, renewals, clauses, or signing status, call the Docusign MCP Demo tool. Never answer from training data or prior chat context for live Docusign state.

2. Use Docusign default account unless otherwise specified.

3. Workflow Builder before eSign. When sending an agreement, always check for an available published Workflow Builder workflow first and use it if one applies.

4. Always call the getWorkflowTriggerRequirements tool before initiating the triggerWorkflow tool. Call List workflows if required to fetch the correct workflow id. Ask the user for all inputs before triggering the workflow.

5. Never fabricate data. If a field is not returned by a Docusign MCP tool, say so explicitly. Do not invent envelope IDs, recipient emails, statuses, dates, dollar amounts, or clause text.

6. Ask one clarifying question when required parameters are missing.

7. Response format. Keep responses brief, accurate, and visually scannable: lead with a one-line summary, then the detail. Use visual indicators - in place, at-risk, missing, pending.
```
- Say: "These instructions define the agent's operating rules. Rule 3: always check for a Workflow Builder workflow before sending an envelope. Rule 4: always call `getWorkflowTriggerRequirements` before `triggerWorkflow`. You will see both of these in action in Scenario B."

---

### 3.3 · Adding the MCP tool - what to say and watch for

**The path to add it:**
Tools tab → **+ Add a tool** → select the **Model Context Protocol** tab (not the default tab) → search **"Docusign Demo MCP"** → select **Docusign MCP Demo** → Add and Configure.

**Demo vs Production - explain this explicitly:**
> "There are two servers: Docusign MCP Demo, which connects to `apps-d.docusign.com`, and Docusign MCP, which connects to production. For this workshop, always use the Demo server. If you connect to production by mistake, you will not see the agreements we just ingested."

**What attendees see after adding:**
They should see 30+ tools listed - envelopes, templates, agreements, workflows, users. Point out the key ones:
- `getAgreementDetails` and `getAgreements` - these are what power the agreement intelligence in the next 30 minutes
- `triggerWorkflow` and `getWorkflowTriggerRequirements` - used in Scenario B
- `sendReminder`, `updateEnvelope` - used in Scenario C

**Common blocker: "Not Connected"**
If an attendee sees "Not Connected" next to the connector:
1. Click the dropdown next to Connection → **Create a new connection**
2. Log in with Docusign demo account credentials
3. Allow the requested access

If they run a prompt and get a Microsoft default connection error:
1. Click **Open Connection Manager**
2. Find the entry showing "Not Connected" → click **Connect** → Submit
3. Status changes to Connected → come back to the agent tab → click **Retry**

**Multiple accounts - check the default:**
Some attendees will have multiple Docusign accounts. The agent connects to the default. The first verify prompt ("List all my Docusign accounts") surfaces this. If they are on the wrong account, have them prompt: "Switch to account [account name/ID]."

**Activity map - how to use it:**
> "Turn the activity map on in the Test pane and keep it on for every prompt. It shows you which tool was called, what the inputs were, and what came back. If you run a prompt and there is no `tools/call` in the activity map, the agent answered from training data, not from Docusign. That is a problem - tighten the instructions and republish."

**Permissions - talking point:**
> "MCP does not give the agent any extra access. It respects the same permissions the user has in Docusign. If you cannot see a document in the Agreement Manager UI, the agent will not surface it either. Same access model, just a better interface."

**Iris does the heavy lifting - talking point:**
> "The agreement intelligence is not being generated at query time. Iris already extracted and structured all of this in Stage 2 - party names, renewal dates, payment terms, liability caps. The agent is just surfacing what Iris pre-processed. That is why it is fast, token-efficient, and consistent."

---

### Verify the connection - run before any scenario

Turn the **activity map On** in the Test pane first - keep it on for every prompt.

**P1:**
```
List all my Docusign accounts.
```
- Confirms OAuth is live and which account is active. Multiple accounts? Check which is default. Prompt: "Switch to account [name/ID]" to change.

**P2:**
```
List all my agreements.
```
- Should return the 11 agreements from Agreement Manager. Zero returned? Wrong environment (production instead of sandbox) or extraction still running.

**P3:**
```
List available Workflow Builder workflows.
```
- Should return the Fontara Renewal Order Form workflow. Not there? Workflow is in Draft - go to Agreements → Workflows → open → **Publish**.

Each prompt must show a `tools/call` entry in the activity map. No `tools/call` means the connection is not live - do not proceed to Scenario A until all three are green.

---

### Scenario A · Vendor Agreement Insights (~10 min)

**The story:** MarketPulse Dynamics wants a 10% price increase. Before responding, procurement needs to know exactly what's in place.

**A1 - Portfolio renewal view:**
```
Show me all upcoming renewals across my vendor agreements in the next 180 days.
```
- Portfolio-wide view across all vendors in one prompt - no spreadsheet, no paralegal

**A2 - Vendor account overview:**
```
For MarketPulse Dynamics, which agreements are active and in place today? List key details - value, renewal date, payment terms, and notice period.
```
- Iris extracted all of these in Stage 2 - the agent is surfacing structured data, not reading PDFs live

**A3 - Payment terms and renewal risk scan:**
```
MarketPulse Dynamics is proposing a 10% price increase on renewal. Pull the payment terms, renewal notice period, and termination-for-cause notice period from all active MarketPulse Dynamics agreements. Flag anything that is outside standard - payment terms beyond 30 days, or a renewal notice window under 90 days.
```
- "Flag anything outside standard" is a business rule in plain English - point out the agent applied it against extracted data

**A4 - Cross-vendor comparison:**
```
Compare MarketPulse Dynamics and Momentum Driver side-by-side on compliance posture and obligations. Show me what MarketPulse Dynamics is missing that Momentum Driver has in place.
```
- Two vendors, entire corpus, one prompt

> "This is what used to take a paralegal 2 days. The agent just did it in 10 seconds - grounded in the actual extracted clause text, not a guess."

---

### Scenario B · Workflow Builder Orchestration (~10 min)

**The story:** Procurement is cleared to renew at current price. They need the order form signed by the vendor.

**B1 - Build the deal math:**
```
Work out the renewal deal math: 50,000 unit batch size at $45 per unit with a 10% volume discount.
```
- Agent can calculate before triggering - good sanity check before committing to a workflow

**B2 - Initiate the renewal:**

Replace `[recipient email]` with a real email before running.
```
Initiate a renewal for the Clinical Trial Supply Agreement with MarketPulse Dynamics for 50,000 units at $45 per unit with 10% discount for a 1-year term starting August 1, 2026. Route it to [recipient email] at the vendor.
```
- Watch the activity map: agent calls `getWorkflowTriggerRequirements` before `triggerWorkflow` - that sequencing comes from instruction rule 4
- Content-filter error on B2: use a different recipient email (sandbox restriction) and retry

> "The agent called `getWorkflowTriggerRequirements` before triggering. That is instruction rule 4 at work - it never fires a workflow blind."

---

### Scenario C · Track Status (~5 min)

**C1 - Workflow status:**
```
What's the status of the MarketPulse Dynamics renewal workflow instance? Which step is it on, who needs to act next, and is anything blocked?
```

**C2 - Signature status on the vendor envelope:**
```
Has the recipient at MarketPulse Dynamics signed the renewal order form yet? When was it sent and has it been opened?
```

**C3 - Send a signing reminder:**
```
Send the MarketPulse Dynamics recipient a signing reminder through Docusign - use the existing envelope, don't create a new one. Then tell me when the envelope expires and what happens if it's not signed by then.
```
- Procurement never left the chat interface

> "They kicked off the renewal, tracked it, and nudged the vendor - all through natural language."

---

### 3.8 · Publish to Teams / M365 Copilot
- Channels → Microsoft 365 and Teams → Add channel → Publish
- "Now the same agent appears in Teams - wherever procurement already works."
- Note: tenant admin approval may be needed; allow propagation time

---

## Stage 4 · Agent Studio - Procurement Agent (10 min)

> ⚠️ **Agent Studio is in Early Access** - not yet enabled in the developer/demo accounts used for this workshop. Walk through this as a preview of the native Docusign agent experience. Announced at Momentum '26.

### Talk track - opening
> "Everything so far - Stage 3 - was the integration story: we brought Docusign into Microsoft Copilot Studio through MCP. Stage 4 is the native story. Agent Studio is Docusign's own builder and governance layer for agents, built directly inside IAM. Same agreement corpus, same Iris-extracted data, but the agent lives natively in Docusign and can be governed there."

### What Agent Studio adds (Momentum '26, Early Access)
- **Pre-built agents** for common agreement tasks: intake and triage, drafting and redlining, renewal management - you do not always start from a blank agent
- **Grounded in your context** - agents are built with natural language, grounded in agreement history, business policies, and internal playbooks
- **Deployed where work happens** - agents can be added as a step inside a Workflow Builder workflow, or run through Iris, with logged actions and human-in-the-loop approvals
- **Governance built in** - you control who can build an agent, what agreement data it can access, where it participates in the lifecycle, and how its actions are audited

### Walk through the flow (preview)
1. Agent Studio → Create a draft agent → paste the description
2. Name it **Fontara Procurement Agent**, paste the instructions
3. Show the test prompts - same procurement questions as Stage 3, running natively in Docusign

### Talk track - what to emphasise
> "One corpus, two paths. Stage 3 showed MCP - expose Docusign to any external AI client: Claude, Gemini, Microsoft Copilot, a custom app. Stage 4 is Agent Studio - build and govern the agent natively inside Docusign, with the approvals and audit trail enterprises need. Most teams will use both: MCP for reach into the tools people already use, Agent Studio for governed agents inside the agreement lifecycle. The agreement data you built in Stages 1 and 2 powers all of it."

---

## Closing (2 min)

### The pattern
> Ingest once → Extract with AI → Expose via MCP → Deploy agents everywhere

### Key messages to leave the room with
1. **Agreement Manager + CLI** = configuration as code. Repeatable across any client account.
2. **Iris extraction** = static PDFs become structured, queryable data. No manual review.
3. **MCP + Copilot Studio** = procurement answers in Teams and M365 Copilot, in plain English.
4. **Agent Studio** (Early Access) = native Docusign agent builder with governance and human-in-the-loop approvals, same corpus, no external platform.

---

## Troubleshooting quick-ref

| Issue | Fix |
|---|---|
| Agent returns "I don't see any agreements" | Reconnect MCP connector with sandbox credentials (`apps-d.docusign.com`) |
| Fields blank or partial in Agreement Manager | Click Re-analyze, wait 5 min |
| Workflow not appearing when agent queries | Go to Agreements → Workflows → open → click Publish |
| No `tools/call` in activity map | Confirm Generative orchestration is On; tighten instructions; republish |
| B2 content-filter error | Use a different recipient email |
| Agent in Teams not appearing | Confirm channel is enabled and submitted; may need tenant admin approval |

---

*For questions: amrit.prakash@docusign.com*
