# RIG Doctrine Repo Agent Instructions

This repo is the canonical doctrine layer for RIG.

When working here:

- Treat doctrine as executable operating guidance, not prose decoration.
- Do not claim a doctrine is v10 unless it has source evidence, an agent pack, tests, proof requirements, and a versioned release path.
- Keep raw intake separate from promoted doctrine.
- Prefer small, verifiable doctrine packs over broad unsourced essays.
- Every non-trivial change should include a clear objective, changed surfaces, verification command, and proof path.
- Do not include credentials, private client material, or machine-specific secrets.

## Global operating doctrine

The repository now treats `doctrines/GLOBAL-OPERATING-RULES.md` as always-on agent guidance.

For all non-trivial work, apply the doctrine stack in order.

### Design / conversion track

1. **Audience & Intent Foundation** — establish who lands, why they land, persona share, confidence grade, and kill-condition from evidence.
2. **GIVE↔THINK** — map what is given and what the recipient thinks beat by beat before design or implementation.
3. **Commitment Ladder** — escalate asks only as fast as the THINK-state earns them; proof precedes ask.
4. **IQRSQPI** — run Intent → Questions → Research → Spec → Quality⇄Research until dry → Plan → Implement for every meaningful node/component.
5. **27-Persona Panel** — gate craft, performance, accessibility, copy, motion, positioning, and system quality.
6. **Buyer Panel** — gate sales intent; beautiful-but-won't-book still fails.

### Build / engineering track

1. **RIG Build Method** — every product/service uses the engineering counterpart to the design method.
2. **IQRSQPI Engineering** — run the spine per step/layer, with prototype-led loops and adversarial red-team.
3. **Proof or It Didn't Happen** — no done/fixed/green/working claim without real command output, gate result, or artifact hash.
4. **Adversarial Verification** — plant-failure verify every gate and load-bearing claim.
5. **Deterministic Before Agentic** — deterministic substrate first; AI only in narrow named slots; generator control/verification stays AI-free.
6. **Gate-D** — no outward or irreversible action without exact typed human approval; SKIP/UNAVAILABLE is never a fake PASS.
7. **Reproducibility & Pinning** — claim only the tier proven; exact pins, real digests, secrets by reference.
8. **Phase Discipline** — build in dependency order; build → adversarial-verify → verify real tree → commit on green.

Agent rule: if a user request conflicts with these doctrines, flag the conflict and propose a compliant path instead of silently violating the doctrine stack.

## Repository quick reference

The repository is Markdown-first; no dependency bootstrap or application runtime is required.

- `doctrines/`: promoted canonical doctrine.
- `intake/`: unpromoted source material.
- `agent-packs/`: compact agent instructions.
- `proofpackets/`: doctrine and release evidence.
- `schemas/`: doctrine contracts.
- `scripts/`: repository smoke entry point.
- `docs/`: architecture, evaluation, and public-boundary guidance.
- `graft/`: generated context; read when useful and preserve unchanged.

Test and smoke from the repository root:

```bash
bash scripts/smoke.sh
```

Always run the smoke command before claiming done.
