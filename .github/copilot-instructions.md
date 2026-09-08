# Copilot instructions

## Repository purpose

`doctrine` is the canonical, Markdown-first law layer for RIG agents: operating rules, proof standards, gates, reusable agent packs, and the intake-to-promotion boundary.

## Work map

- `doctrines/`: promoted canonical doctrine.
- `intake/`: unpromoted source material.
- `agent-packs/`: compact agent-facing instruction bundles.
- `proofpackets/`: doctrine and release evidence.
- `schemas/`: doctrine contract schemas.
- `scripts/`: repository smoke entry point.
- `docs/`: architecture, evaluation, and public-boundary guidance.
- `graft/`: generated context; read when needed and leave unchanged.

## Commands

No dependency bootstrap or application runtime is required. Test and smoke from the repository root:

```bash
bash scripts/smoke.sh
```

## Editing rules

- Treat doctrine as executable guidance, not decorative prose.
- Keep raw intake separate from promoted doctrine. Promotion needs source evidence, agent instructions, tests, proof requirements, and a versioned path.
- Apply `doctrines/GLOBAL-OPERATING-RULES.md` to non-trivial work.
- Keep credentials, secrets, private client material, and unsourced public claims out of the repository.
- Never weaken Gate-D, adversarial verification, public-boundary, or reproducibility requirements.
- Always run the smoke command before claiming done.
