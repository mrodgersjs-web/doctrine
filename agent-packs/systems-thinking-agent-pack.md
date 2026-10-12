# Systems Thinking Agent Pack

Load when a problem has **recurred** — same incident class twice, same retro item three
quarters running, a metric that snaps back after every push. Do not load for first-occurrence
bugs; those are [PHASE-DISCIPLINE](../doctrines/PHASE-DISCIPLINE.md) work.

## Pre-flight

- Read `doctrines/SYSTEMS-THINKING.md`.
- Establish recurrence before applying: this pack is for problems with a history, not incidents.
- Pull two readings of the straining stock separated by at least the system's natural delay.
  One reading is not evidence — law 4.

## The six-step protocol

1. Name the straining stock — units and current value.
2. Trace the draining loop — sign every arrow, label R or B, state which dominates.
3. Mark the delay in days — a number, not "eventually."
4. Locate the current attempt's rung honestly — usually rung 1.
5. Design exactly one intervention one rung higher.
6. Run two weeks, compare against everything the lower rung ever gave.

## The ladder (weakest → strongest)

| Rung | Lever | Engineering example |
|---|---|---|
| 1 | Numbers | New tool, tighter alert threshold, another lint rule |
| 2 | Structure | CI gate, default-deny config, pre-commit hook, protected time block |
| 3 | Information flows | Make a hidden level visible to the people who add to it |
| 4 | Rules / goals | Redefine done; change the target the system optimizes |
| 5 | The story | Change the unexamined assumption everything downstream grew from |

Rung 3 is the most underused and usually the best effort-to-effect trade.

## Archetype triage

| Symptom | Archetype | Move |
|---|---|---|
| Fix keeps getting reapplied; root capability weakening | Shifting the burden | Stop the symptomatic fix; rebuild root capacity |
| Fix works, then problem returns bigger | Fixes that fail | Price the return trip before shipping |
| Growth flattened; pushing harder makes it worse | Limits to growth | Relax the binding constraint, stop feeding the engine |
| Shared resource degrading, everyone acting reasonably | Tragedy of the commons | Publish the level; assign a refill rule |
| Metric swinging between extremes | Oscillation | Halve the correction, lengthen the review gap |
| Small upstream wobble, large downstream chaos | Bullwhip | Smooth the source, not the symptom |

## Domain sort before method (Cynefin)

Clear → checklist. Complicated → expert analysis. Complex → safe-to-fail probes. Chaotic → act,
stabilize, then analyze. Confused → sort first. Most recurring org problems are **Complex**;
shipping a Clear-world move (new tool, new template) at a Complex problem is the standard error.

## When NOT to use

- First occurrence of a bug — no pattern yet, go fix it.
- Genuine one-off external events with no internal loop.
- Time-critical incident response — stabilize first (Chaotic), analyze after.
- As a substitute for a root cause you can already name and fix cheaply today.

## Failure modes of this pack

- **Diagram theater.** A causal loop diagram that produces no valve setting with a number and a
  date is decoration. Kill it.
- **Rung inflation.** Claiming a rung-1 change is rung 3 because it has a dashboard. If nobody
  who *adds load* can see the level, it is not rung 3.
- **Skipping the delay number.** Without a written payoff date, the intervention gets judged at
  week two and cancelled.

---
*Version 1 · 2026-08-10 · doctrine: [`doctrines/SYSTEMS-THINKING.md`](../doctrines/SYSTEMS-THINKING.md).*
