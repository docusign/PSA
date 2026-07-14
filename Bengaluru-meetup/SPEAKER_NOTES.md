# Speaker Notes — Bengaluru Meetup: Docusign Manage Workshop
**Runtime:** ~65–75 min | **Audience:** Implementation-partner architects & developers + cross-functional business stakeholders

---

## Before the session

Attendees do ingestion (Stage 1), extraction (Stage 2), and agent setup (Stage 3) live — nothing to pre-run. Your checklist is just access and tools.

- **Your machine:** Node + npm installed, `@docusign/agreement-cli@1.1.0-beta` installed globally — run `docusign` to confirm it's on PATH
- **Demo account:** logged into `apps-d.docusign.com`, Agreement Manager enabled, CLI (open beta) access on the account
- **Workshop resources:** downloaded and unzipped — `workshop-resources/` folder ready with the manifest, training docs, and ingest contracts
- **Copilot Studio access:** Microsoft 365 / Copilot Studio environment ready to create a blank agent in Stage 3
- Have the lab page open: https://docusign.github.io/PSA/Bengaluru-meetup/2_Hands_on_Flow.html
- Have `apps-d.docusign.com` open in a second tab

---
## Stage 0 · Before you begin (5 min)

**Goal:** Set the scene — why agreements matter as data, not just documents.

### What to say
- "Fontara is a pharma/medtech company. Their procurement team manages hundreds of vendor contracts — MSAs, SOWs, NDAs — all sitting as flat PDFs."
- "Today nobody can answer: which contracts auto-renew next quarter? Which vendors have payment terms beyond 45 days? Every question means a human opening files one by one."
- "Over the next hour you'll change that. We're going to treat agreements as data — ingest them, extract intelligence from them with AI, and then query the whole corpus in plain English through an agent."

### Pattern to land
> Ingest once → Extract with AI → Expose via MCP → Deploy agents everywhere

### Prereqs check
- Audience should have Node + npm installed and the Agreement CLI ready
- If anyone is missing it: `npm i -g @docusign/agreement-cli@1.1.0-beta`
- Tick all 3 prereq checkboxes on the lab page — modal will auto-pop to unlock stages

---

## Stage 1 · Docusign CLI + Agreement CLI (15 min)

**Goal:** Show that agreement configuration and bulk ingestion is code — repeatable, version-controlled, partner-deliverable.

### Talk track — opening (say this before running the first command)
> "Right now, if you want to set up Agreement Manager for a client — define their agreement types, their custom fields, map everything together — you'd click through the UI, manually, for every account. That doesn't scale.
>
> What we're going to do instead is define all of that as a JSON manifest. Three agreement types, nine custom pharma fields, training documents, all of it. One file. And then we'll deploy it with a single CLI command.
>
> The same manifest you test in a dev account today? You hand it to the client, point it at production, run the same command. Done. No re-clicking, no re-configuring, no human error."

### Step by step

**1.1 — Authenticate**
```
docusign auth login
docusign auth test
```
- Browser-based OAuth. Each attendee logs into their own demo account.
- Expect: `Authentication is valid`

**1.2 — Scaffold the workspace**
```
mkdir ~/docusign-workshop && cd ~/docusign-workshop
docusign scaffold -w demo-workspace -p demo-project -f agreement-manager
```
- Creates the folder structure: `configs/`, `files/train/`, `files/test/`

**1.3 — Drop in the manifest & training docs**
```
curl -L https://github.com/docusign/PSA/raw/main/Bengaluru-meetup/workshop-resources.zip -o workshop-resources.zip && unzip -q workshop-resources.zip && rm workshop-resources.zip
cp workshop-resources/agreement-manager-manifest.json demo-workspace/demo-project/agreement-manager/configs/agreement-manager-manifest.json
cp workshop-resources/files/train/* demo-workspace/demo-project/agreement-manager/files/train/
```
```
cd demo-workspace && docusign agm get catalog
docusign agm upload --bypass
```
- `agm upload` creates fields, creates agreement types, maps fields, uploads training docs, triggers AI training — all in one command.
- AI training runs async — extraction results appear in the UI after a few minutes.

**1.5 — Bulk ingest**
```
cd ..
docusign agm ingest --directory workshop-resources/files/ingest --dry-run
echo "y" | docusign agm ingest --bypass --directory workshop-resources/files/ingest
```
- 4 contracts uploaded at once. "This is the legacy repository moment — not one file at a time."

### Talk track — what to emphasise (say this after `docusign agm upload` completes)
> "Everything you just saw — fields created, agreement types created, training uploaded, AI kicked off — that was one command. Not a ticket to the PS team, not an afternoon in the UI.
>
> This is the developer value story. Implementation time drops by over 40% compared to manual configuration. You can version-control this manifest in Git, run it through CI, promote it from dev to prod, replicate it across client accounts.
>
> What you're handing a client isn't just a configured Docusign account — it's a repeatable, auditable asset. That's the difference between a one-time implementation and a scalable practice."

---

## Stage 2 · AI Extraction in Agreement Manager (10 min)

**Goal:** Show static PDFs becoming structured, queryable data.

