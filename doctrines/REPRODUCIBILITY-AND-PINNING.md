# REPRODUCIBILITY & PINNING

**RULE.** Reproducibility is **two honest tiers**, and you never claim a tier you can't
prove: **Tier 1 byte-identical** (frontend / deterministic templates — hash-checked) and
**Tier 2 lockfile-pinned + version-stamped** (backend / AI slots — never claimed
byte-identical). **Exact pins only** (no `^`, `~`, `latest`). Base images pinned by
**real `@sha256` digests**. **Secrets by reference, never inline.**

## The laws
1. **Tier honesty.** Tier-1 = same input ⇒ identical bytes, proven by a tree hash. Tier-2
   = pinned deps + a version stamp + property/behavioral tests. Calling Tier-2 "byte-
   identical" is a lie that the determinism gate must reject.
2. **Exact pins.** Dependencies pin to exact versions. No floating ranges/tags. A loose
   pin is a non-deterministic build waiting to happen.
3. **Real digests.** Base images resolve to a real multi-arch `@sha256` (resolve once via
   `docker buildx imagetools inspect`, pin it, then generate offline). No placeholder
   `@sha256:000…`.
4. **Secrets by reference.** Generated source contains secret *names* (`.env.example`
   keys-only, empty RHS), resolved from env/vault at runtime, fail-closed on absence —
   never a literal value, never in a log.
5. **Stamp, don't timestamp.** Use a content-derived stamp (spec hash), never wall-clock,
   so docs and artifacts stay reproducible. Emit a stack+version manifest for diffable regen.

## Why
The build's "byte-identical" `output_hash` was secretly salted by uuid+wall-clock until a
double-build exposed it; a "loose pin" alarm turned out to be a comment; the base-image
digest shipped as all-zeros until resolved for real. Tier honesty + exact pins are what
make "deploys + runs reproducibly" true instead of asserted.

## How to apply
- Hash-check Tier-1; lockfile + stamp + property-test Tier-2; the determinism gate enforces both.
- Grep generated deps for `^`/`~`/`latest` (zero); grep for secret literals (zero).
- Resolve + pin real base digests; exclude `.rig/` from the hash.

---
*Version 1 · 2026-06-05 · [RIG-BUILD-METHOD](./RIG-BUILD-METHOD.md).*
