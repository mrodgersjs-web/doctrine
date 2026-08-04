---
title: HIGGSFIELD — Cinematic Studio OS Doctrine
version: 1.0.0
source: BUILD CARD v2 — Higgsfield Cinematic Studio OS
status: promoted
---

# HIGGSFIELD — Cinematic Studio OS

**RULE.** A video generation request is a directorial brief, not a prompt. Route through the 24-skill dispatcher by intent (Seedance, Cinema Studio, GPT Image, marketing), run the pre-flight gate (schema verify → cost estimate → resolution matrix) before every paid job, and never submit without iteration discipline. Every credit spent was schema-checked and priced first.

## The laws

1. **Dispatcher routes by intent, not model.** The SKILL.md dispatcher reads the user's request and routes to the correct sub-skill — Seedance for long-form cinematic, Cinema Studio for tiered production, GPT Image 2 for stills, marketing studio for ads. The agent does not guess the model; the dispatcher knows the mapping.

2. **Pre-flight gate is mandatory before every paid generation.** Three steps, in order, no exceptions: (1) SCHEMA VERIFY — check model parameters (aspect ratio enum, duration range, media roles), (2) COST ESTIMATE — call `get_cost: true` before submitting, (3) GENERATE — only after cost approval. Skip step 2 and you burn credits on blind renders.

3. **Resolution Decision Matrix saves 60%+ of credit burn.** Draft at 480p (composition/motion check) or 720p (client preview). Final at 1080p (published asset). Never render a first-pass draft at 1080p — 480p costs 30% of 1080p per frame, 720p costs 50%. This is not optional frugality; it's the difference between 10 iterations being affordable vs. 3.

4. **MCSLA formula governs every shot.** Every shot specification contains four components: Motion (method), Camera (angle/lens/focal), Subject (character + emotion), Lighting (palette/source), Audio (SCELA sync). A shot without all five is incomplete — the dispatcher should flag it.

5. **Identity vs. Motion separation is the hard rule.** Character consistency requires splitting Identity (who — Soul ID, appearance, clothing) from Motion (what they do — gesture, expression, movement) in the prompt. Merge them and the character drifts across shots. This is the single most common failure mode.

6. **2.35:1 is an anamorphic style vocabulary, not a valid output ratio.** Output ratios are platform-bounded: 16:9, 9:16, 4:3, 3:4, 1:1. If a user requests 2.35:1, the pre-flight linter flags it as a gotcha and maps it to the corresponding anamorphic style within a valid ratio.

7. **Engine routing by capability, not cost per token.** Cloud Muapi gateway for heavy video (Seedance, Veo, Kling). Local sd.cpp for cheap image iteration. Self-hosted Wan2GP/LTX/CogVideoX-2B on M3-Pro-class hardware. Basic laptops cannot run video models. The resolution decision matrix is per-model.

## Why

The v1 build card wired one engine to one skill. v2 adds the four things that separate hobby output from a production studio: the 24-skill dispatcher (so the agent routes correctly without hand-holding), the Seedance director system (documenting 8 named render failures with counter-measures), exact engine spec tables (stopping the "which model" guess), and a pre-flight/cost-gate discipline layer that prevents credit burn. The 2.35:1 gotcha exists because the anamorphic style vocabulary leaks into output ratio requests — every studio has burned credits on renders that produced incorrect framing.

## How to apply

- SKILL.md at the repo root is the dispatcher. All 24 sub-skills are documented there with routing rules.
- Before generating: `python3 seedance_lint.py` — checks model validity, aspect ratio, duration, slop words, the 2.35:1 gotcha.
- Cost estimation: built into `seedance_lint.py`'s `estimate_cost()` — always call it before submitting.
- Resolution matrix: `resolution-matrix.md` — draft at 480/720, final at 1080.
- The full source repo from OSideMedia lives at `source-repo/` with 20+ sub-skill implementations.
- For iteration: apply the 6-Pass Diagnostic Sequence (Character Anchor Block → Two-Tool Refinement → Four Questions → Next-Shot Decision Tree).

## Gate criteria

| Gate | Threshold | Planted failure test |
|------|-----------|---------------------|
| Pre-flight before generation | All 3 steps executed | Submit without cost check → RED |
| Model validity | Model in MODEL_SPECS | Pass nonexistent model → UNKNOWN flag |
| Ratio validity | Ratio in model's valid set | Pass 2.35:1 → gotcha flag raised |
| Duration | <= model max_duration | Pass 20s to 10s-max model → RED |
| Slop words | Zero in prompt | Include "delve" → flagged |
| Resolution matrix | Draft < 1080p | Submit draft at 1080p → warning |