---
title: PHRONEMA — Compiled Intelligence Studio Doctrine
version: 1.0.0
source: BUILD CARD v2 — Paramount Obsidian Phronema
status: promoted
---

# PHRONEMA — Compiled Intelligence Studio

**RULE.** Intelligence is compiled, not collected. A Phronema studio runs a hot/cold evidence pipeline on a deterministic floor (>=70%), renders through an Obsidian vault surface, and seals every output in a ProofPacket. There is no "second brain" — there is a compiled runtime with provenance, gates, and audit.

## The laws

1. **Evidence pipeline, not scraped dump.** Every source passes through a multi-stage pipeline (QUEUED → RAW → NORMALIZED → EXTRACTED_CLAIMS → PROMOTED_SIGNAL → PROPOSAL). No source skips stages. No signal is promoted without a source_hash.

2. **70/30 deterministic floor.** At least 70% of compile-time operations are deterministic (templates, hash-verified extractors, state machines). No more than 30% is agentic/LLM. The compiler enforces this — a phase below 70% is refused.

3. **Source_hash_required.** Every claim, signal, and proposal is cryptographically bound to its source via SHA-256 prefix (16 hex chars). A claim without a source_hash cannot pass the deviation gate.

4. **Deviation gates guard every promotion.** A raw source does not automatically become a signal. At each promotion point (claim → signal, signal → proposal), a deviation gate checks: is this median/generic? fake mechanism? unsupported? bypassing approval? The gate must be adversarially verifiable — prove it goes RED under a planted violation.

5. **Immutable AuditOfficer.** The AuditOfficer is a code object, not a person or config file. It appends-only logs every check. Its immutability is provable: the same input always produces the same log entries. Irreversible actions (payments, credential changes, sensitive writes) require Mike's typed approval — the officer blocks without it.

6. **Observation vault as render surface.** The vault does NOT store intelligence. It displays it: daily focus dashboard, scrape ledger, signal feed, capability map health. The intelligence lives in the compiled evidence pipeline. The vault is a terminal, not a database.

7. **Skill crystallization.** When a pattern works repeatedly (source connector, claim extractor, anomaly classifier), promote it from agentic to deterministic. Track the deterministic ratio over time — it must trend up.

## Why

The build card v1 was an Obsidian vault fed by a scraper — passive, no gates, no provenance. v2 makes the vault a render surface for a compiled runtime that runs 24/7, gates every promotion, and self-improves by crystallizing skills. The 70/30 floor exists because every serious defect found during development was invisible to a system that couldn't fail RED under a planted violation. The source_hash rule exists because a claim without provenance is indistinguishable from hallucination.

## How to apply

- Start with `studio.yaml` declaring sources, risk level, freshness windows, and agent calibration.
- Implement the evidence pipeline before any agent: `raw → normalized → extracted_claims → promoted_signal → proposal`.
- Each pipeline stage is a separate Python class/module with its own adversarial planted-failure test.
- The ConductorAgent orchestrates the daily 08:00 cycle — it does not create intelligence, it dispatches the deterministic pipeline and collects ProofPackets.
- Every source gets a ledger row tracking its stage. Render the ledger as markdown for Obsidian consumption.
- Before promoting anything to "1000x": get it running (service up, pipeline executing), wire to RIG toolchain (cron, `rig`, `gh`), add self-healing, add tests, then document with a ProofPacket. Not the reverse order.

## Gate criteria

| Gate | Threshold | Planted failure test |
|------|-----------|---------------------|
| Evidence quality floor | All claims >= 0.70 confidence | Inject 0.2 confidence → RED |
| Source hash required | Every signal has source_hash | Omit source_hash field → RED |
| 70/30 deterministic floor | Deterministic >= 70% | Test with 50/50 split → RED |
| Deviation gate | confidence >= 0.70 | Pass 0.3 confidence → RED |
| AuditOfficer immutable | Log is append-only | Verify same input = same output |
| ProofPacket seal | Proof self-verifies via hash | Modify proof → hash mismatch → RED |