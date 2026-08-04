---
title: MTP — Multi-Token Prediction and Speculative Decoding Doctrine
version: 1.0.0
source: BUILD CARD v2 — 3x–5x Faster Inference
status: promoted
---

# MTP — Multi-Token Prediction and Speculative Decoding

**RULE.** LLM inference is memory-bandwidth bound — verifying N candidate tokens costs the same as generating 1. Speculative decoding exploits this by having a small drafter propose N tokens for the target model to verify in a single forward pass. Always measure acceptance rate before enabling. Below alpha=0.5, spec decode hurts throughput — disable it.

## The laws

1. **Acceptance rate is the only metric that matters.** Track `spec_decode_draft_acceptance_rate` via Prometheus. If alpha < 0.70, the drafter is a bad match. If alpha < 0.50, speculative decoding is actively reducing throughput — fall back to standard decoding.

2. **Speedup formula is non-negotiable.** `E = (1 - alpha^(N+1)) / (1 - alpha)`. At alpha=0.80, N=5, you get ~3.7x before draft overhead. N=5 is the default start. Raise N to 7-8 if alpha > 0.80. Drop to N=3 if alpha < 0.50. Never guess — run the calculator.

3. **Draft model must share the target's tokenizer.** If tokenizers differ, every draft token is guaranteed rejected — alpha=0. Zero speedup. Same rule applies to MTP heads: they must be trained on the target model or they are pure overhead.

4. **Choose method by model support, not vibes.** Priority: native MTP heads (if model has them, e.g. Gemma 4, Qwen 3.6, DeepSeek) → EAGLE-3/P-EAGLE (highest known speedup, 3.5-5x) → draft model (widest support, 2-3x) → Medusa (task-specific) → n-gram/lookahead (zero VRAM, low-medium gain). If the model has native MTP, that's the first choice — not EAGLE.

5. **VRAM budget both models.** Target + drafter must both fit in GPU VRAM. Common: Llama 70B FP8 + Llama 1B = ~76 GB on H100. Quantize the drafter (FP8/INT4) to cut latency. Keep drafter at tensor-parallel=1. If VRAM is tight, use n-gram (zero extra model).

6. **Disable for batch > 32 or output < 50 tokens.** At high batch sizes, the GPU becomes compute-bound and the drafter is pure overhead. For very short completions (< 50 tokens), speculative decoding's setup cost exceeds gains. For embeddings or classifiers, never enable it.

7. **Validate quality parity.** Speculative decoding produces the same distribution as standard decoding — mathematically identical. But validate with lm-evaluation-harness on a representative benchmark set. If scores drop, the implementation is buggy, not the theory.

## Why

Decode is memory-bandwidth bound — the GPU spends most of its time loading weights from VRAM, not computing. Verifying N candidate tokens costs about the same as generating 1. This is not an optimization trick; it's a hardware reality. The acceptance rate formula is validated across multiple deployments (Gemma 4 hit 96.5% acceptance, Qwen 3.6 hit 2.64x on vLLM). The when-NOT-to-use rule exists because multiple production deployments have shipped spec decode without measuring acceptance rate and regressed throughput.

## How to apply

- Run `python3 scripts/acceptance-calculator.py` before deploying — it prints expected speedup for your alpha and N.
- Start with configs/ in `mtp-inference-studio`:
  - `vllm-draft-model.yaml` — production GPU, dominant choice
  - `vllm-eagle3.yaml` — highest speedup, needs EAGLE head checkpoint
  - `vllm-ngram.yaml` — zero extra model, for VRAM-constrained
  - `llamacpp-draft.yaml` — local/edge GGUF deployments
  - `sglang-eagle3.yaml` — prefix-heavy workloads (tree attention)
- Monitor: `curl http://localhost:8000/metrics | grep spec_decode` — watch acceptance rate and efficiency.
- Benchmark with `scripts/deploy-fleet.sh` — checks fleet node availability and recommends deploy path.
- For local deployments: llama.cpp + matched draft (same tokenizer) + `--draft-max 16`.
- For custom work: train an EAGLE-3 drafter on your traffic distribution using SpecForge or vLLM speculators.

## Gate criteria

| Gate | Threshold | Planted failure test |
|------|-----------|---------------------|
| Acceptance rate | alpha >= 0.70 | Inject bad drafter (alpha=0.4) → calculator shows < 1x |
| VRAM fit | Both models fit with 0.94 utilization | Compute VRAM sum, compare to GPU capacity |
| Quality parity | lm-eval scores within 1% of standard | Run eval with and without spec decode |
| Tokenizer match | Draft and target share tokenizer | Use different tokenizer → acceptance = 0 |
| Batch guard | Disabled if batch > 32 | Verify standard decoding fallback activates |