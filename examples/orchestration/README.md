# Orchestration examples

Runnable proof for [`doctrines/WORKFLOW-ORCHESTRATION.md`](../../doctrines/WORKFLOW-ORCHESTRATION.md).
Three Kestra flows and the validator that keeps them honest.

```bash
pip install -r requirements.txt          # from repo root
python3 examples/orchestration/validate_flows.py
```

Expected: `3 flow(s) valid`.

## Flows

| Flow | Demonstrates | Laws |
|---|---|---|
| [`uptime-check-alert.yml`](flows/uptime-check-alert.yml) | `allowFailed` + `runIf`; a missing status code is treated as an outage | 1–3 |
| [`subflow-fanout.yml`](flows/subflow-fanout.yml) | Parallel fan-out to a reusable subflow; `transmitFailed` stops the parent reporting green over a failed child | 5, 10 |
| [`webhook-triggered.yml`](flows/webhook-triggered.yml) | Event-driven entry; webhook key via secret reference | 7, 11 |

All flows target synthetic endpoints (`example.com`) and are validated, not executed.

## The validator

`validate_flows.py` enforces four things:

| Check | Catches |
|---|---|
| YAML parses | Indentation and quoting errors |
| `id`, `namespace`, `tasks` present | Flows that cannot deploy |
| Task/trigger ids unique | Silent collisions, unreferenceable outputs |
| Plugin class is known | **Hallucinated or misremembered class paths** (law 8) |

`CORE_CLASSES` is pinned from the Kestra source tree
(`core/src/main/java/io/kestra/plugin/core`), not from recall. The tree walk is recursive
because tasks nest — a bad class inside a `Parallel` or an `If` branch is precisely where a
shallow check misses it.

## Prove the gate is real

Per law 4, a gate that has never been observed failing is decoration:

```bash
sed -i.bak 's/core\.http\.Request/core.http.HttpRequest/' examples/orchestration/flows/uptime-check-alert.yml
bash scripts/smoke.sh     # FAILS: unknown core class 'io.kestra.plugin.core.http.HttpRequest'
mv examples/orchestration/flows/uptime-check-alert.yml.bak examples/orchestration/flows/uptime-check-alert.yml
bash scripts/smoke.sh     # PASS again
```

Verified at authoring time for a top-level task, a task nested inside `Parallel`, and tasks in
both branches of an `If` — all three go red.

## What it does not check

- Plugin **properties** — a valid class with a misspelled option still passes.
- Non-core (`io.kestra.plugin.<vendor>.*`) class existence; only FQCN shape is checked.
- Runtime behavior. Nothing executes; a logically wrong flow that parses is green.

Structural validity is a floor. The behavioral claim in law 4 is verified by pointing a flow at
a dead target against a live engine — deliberately a human step.
