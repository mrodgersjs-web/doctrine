# PHASE DISCIPLINE

**RULE.** Build in **dependency order**, one coherent phase at a time. Every phase runs
the same loop: **build → adversarial-verify → verify the real tree → commit on green.**
Small, coherent commits. **Log every decision with its reversibility**; when a one-way
door must be decided with no human in the loop, **bias to the reversible option** and
record it for override.

## The laws
1. **Dependency order.** Contracts/schema → core substrate → features → operate lane →
   ship. Never build a layer on an unproven one (build the substrate first, prove it boots).
2. **One green gate per commit.** A phase is committed only when its proof gate is green
   *on the real tree* (per [PROOF-OR-IT-DIDNT-HAPPEN](./PROOF-OR-IT-DIDNT-HAPPEN.md)) and
   its planted-failure checks hold (per [ADVERSARIAL-VERIFICATION](./ADVERSARIAL-VERIFICATION.md)).
3. **Reconcile before commit.** Multiple writers (agents) drift — re-read the working tree,
   resolve stray/uncommitted files, run the gate, *then* commit. Stage only your phase.
4. **Decisions log.** Every fork is recorded in `decisions-log.md` with: the choice, the
   why, and **reversible? (yes/no)**. Autonomous one-way-door calls pick the reversible
   option and are flagged for the human to override.
5. **Never advance on red.** A failing gate stops the phase; fix or escalate — don't paper over.

## Why
The P0→P7 RIG App Studio arc held because each phase was committed only on a green real-tree
gate; the autonomous D1–D7 decisions were reversible-biased and logged, so they're the
human's to override; and "verify the real tree before commit" caught every concurrent-write
drift (mismatched test counts, a stray uncommitted `g05` file).

## How to apply
- Write the dependency-ordered phase plan at IQRSQPI's Plan step (the ultra plan).
- Per phase: implement → adversarial panel → run the gate on the real tree → commit on green.
- Keep `decisions-log.md` current; reconcile the tree before each commit; branch off the default branch.

---
*Version 1 · 2026-06-05 · [RIG-BUILD-METHOD](./RIG-BUILD-METHOD.md).*
