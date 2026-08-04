# GATE-D — no outward action without human approval

**RULE.** No **outward or irreversible** action happens without **explicit, typed human
approval**. Outward = deploy, push, publish, send (email/social/message), payment,
destructive command, private-data export, public exposure. The approval is an **exact
typed phrase** (`APPROVE <run_id>`) — **no `--yes` / `--force` / env / non-interactive
bypass**. An honest **SKIP / UNAVAILABLE is never a fake PASS**.

## The laws
1. **Generate dormant; arm separately.** Outward artifacts (deploy workflows, IaC) ship
   inert (`workflow_dispatch` only + a fail-closed `if armed` gate). The only path to
   outward is a distinct **arm** step that requires the typed approval.
2. **No bypass, exact match.** The approval phrase matches exactly (no trailing-space
   leniency). There is no flag/env that skips it. Prove zero outbound until armed.
3. **Skip ≠ pass.** A gate that can't run (no Docker, no k6) returns a distinct
   non-pass status that **blocks** "done" — it never silently counts green.
4. **Stop and ask.** Before any outward/irreversible action not covered by an approved
   runbook, halt and get the human's go. Approval in one context doesn't extend to the next.
5. **LAN-first, record the path.** Outward/control-plane calls use local endpoints first
   (RIG comms doctrine); record the path taken in the ProofPacket/handoff.

## Why
RIG App Studio emits a full deploy bundle but arms nothing; a socket trap proved zero
outbound across generate→arm. The adversarial pass caught a whitespace-padded approval
that *would* have armed — fixed to exact-match. This is the rule that keeps a generator
from becoming a foot-gun.

## How to apply
- Emit ops/deploy artifacts DORMANT; build an `arm` verb gated on a typed approval, no bypass.
- Treat push/deploy/send/payment as Gate-D — confirm with the human first.
- Report what was skipped honestly; never dress a skip as a pass.

---
*Version 1 · 2026-06-05 · [RIG-BUILD-METHOD](./RIG-BUILD-METHOD.md).*
