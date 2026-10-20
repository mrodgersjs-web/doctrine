# Changelog

Notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses
semantic versioning.

## [0.1.1] - 2026-10-19

### Added

- `tests/test_repo_hygiene.py`: 4 checks read from the files on disk that
  `.github/CODEOWNERS` assigns `*` to `@mrodgersjs-web`, that
  `.github/copilot-instructions.md` is non-empty, at most 8000 bytes and names a
  test command, that `README.md` carries a `github/actions/workflow/status` badge,
  the "Built by Mike Rodgers - rodgersintelligence.com" footer, a test command and
  only clones `mrodgersjs-web/doctrine`, and that every job under
  `.github/workflows/` sets `timeout-minutes` and never sets `continue-on-error: true`.

### Changed

- `.github/copilot-instructions.md` rewritten to 2373 bytes: what the repository is,
  the layout, the exact commands (`pip install -e '.[dev]'`, `ruff check .`,
  `rig-doctrine validate`, `pytest -q`, `bash scripts/smoke.sh`), conventions
  (conventional commits, a test for every change, no secrets, no machine paths) and
  the truth rule that every number in docs comes from a command run in this
  repository.
- `.github/workflows/ci.yml`: the `test` job now sets `timeout-minutes: 15`.
- `README.md`: the Quickstart comment now reads `# 33 tests`, the count printed by
  `pytest -q` after the hygiene tests landed, and the footer is the plain literal
  "Built by Mike Rodgers - rodgersintelligence.com".

### Verified

- Fresh venv `python3.12 -m venv`, `pip install -e '.[dev]'`, `ruff check .` clean,
  `pytest -q --cov=rig_doctrine` 33 passed, coverage 97 percent.

## [0.1.0] - 2026-10-19

### Added

- `rig_doctrine` Python package: loader, schema validator, and the
  `rig-doctrine` CLI (`list`, `show`, `validate`, each with `--json`).
- Test suite with per-rule unit tests, CLI tests, and a corpus-wide schema
  check that runs the validator over every bundled doctrine, intake and
  agent-pack file.
- Runnable example (`examples/validate_repo.py`), executed by the suite and CI.
- CI workflow on Python 3.10 to 3.13 running ruff, corpus validation, pytest
  with coverage, and the example. It replaces the smoke-only workflow.
- Packaging metadata (pyproject, `py.typed`), community files: this changelog,
  code of conduct, issue templates, pull request template, dependabot config.

### Fixed

- Broken relative links in `doctrines/RIG-BUILD-METHOD.md` and
  `intake/rig-app-studio-north-star-lock-intake.md`.
- A machine-specific path reference removed from `doctrines/RIG-BUILD-METHOD.md`.

### Changed

- README rewritten to describe the shipped package and the real corpus counts.
- SECURITY.md reporting address is now security@rodgersintelligence.com;
  CONTRIBUTING.md reflects the real test and lint commands.
