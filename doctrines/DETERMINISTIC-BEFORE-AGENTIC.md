# DETERMINISTIC BEFORE AGENTIC

**RULE.** The generator is **offline and byte-deterministic**; AI fills **only narrow,
named slots**. The generator core stays **AI-free** (the Z0 "no-AI zone") even when the
*output product* uses AI at runtime — **compile-time AI, never AI in the generator's
control/verification path**. Outward/ops artifacts are **generated DORMANT** (the
generate/operate split). Vibe-coding does not produce a robust app; the deterministic
floor is the moat.

## The laws
1. **Floor first.** Structure, wiring, schema/data layer, migrations, IaC, CI = 100%
   deterministic templates/AST. Same input ⇒ byte-identical output.
2. **AI only in declared slots.** Probabilistic generation is confined to small,
   pre-validated business-logic holes — never structure, never authz, never the gate.
3. **Output-AI ≠ generator-AI.** An AI-native product (chat/RAG/agent) ships a runtime AI
   client in its *output*; the *generator* that emits it imports no AI client. Lint Z0.
4. **Reproducible AI.** Cache completions (key = prompt+model+params → replay, don't
   re-roll) and property-test the slot; never wall-clock — use a content-derived stamp.
5. **Generate, don't operate.** Outward artifacts ship dormant; running them is a separate
   [Gate-D](./GATE-D.md) step.

## Why
The whole robustness thesis: a generator that "vibe-codes" the whole app is fragile and
unrepeatable. A deterministic floor + a thin AI slot is provable. The A2 AI-product proved
the boundary holds — 34 generator modules AI-free while the output genuinely runs an LLM.

## How to apply
- Schema-first single source of truth (OpenAPI/Prisma/Drizzle) so data/authz leave AI's blast radius.
- A no-AI lint over the generator Z0 modules (a real, plant-verified gate).
- Exclude the proof sidecar (`.rig/`) from the determinism hash; stamp with spec-hash, not time.

---
*Version 1 · 2026-06-05 · [RIG-BUILD-METHOD](./RIG-BUILD-METHOD.md).*
