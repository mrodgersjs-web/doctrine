# PROOF OR IT DIDN'T HAPPEN

**RULE.** Nothing is "done", "fixed", "green", or "working" until a **real command's
output** says so. Every load-bearing claim is bound to evidence: a regression result, a
gate exit code, an artifact hash. **"Done" = a hard AND of all required gates**, sealed
into a **ProofPacket** (`.rig/proofpacket.json`) that is hash-bound to the actual artifact.

## The laws

1. **Verify the artifact, not the report.** An agent (or a teammate, or yourself) saying
   "tests pass" is a hypothesis. Run the gate; read the real tree. When reports disagree
   (they will, under concurrency), the working tree + the command output are the only truth.
2. **A green must be reproducible by command.** If you can't paste the command and show its
   exit code / output, it isn't proven.
3. **"Done" is computed, not asserted.** `done = all(blocking_gates_pass)` — a hard AND,
   never a vibe. One RED blocking gate ⇒ not done.
4. **Hash-bind the proof.** The ProofPacket records the artifact hash + each gate's result;
   it self-verifies. A claim that floats free of the artifact it describes is not proof.

## Why
The RIG App Studio build repeatedly had subagents report different test counts (20 vs 21
vs 22) because they wrote concurrently — only re-running the regression on the real tree
revealed the truth. A "10/10 regression" turned out to be 8 stubs. The cure: never trust
a summary; run the gate yourself before you commit.

## How to apply
- Before committing any phase: run the proof gate (`<project> test/regression`), read the
  actual exit code + headline, confirm the real files exist.
- Emit a ProofPacket for full-stack/outward work; "done" is its computed hard-AND.
- In a report, lead with the command and its output, not the adjective.

---
*Version 1 · 2026-06-05 · [RIG-BUILD-METHOD](./RIG-BUILD-METHOD.md).*
