---
title: Workflow Orchestration — Failure Paths, Flows as Code, Engine Choice
version: 1.0.0
source: kestra-io/kestra (27,685★) · kestra-io/plugin-github · kestra-io/kestra-flows-template · Zie619/n8n-workflows (56,010★; 4,343 workflows / 365 integrations) · "Getting Started with Kestra" — Learn Linux TV, 2026-05-14 (56 min, sponsor-disclosed)
status: promoted
---

# Workflow Orchestration — Failure Paths, Flows as Code, Engine Choice

**RULE.** An orchestrator is judged by what it does when a task **fails**, not by what it does
when everything works. Three properties decide that: the failure path must actually execute,
the definition must be reviewable and revertible, and the artifact must be workable by whoever
holds the pager. Everything else — plugin counts, star counts, canvas aesthetics — is
secondary.

## The laws

1. **A probe that aborts cannot alert.** Any task whose *failure is the signal* must be marked
   tolerated so execution reaches the notifier. Default engine behavior is to abort the run on
   task failure, which means the naive monitoring flow goes silent exactly when it matters —
   and its silence is indistinguishable from health. In Kestra: `allowFailed` on the probe.

2. **Gate the alert on the result, not on reaching the line.** Tolerating the failure is half
   the fix; without a condition, the flow now alerts on every healthy run and gets muted within
   a week. In Kestra: `runIf` on the notifier.

3. **Absence is unhealthy.** Write the guard so a *missing* result alerts.
   `runIf: "{{ outputs.probe.code != 200 }}"` can skip when the endpoint refuses the
   connection, DNS fails, or the request times out — dropping the loudest possible outage.
   Correct: `code is not defined or code != 200`.

4. **An untriggered failure path is assumed broken.** A green run against a healthy target
   proves nothing. Point the flow at a guaranteed-dead target, confirm the alert fires, and
   keep that run as a permanent regression case. This is
   [ADVERSARIAL-VERIFICATION](./ADVERSARIAL-VERIFICATION.md) applied to operations: plant the
   failure, observe red, restore.

5. **The definition lives in git; the UI is for observing.** A flow authored in a web canvas
   has no diff, no review, no rollback, and no answer to "who changed this and why." Author in
   an editor, land through a PR, deploy from CI.

6. **Namespaces organize; they do not isolate.** A namespace is a folder that sorts flows by
   project. Same instance means same database, same workers, same blast radius, same
   credentials. The upstream Terraform template says outright that namespace-only dev/prod
   separation is not recommended for production — while doing it for demonstration. Do not let
   the convenience become a claim about isolation.

7. **Secrets are referenced, never inlined.** Anything literal in a committed flow is in git
   forever, in every clone and fork. A committed webhook key is not a leaked password — it is a
   publicly callable trigger for a production workflow. Reference `{{ secret('NAME') }}`;
   rotate on exposure.

8. **Never write a plugin class you did not resolve.** Fully-qualified class paths are the
   single easiest thing to hallucinate — `io.kestra.plugin.core.http.HttpRequest` looks correct
   and does not exist. It parses, deploys, and fails at runtime on the unhappy path. Resolve
   from the upstream source tree, then pin it in a validator so a wrong path goes red in CI.

9. **Idempotency is table stakes.** Every task must be safe to run twice; that is what makes
   retries and backfills possible instead of dangerous.

10. **Explicit data flow beats implicit state.** Pass values through the graph. Coordinating
    through a shared file or a global is how you get a race you cannot reproduce.

11. **Triggers belong in the definition.** Schedules, webhooks, and flow-to-flow triggers are
    part of the versioned artifact, not an external scheduler that drifts out of sync.

12. **Choose the engine by who fixes it at 3am.** An engineer with a diff and a git history →
    declarative and code-first. Whoever built it, in the UI, by looking at the canvas →
    node-based. Both are legitimate; the mismatch between artifact and on-call model is what
    hurts.

## Why

The failure mode this doctrine exists to kill is the monitoring flow that has never been
observed firing. It passes review, it passes its happy-path test, and it is silent on the night
it is needed — because the probe it depends on aborts the execution before the alert task runs.
The bug is invisible in testing by construction: you cannot see it without deliberately breaking
the thing being monitored.

Laws 5–7 exist because the second failure mode is organizational rather than technical. A
workflow estate authored in a UI becomes shadow infrastructure — production behavior with none
of production's controls — and the discovery moment is always an incident where nobody can say
what changed.

Law 8 is new pressure from AI-assisted authoring specifically. Plugin FQCNs are exactly the
shape of token an LLM will confidently reconstruct, and YAML gives no compile step to catch it.
The mitigation is deterministic and cheap: pin the known class set and validate in CI. That is
[DETERMINISTIC-BEFORE-AGENTIC](./DETERMINISTIC-BEFORE-AGENTIC.md) — the AI writes the flow, a
non-AI gate decides whether it is real.

## How to apply

For any new or reviewed flow:

1. Identify every task whose failure is a signal. Mark it tolerated; gate its notifier on the
   result; write the guard so absence alerts.
2. Point it at a dead target once and watch the alert fire. Keep the run.
3. Put the definition in git. Deploy from CI, not from the canvas.
4. Replace every literal credential with a secret reference. Rotate anything already committed.
5. Resolve every plugin class from source and pin it in the validator.
6. Run the validator in CI, then break a class path and confirm the validator goes red.

Reference implementation with three runnable flows and the pinned-class validator:
[`examples/orchestration/`](../examples/orchestration/).

## Cost, stated honestly

Flows-as-code is not free. Terraform-wrapped definitions mean a plan/apply cycle instead of
clicking save, and iteration slows. For a personal automation that restarts a service, that
overhead is pure loss — author it in the UI and move on. The cost pays back where a broken flow
wakes somebody up, where more than one person edits, or where you need to answer what changed
last Tuesday. Adopt per flow at that threshold; "everything in Terraform from day one" is how
teams end up with an unmaintained `environment/` directory and the real flows in the UI.

---
*Version 1 · 2026-08-10 · pairs with [ADVERSARIAL-VERIFICATION](./ADVERSARIAL-VERIFICATION.md) and [DETERMINISTIC-BEFORE-AGENTIC](./DETERMINISTIC-BEFORE-AGENTIC.md) · agent pack: [`agent-packs/orchestration-agent-pack.md`](../agent-packs/orchestration-agent-pack.md) · examples: [`examples/orchestration/`](../examples/orchestration/).*
