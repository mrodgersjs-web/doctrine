# Contributing

## Bar

1. Public-boundary safe (no PII, secrets, client dumps, ToS-risk bots).
2. `rig-doctrine validate` clean (the corpus must satisfy the schema).
3. `ruff check src tests` clean and `pytest -q` passing.
4. README claims must match runnable commands.
5. Prefer small diffs with proof over large narrative refactors.

## Flow

1. Fork or branch from `main`.
2. Add doctrine to `intake/` (with front matter) or promote into `doctrines/`
   with a matching agent pack; add or adjust tests for code changes.
3. Run `rig-doctrine validate && ruff check src tests && pytest -q --cov=rig_doctrine`.
4. Open a PR with: what changed, how verified, boundary impact.

Do not merge doctrine because it sounds good. Merge it because it improves
agent behavior, build quality, user outcomes, or operating clarity and can be
verified.
