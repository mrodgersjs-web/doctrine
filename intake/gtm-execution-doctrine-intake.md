---
title: "Intake: GTM EXECUTION-DOCTRINE / THE RIG EXECUTION DOCTRINE"
source: "User-provided doctrine text in session context; original file name: GTM EXECUTION-DOCTRINE.md"
received: 2026-06-06
status: intake
promoted_to: null
---

# THE RIG EXECUTION DOCTRINE
### Anti-Drift Operating Law for Claude Code
**Owner:** Mike Rodgers · **Status:** ENFORCED · **Read this before any work in this repo.**

> This doctrine exists because of a specific, observed failure: a session that started as *"get a couple proposals out the door today"* and ended hours later with **nothing shipped** — the build outran the method, scope inflated turn over turn, agents reported failures that weren't real, and the context degraded into rework.

---

## Article 0 — The Session Contract

At the start of every session, before any tool call that changes a file, **state back in ≤5 lines:**

1. **THE ONE OBJECTIVE** — a single, shippable outcome.
2. **THE SCOPE CEILING** — exactly what is in, and the named things that are out this session.
3. **THE STOP LINE** — the last action you will take without asking.
4. **THE GOVERNING DOCTRINE** — which method/gates apply.
5. **THE FIRST STEP** — the single next action.

No objective stated = no build.

---

## Article 1 — One Objective Per Session

A session serves **one** objective. Anything mid-session that isn't that objective goes to **`BACKLOG.md`** with one line. No quick side-quests.

---

## Article 2 — Doctrine Is the Spine, Not the Polish

Before building **any** deliverable, **load the governing doctrine files and state which layers/gates apply.** For RIG sites that is the full stack: Layer 0 audience/named-recipient mind-map → GIVE↔THINK → Commitment Ladder → IQRSQPI per node → dual gate → DELIVER proof gate.

Tripwire: if writing content/code and the relevant doctrine is not loaded in this session, **STOP.**

---

## Article 3 — The Scope Ceiling Is Fixed

The scope set in Article 0 is **locked for the session.** It does not silently grow. "Make it better," "now do all verticals," and "also build the engine" are each a **NEW objective**.

**Pilot-first is mandatory.** Build **ONE** to lock the pattern, gate it green, get sign-off — *then* fan out.

---

## Article 4 — Verify the Tree, Not the Agent

An agent or workflow report is **not** ground truth. **The files on disk are.** After every agent/workflow run, inspect actual artifacts, run the build, check rendered output. A reported failure on work that exists on disk is a reporting failure.

---

## Article 5 — One Thing at a Time

Sequential by default. Parallelize only when proven safe. **Two-strike rule:** if an action fails twice, **STOP** and report — do not enter a retry loop.

---

## Article 6 — Checkpoint Before the Context Degrades

At ~50% context, or before any multi-hour build, write the handoff to disk (`HANDOFF.md`) and recommend a fresh session.

---

## Article 7 — Plan to Disk Before You Execute

Every non-trivial build gets a **written plan on disk, approved before execution.** No approved plan = no build.

---

## Article 8 — Honest Numbers, Zero Fabrication

Every figure on any deliverable is **real and cited, or omitted.** No invented stats.

---

## Article 9 — The Stop Line Is Sacred

**Deploy, send, push, publish, delete, pay, or any irreversible action requires explicit approval — every time.**

---

## Article 10 — Status Discipline

End every gate / major step with exactly:

- **DONE (verified on disk):** …
- **THE ONE DECISION I need from you:** …
- **NEXT SINGLE STEP:** …

---

## Drift Tripwires

- Building and governing doctrine isn't loaded → Article 2.
- About to do something outside stated objective → Article 1 / 3.
- Absorbed a "make it better / also do X" into current build → Article 3.
- About to retry a third time → Article 5.
- Declaring done/failed on an agent's word without checking disk → Article 4.
- Context feels cooked and starting something heavy → Article 6.
- About to deploy/send/push without a fresh yes → Article 9.

---

## Definition of Done

A deliverable is DONE when all are true:
1. It ran the governing doctrine as its spine, with gates passed and eyeballed.
2. Every number is real + cited.
3. It's the pilot proven first, or a fan-out of an already-proven pilot.
4. The state is checkpointed to disk.
5. It has stopped at the stop line awaiting explicit go for any side-effect.

Anything short is **in progress**, not done.
