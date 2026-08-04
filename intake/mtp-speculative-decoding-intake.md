---
title: "Intake: MTP + Speculative Decoding v2 Build Card"
source: BUILD CARD v2 — 3x–5x Faster Inference MTP + Speculative Decoding.md
received: 2026-06-05
status: promoted
promoted_to: doctrines/MTP-SPECULATIVE-DECODING.md
---

## Source summary

Executable playbook for 3x-5x faster LLM inference using MTP and speculative decoding. Key architectural decisions:

1. Speedup formula: E = (1 - alpha^(N+1)) / (1 - alpha)
2. Method tiers: MTP native > EAGLE-3 > draft model > Medusa > n-gram
3. VRAM: both models must fit, quantize drafter to FP8/INT4
4. When NOT to use: batch > 32, output < 50 tokens, embeddings
5. 30 open-source solutions mapped across 5 categories
6. Monitoring via Prometheus spec_decode metrics

## Key claims extracted

- Decode is memory-bandwidth bound (verified by formula)
- At alpha=0.80, N=5, ~3.7x before draft overhead
- Below alpha=0.50, spec decode hurts throughput
- Output is mathematically identical to standard decoding
- Gemma 4 hit 96.5% acceptance on MTP

## Verification notes

Acceptance calculator verified: all 5 cases produce correct values. Adversarial test passes (alpha=0.4,N=3,overhead=0.7 = 0.96x). 5 copy-paste configs written and validated.