### What to say
- "Iris reads every ingested contract and populates the fields we defined in Stage 1."
- Navigate to `apps-d.docusign.com` → Agreements → Completed
- Show the 4 ingested contracts with their agreement types auto-applied
- Open one → show the right-hand extraction panel side-by-side with the PDF

### Fields to highlight
| Agreement type | Show this field | Why it matters |
|---|---|---|
| Clinical Trial Supply | `Pharma - Clinical Batch Size (units)` | Batch volume commitments |
| CRO Services | `Pharma - Total Study Budget (USD)` | Full CRO spend visibility |
| Medical Device Supply | `Pharma - FDA Device Classification` | Regulatory compliance at a glance |

### Standard fields
Also point out: Payment Terms, Governing Law, Renewal, Termination Notice — extracted automatically on top of custom fields.

### What to emphasise
> "Procurement now has payment terms, governing law, termination notice, and renewal dates extracted automatically — without any manual review — across the entire corpus. This feeds the agent in Stage 3."

---

## Stage 3 · MCP via Microsoft Copilot Studio (30 min)

**Goal:** Natural language queries against the whole vendor corpus. Show the "agent as procurement analyst" moment.

### Setup check before starting
You're running Stage 3 live alongside attendees — no pre-built agent. Everyone creates the blank agent and connects the Docusign MCP Demo connector together. Make sure before starting:
- Everyone has access to `copilotstudio.microsoft.com`
- Everyone is authenticated to their Docusign demo account (`apps-d.docusign.com`)
- The Fontara Renewal Order Form workflow was imported and **Published** at the end of 3.1
- Activity map is ON in the Test pane before running any prompts

---

### 3.1–3.3 · Setup (already done — just verify)
Run the 3 verification prompts to confirm the connection is live:
- "List all my Docusign accounts."
- "List all my agreements."
- "List available Workflow Builder workflows."

Each should produce a `tools/call` in the activity map.

---

### Scenario A · Vendor Agreement Insights (~10 min)

**The story:** MarketPulse Dynamics wants a 10% price increase. Before responding, procurement needs to know what's in place.

**Run in order:**

| Prompt | What to point out |
|---|---|
| A1: Renewals in 180 days | Portfolio-wide view — no spreadsheet needed |
| A2: MarketPulse Dynamics overview | Active agreements, value, renewal date, payment terms |
| A3: Payment terms & renewal risk scan | Flag anything off-standard — >30 day terms, <90 day notice |
| A4: Cross-vendor comparison | MarketPulse vs Momentum Driver — what's missing |

> "This is what used to take a paralegal 2 days. The agent just did it in 10 seconds — and it's grounded in the actual extracted clause text, not a guess."

---

### Scenario B · Workflow Builder Orchestration (~10 min)

**The story:** Procurement is cleared to renew — at current price. Need to get the order form signed by the vendor.

**Run in order:**

| Prompt | What to point out |
|---|---|
| B1: Deal math | Agent can calculate before triggering |
| B2: Initiate renewal | Calls `getWorkflowTriggerRequirements` first, then `triggerWorkflow` — correct sequencing |

> "Notice the agent called `getWorkflowTriggerRequirements` before triggering. That's the instruction at work — it never fires a workflow blind."

- If content-filter error on B2: use a different recipient email and retry

---

### Scenario C · Track Status (~5 min)

| Prompt | What to point out |
|---|---|
| C1: Workflow status | Which step, who needs to act, anything blocked |
| C2: Signature status | Has the vendor opened/signed the envelope |
| C3: Send reminder | Nudges stalled signer — without leaving chat |

> "Procurement never left the chat interface. They kicked off the renewal, tracked it, and nudged the vendor — all through natural language."

---

### 3.8 · Publish to Teams / M365 Copilot
- Channels → Microsoft 365 and Teams → Add channel → Publish
- "Now the same agent appears in Teams — wherever procurement already works."
- Note: tenant admin approval may be needed; allow propagation time

---

## Stage 4 · Agent Studio — Procurement Agent (10 min)

> ⚠️ **Agent Studio is coming soon** — not yet available in developer/demo accounts. Walk through this as a preview of what the native Docusign experience will look like.

### What to say
- "Stage 3 was the integration story — bring Docusign into Microsoft. Stage 4 is the native story — build the agent directly inside Docusign, no external platform needed."
- "Same corpus, same extracted data, different surface."

### Walk through the flow
1. Agent Studio → Create a draft agent → paste the description
2. Name it **Fontara Procurement Agent**, paste system instructions
3. Show the 5 test prompts (T1–T5) — same questions as Stage 3, native UI

### What to emphasise
> "One corpus. Two deployment paths. Copilot Studio for the Microsoft-first team. Agent Studio for the Docusign-native team. The agreement data built in Stages 1 and 2 powers both."

---

## Closing (2 min)

### The pattern
> Ingest once → Extract with AI → Expose via MCP → Deploy agents everywhere

### Key messages to leave the room with
1. **Agreement Manager + CLI** = configuration as code. Repeatable across any client account.
2. **Iris extraction** = static PDFs become structured, queryable data. No manual review.
3. **MCP + Copilot Studio** = procurement answers in Teams and M365 Copilot, in plain English.
4. **Agent Studio** = coming soon — native Docusign agent builder, same corpus, no external platform.

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
