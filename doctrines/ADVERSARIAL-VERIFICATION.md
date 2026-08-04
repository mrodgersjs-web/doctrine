# ADVERSARIAL VERIFICATION (non-vacuity)

**RULE.** Every gate, test, and load-bearing claim must be **plant-failure verified**:
break the exact thing it guards, confirm it goes **RED**, then restore. A green that
won't go red under a planted failure is **theater**, not proof. Default to skeptic — try
to *refute* a finding/design/diff before you accept it.

## The laws
1. **Non-vacuity per gate.** When you add a check, prove it can fail: inject the violation
   it exists to catch, assert RED, restore — and keep the planted-failure as a permanent
   regression case so it can never silently rot back to vacuous.
2. **Red-team before build.** Specs, plans, and diffs get an adversarial pass (a panel of
   skeptics, distinct lenses) that tries to break them *before* code is written.
3. **Verify against ground truth, empirically.** Don't grade by inspection — run the build,
   boot the app, plant the failure, observe. Reports lie; the planted failure doesn't.
4. **Majority-refute kills a finding.** If independent skeptics can't break a claim, it
   survives; if they can, it's downgraded — never the reverse.

## Why
Every serious defect in the RIG App Studio build was caught this way, not by trusting a
pass: the "10/10 regression" that was 8 constant-returning stubs counting BLOCKED as pass;
the determinism gate that read green on a generator emitting *zero files* (empty-tree
hash); the `arm` verb that accepted a whitespace-padded approval; the load gate that
fake-FAILED on a missing script. Each invisible until someone planted the failure.

## How to apply
- New gate ⇒ write its planted-failure regression case in the same change.
- Before accepting a design/diff: run an adversarial panel; fold the fixes in.
- "It passes" is not done; "it passes, and I broke it and watched it fail" is.

---
*Version 1 · 2026-06-05 · [RIG-BUILD-METHOD](./RIG-BUILD-METHOD.md).*
