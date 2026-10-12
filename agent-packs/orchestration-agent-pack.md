# Workflow Orchestration Agent Pack

Load when authoring, reviewing, or deploying a workflow definition — Kestra, Airflow, Dagster,
Temporal, n8n, or GitHub Actions. The mechanisms differ; the failure modes do not.

## Pre-flight

- Read `doctrines/WORKFLOW-ORCHESTRATION.md`.
- Identify every task whose **failure is the signal**. Those are the ones that break silently.
- Never write a plugin class from memory. Resolve it:
  ```bash
  gh api repos/kestra-io/kestra/contents/core/src/main/java/io/kestra/plugin/core/<pkg> \
    --jq '.[].name'
  ```
  Then add it to `CORE_CLASSES` in `examples/orchestration/validate_flows.py` with that path as
  the evidence.

## Core commands

```bash
# validate every example flow
pip install -r requirements.txt
python3 examples/orchestration/validate_flows.py

# full repo smoke (includes the validator)
bash scripts/smoke.sh

# refute the gate — required whenever a validation rule changes
sed -i.bak 's/core\.http\.Request/core.http.HttpRequest/' examples/orchestration/flows/uptime-check-alert.yml
bash scripts/smoke.sh   # must FAIL
mv examples/orchestration/flows/uptime-check-alert.yml.bak examples/orchestration/flows/uptime-check-alert.yml
bash scripts/smoke.sh   # must PASS
```

## Review checklist

- [ ] Every failure-signal task is tolerated (`allowFailed` or equivalent).
- [ ] Every notifier is gated on the **result** (`runIf`), not on control flow reaching it.
- [ ] Guards treat a missing value as unhealthy, not just a wrong value.
- [ ] The alert has been observed firing against a dead target at least once.
- [ ] No literal secrets, webhook keys, real hosts, or customer namespaces.
- [ ] Every plugin class resolved from source, not recalled.
- [ ] Triggers are in the definition, not in an external scheduler.
- [ ] Tasks are idempotent — safe to run twice.

## Failure modes to look for in review

| Symptom | Law | Fix |
|---|---|---|
| Monitoring flow has never paged | 4 | Point at a dead target; confirm it fires |
| Probe aborts the run | 1 | Tolerate the failure |
| Alerts on every healthy run | 2 | Gate the notifier on the result |
| Silent on total outage | 3 | `code is not defined or code != 200` |
| "Who changed this?" unanswerable | 5 | Move the definition into git |
| dev and prod as two namespaces | 6 | Namespaces organize; instances isolate |
| Key literal in a committed flow | 7 | Secret reference; rotate the key |
| Class path fails at runtime | 8 | Resolve from source; pin in the validator |

## When NOT to use

- A one-off personal automation with no on-call impact — the flows-as-code overhead is pure
  loss; author it in the UI.
- Choosing an engine on star count or plugin totals rather than on who fixes it at 3am.
- As a substitute for actually running the dead-target test. Nothing in this pack proves an
  alert fires.

---
*Version 1 · 2026-08-10 · doctrine: [`doctrines/WORKFLOW-ORCHESTRATION.md`](../doctrines/WORKFLOW-ORCHESTRATION.md).*
