# RIG BUILD METHOD — the engineering engine for every product

**RULE, going forward, no exceptions.** Every product/service RIG builds runs this method.
It is the engineering counterpart to [RIG-DESIGN-METHOD](./RIG-DESIGN-METHOD.md) (the
sell/craft track). Both sit on the same root spine, **[IQRSQPI](./IQRSQPI-DOCTRINE.md)**
(design) / **[IQRSQPI-ENGINEERING](./IQRSQPI-ENGINEERING.md)** (build). The cure never
ships before the diagnosis is researched; nothing advances on a guess; proof or it
didn't happen.

> Born 2026-06-05 from the RIG App Studio build: every rule below is one the build
> actually used, and each was *earned* by a failure it now prevents.

## The build-track doctrines (each its own file)

| Doctrine | The one rule |
|---|---|
| [IQRSQPI-ENGINEERING](./IQRSQPI-ENGINEERING.md) | The spine: Intent→Questions→Research→Spec→Quality→Research→Plan→Implement, prototype-led loops, adversarial + iterative depth at every step and layer. |
| [PROOF-OR-IT-DIDNT-HAPPEN](./PROOF-OR-IT-DIDNT-HAPPEN.md) | Every claim is backed by a real command's output; "done" = a hard AND of all gates; verify the actual artifact, never the agent's report. |
| [ADVERSARIAL-VERIFICATION](./ADVERSARIAL-VERIFICATION.md) | Every gate is plant-failure verified — break what it guards, confirm RED, restore. A green that won't go red is theater. |
| [DETERMINISTIC-BEFORE-AGENTIC](./DETERMINISTIC-BEFORE-AGENTIC.md) | Generation is offline + byte-deterministic; AI fills only narrow named slots; the generator stays AI-free; outward artifacts ship DORMANT. |
| [GATE-D](./GATE-D.md) | No outward/irreversible action without explicit typed human approval; no bypass; an honest SKIP is never a fake PASS. |
| [REPRODUCIBILITY-AND-PINNING](./REPRODUCIBILITY-AND-PINNING.md) | Two honest tiers (byte-identical vs lockfile-pinned); exact pins + real @sha256 digests; secrets by reference, never inline. |
| [PHASE-DISCIPLINE](./PHASE-DISCIPLINE.md) | Build in dependency order; each phase: build → adversarial-verify → verify the real tree → commit on green; log every decision with its reversibility. |

## Which doctrine fires at which IQRSQPI step

| IQRSQPI step | Doctrines in force |
|---|---|
| **I / Q / R** Intent · Questions · Research | IQRSQPI-ENGINEERING (persona panel, prototype-led loops) |
| **S** Spec | DETERMINISTIC-BEFORE-AGENTIC · REPRODUCIBILITY-AND-PINNING (the spec declares the det/prob boundary + tiers) |
| **Q⇄R** Quality / re-research | ADVERSARIAL-VERIFICATION (red-team the spec) |
| **P** Plan | PHASE-DISCIPLINE (dependency-ordered phases + proof gates) · the ultra plan is earned here |
| **I** Implement | PROOF-OR-IT-DIDNT-HAPPEN + ADVERSARIAL-VERIFICATION on every phase; GATE-D guards every outward step; commit on green |

## The non-negotiables (one line each)
1. **Confidence is the gate, not the calendar.**
2. **No DRAFT silently becomes a decision** — it gets more research or escalates.
3. **Proof or it didn't happen** — the tree + the gate output are truth, not the report.
4. **Deterministic before agentic** — the floor is the moat.
5. **Gate D for everything outward/irreversible.**
6. **Adversarially verify every load-bearing claim before accepting it.**

---
*Version 1 · 2026-06-05 · the engineering track of the RIG method. Pairs with
RIG-DESIGN-METHOD. Globalized via `~/.claude/rules/rig-build-doctrine.md`.*
