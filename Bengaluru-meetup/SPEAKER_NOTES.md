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
- "Fontara is a pharma/medtech company. Their procurement team manages hundreds of vendor contracts - MSAs, SOWs, NDAs - all sitting as flat PDFs."
- "Today nobody can answer: which contracts auto-renew next quarter? Which vendors have payment terms beyond 45 days? Every question means a human opening files one by one."
- "Over the next hour you'll change that. We're going to treat agreements as data - ingest them, extract intelligence from them with AI, and then query the whole corpus in plain English through an agent."

### Pattern to land
> Ingest once → Extract with AI → Expose via MCP → Deploy agents everywhere

### Prereqs check
- Audience should have Node + npm installed and the Agreement CLI ready
- If anyone is missing it: `npm i -g @docusign/agreement-cli@1.1.0-beta`
- Tick all 3 prereq checkboxes on the lab page - modal will auto-pop to unlock stages

---

## Stage 1 · Docusign CLI + Agreement CLI (15 min)

**Goal:** Show that agreement configuration and bulk ingestion is code - repeatable, version-controlled, partner-deliverable.

### Talk track - opening (say this before running the first command)
> "Right now, if you want to set up Agreement Manager for a client - define their agreement types, their custom fields, map everything together - you'd click through the UI, manually, for every account. That doesn't scale.
>
> What we're going to do instead is define all of that as a JSON manifest. Three agreement types, nine custom pharma fields, training documents, all of it. One file. And then we'll deploy it with a single CLI command.
>
> The same manifest you test in a dev account today? You hand it to the client, point it at production, run the same command. Done. No re-clicking, no re-configuring, no human error."

### The four IAM Toolkit value points (land at least two of these)
- **Custom configuration** - extend Agreement Manager with custom agreement types and fields, defined as code in the manifest
- **Extraction testing** - validate Iris extraction accuracy against ground-truth values *before* deploying to production (`ds agm test`)
- **Multi-account deployment** - build the configuration package once, deploy it to multiple production accounts
- **Bulk ingestion via CLI** - ingest agreements plus metadata at scale from a local or network directory

> "This is the IAM Toolkit - it is in open beta. The command prefix is `docusign agm` or the short form `ds agm`. Everything we run today is one of those commands."

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

**1.1 - Authenticate**
```
docusign auth login
docusign auth test
```
- Browser-based OAuth. Each attendee logs into their own demo account.
- Expect: `Authentication is valid`

**1.2 - Scaffold the workspace**
```
mkdir ~/docusign-workshop && cd ~/docusign-workshop
docusign scaffold -w demo-workspace -p demo-project -f agreement-manager
```
- Creates the folder structure: `configs/`, `files/train/`, `files/test/`
- The CLI scaffolds the exact directory layout `agm upload` expects - you drop the manifest into `configs/` and training docs into `files/train/`, then run upload.

**1.3 - Drop in the manifest & training docs**
```
curl -L https://github.com/docusign/PSA/raw/main/Bengaluru-meetup/workshop-resources.zip -o workshop-resources.zip && unzip -q workshop-resources.zip && rm workshop-resources.zip
cp workshop-resources/agreement-manager-manifest.json demo-workspace/demo-project/agreement-manager/configs/agreement-manager-manifest.json
cp workshop-resources/files/train/* demo-workspace/demo-project/agreement-manager/files/train/
```
```
cd demo-workspace && docusign agm get catalog
docusign agm upload --bypass
```
- `agm get catalog` pulls the account's current standard and custom catalog before upload - `agm upload` reads both to avoid conflicts with existing types or fields.
- `agm upload` creates fields → creates agreement types → maps fields to types → uploads training docs → triggers AI training. All in one command.
- AI training runs async - extraction results appear in the UI after a few minutes.

**1.5 - Bulk ingest**
```
cd ..
docusign agm ingest --directory workshop-resources/files/ingest --dry-run
echo "y" | docusign agm ingest --bypass --directory workshop-resources/files/ingest
```
- `--dry-run` first: shows which files will be uploaded and what types they'll be classified as, without touching the account.
- Real ingest: 11 contracts uploaded (train + ingest folders combined). They appear in Agreement Manager → Completed within a few minutes as Iris indexes them.
- "This is the legacy repository moment - not one file at a time."

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

### What to show
- Navigate to `apps-d.docusign.com` → Agreements → Completed
- Show the 11 ingested contracts with their agreement types auto-applied (not "Miscellaneous")
- Open one → show the right-hand extraction panel side-by-side with the PDF
- Point at a custom field and its extracted value - "the manifest defined this, Iris filled it in"

> "Point to remember: this pre-processing is what makes Stage 3 fast. When the agent answers a question in a minute, it is not re-reading the contracts. It is querying structured data Iris already extracted. Faster, more token-efficient, and it respects the same permissions you have in Docusign.

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

### 3.1–3.3 · Setup - verify before running scenarios
Run the 3 verification prompts to confirm the connection is live:
- "List all my Docusign accounts."
- "List all my agreements."
- "List available Workflow Builder workflows."

Each should produce a `tools/call` in the activity map. If any prompt returns an answer with no `tools/call`, the connection is not live - debug before moving to Scenario A.

---

### Scenario A · Vendor Agreement Insights (~10 min)

**The story:** MarketPulse Dynamics wants a 10% price increase. Before responding, procurement needs to know what's in place.

**Run in order:**

| Prompt | What to point out |
|---|---|
| A1: Renewals in 180 days | Portfolio-wide view - no spreadsheet needed |
| A2: MarketPulse Dynamics overview | Active agreements, value, renewal date, payment terms |
| A3: Payment terms & renewal risk scan | Flag anything off-standard - >30 day terms, <90 day notice |
| A4: Cross-vendor comparison | MarketPulse vs Momentum Driver - what's missing |

> "This is what used to take a paralegal 2 days. The agent just did it in 10 seconds - and it's grounded in the actual extracted clause text, not a guess."

---

### Scenario B · Workflow Builder Orchestration (~10 min)

**The story:** Procurement is cleared to renew - at current price. Need to get the order form signed by the vendor.

**Run in order:**

| Prompt | What to point out |
|---|---|
| B1: Deal math | Agent can calculate before triggering |
| B2: Initiate renewal | Calls `getWorkflowTriggerRequirements` first, then `triggerWorkflow` - correct sequencing |

> "Notice the agent called `getWorkflowTriggerRequirements` before triggering. That's the instruction at work - it never fires a workflow blind."

- If content-filter error on B2: use a different recipient email and retry

---

### Scenario C · Track Status (~5 min)

| Prompt | What to point out |
|---|---|
| C1: Workflow status | Which step, who needs to act, anything blocked |
| C2: Signature status | Has the vendor opened/signed the envelope |
| C3: Send reminder | Nudges stalled signer - without leaving chat |

> "Procurement never left the chat interface. They kicked off the renewal, tracked it, and nudged the vendor - all through natural language."

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
