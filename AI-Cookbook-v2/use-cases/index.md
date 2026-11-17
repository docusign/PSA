# Use cases

Each use case names the prompt or skill that runs it. Read-only unless noted.

Account executive

### Renewal in five minutes

Terms, dates and renewal type sit in different contracts. Before a call, that is a lot of digging.

**Runs:** Renewal prep prompt, renewal-brief skill  
**Outcome:** One brief with the gaps flagged

Sales leader and RevOps

### Chase only what is stuck

A weekly sweep finds envelopes waiting 3+ days, grouped by signer.

**Runs:** signature-chaser skill (weekly automation)  
**Outcome:** A short list with drafted nudges you approve

Procurement

### Check for an NDA before sending a new one

Duplicate NDAs waste legal time and slow vendor onboarding.

**Runs:** vendor-nda-gate skill  
**Outcome:** A yes or no with the existing dates

Procurement manager

### Catch auto-renewals before the notice window closes

Missed notice windows lock in renewals for another term.

**Runs:** renewal-radar skill (weekly automation)  
**Outcome:** A table sorted by renewal date with open notice windows

HR operations

### Get new-hire paperwork moving

Packets stall, and nobody knows who is holding them.

**Runs:** onboarding-orchestrator and policy-ack-tracker skills  
**Outcome:** Who needs to sign, and for how long

Legal operations

### Check a discount against other contracts

Before saying yes to a discount, you need to know whether another contract restricts it.

**Runs:** Clause check prompt, provision-sweep skill  
**Outcome:** The clauses that conflict, cited by agreement

CX and FINS

### Fix account openings before they bounce

Missing fields and stuck signers cause rework and delays for customers.

**Runs:** account-update-tracker skill  
**Outcome:** Stuck steps grouped by who holds them

Finance

### Quarter-end: nothing signed is missing

Revenue documents still open at quarter end delay recognition.

**Runs:** quarter-close-audit skill  
**Outcome:** Open order forms and SOWs, matched to executed agreements

Source: /PSA/AI-Cookbook-v2/use-cases/
