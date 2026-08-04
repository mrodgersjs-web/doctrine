---
title: "Intake: Paramount Phronema v2 Build Card"
source: BUILD CARD (v2 — 1000x) — Paramount Obsidian System as a Phronema Compiled Intelligence Studio on QNAP.md
received: 2026-06-05
status: promoted
promoted_to: doctrines/PHRONEMA-COMPILED-INTELLIGENCE.md
---

## Source summary

The build card defines a Phronema compiled intelligence studio running 24/7 on the QNAP spine, rendering through an Obsidian vault surface. The key architectural decisions:

1. Hot/cold data model with fast nodes (rig-256gb, rig-96gb, blackwell) + durable QNAP (88TB)
2. Evidence pipeline: raw → normalized → extracted_claims → promoted_signal → proposal
3. 70/30 deterministic/agentic floor enforced by compiler
4. 11-agent suite with ConductorAgent orchestrating daily 08:00 cycle
5. Skill crystallization: repeated successful patterns promote to deterministic assets
6. Deviation gates: median/generic, fake mechanism, unsupported claims, approval bypass, credential risk, audit gaps
7. ProofPackets with source_hash binding

## Key claims extracted

- v1 was passive vault. v2 is compiled runtime with provenance, gates, audit.
- The vault is a render surface, not a store.
- 70/30 floor: compiler refuses any phase below it.
- source_hash_required: every claim ties to a hashed source.
- AuditOfficer immutable; irreversible actions require Mike approval.

## Verification notes

Evidence pipeline implementation verified: QUEUED → RAW → NORMALIZED → EXTRACTED → SIGNAL → PROPOSAL all pass with adversarial planted-failure tests. ConductorAgent imports and runs full cycle. AuditOfficer enforces all 4 gates. ScrapeLedger tracks all 10 stages.