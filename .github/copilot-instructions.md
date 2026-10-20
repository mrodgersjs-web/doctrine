# Copilot instructions

## What this repo is

`doctrine` is the Markdown-first law layer for RIG agents: operating rules,
proof standards, approval gates, reusable agent packs, and the boundary between
unpromoted intake and promoted doctrine. The `rig_doctrine` Python package
loads that corpus and the `rig-doctrine` CLI validates it, so a broken link or
a malformed intake record fails CI instead of quietly rotting.

## Layout

- `doctrines/` - promoted canonical doctrine (15 texts plus a catalog).
- `intake/` - unpromoted source material, kept separate on purpose.
- `agent-packs/` - compact agent-facing instruction bundles.
- `proofpackets/` - doctrine and release evidence.
- `schemas/` - doctrine contract schemas.
- `src/rig_doctrine/` - package: `loader.py`, `model.py`, `validator.py`, `cli.py`.
- `tests/` - pytest suite: loader, validator, CLI, corpus, repo hygiene.
- `examples/validate_repo.py` - runnable example, executed by the suite and CI.
- `docs/` - architecture, evaluation strategy, usage, public boundary.
- `scripts/smoke.sh` - the smoke entry point.

## Commands

Run from the repository root in a virtual environment:

```bash
pip install -e '.[dev]'      # installs pytest, pytest-cov, ruff
ruff check .                 # lint
rig-doctrine validate        # whole corpus, exit 0 when clean
pytest -q                    # full test suite
pytest -q --cov=rig_doctrine # tests with coverage
bash scripts/smoke.sh        # smoke
```

## Conventions

- Conventional commit messages: `feat:`, `fix:`, `test:`, `docs:`, `ci:`, `chore:`.
- Every behavior change lands with a test that exercises it and passes on a clean install.
- Doctrine is executable guidance, not decorative prose. Promotion from `intake/` to `doctrines/` needs source evidence, agent instructions, tests, proof requirements, and a versioned path.
- No secrets, credentials, or private client material in any tracked file. No machine paths such as `/Users/...` or `~/Developer/...`.
- Never weaken the Gate-D, adversarial-verification, public-boundary, or reproducibility requirements while editing.

## Truth rule

Any number in docs, comments, or commit messages must come from a command run in
this repository, for example a doctrine count from `rig-doctrine list --kind
doctrine` or a test count from `pytest -q`. Quote the command and its output
rather than a memory of it.
