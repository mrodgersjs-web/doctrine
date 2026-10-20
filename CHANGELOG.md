# Changelog

Notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses
semantic versioning.

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
