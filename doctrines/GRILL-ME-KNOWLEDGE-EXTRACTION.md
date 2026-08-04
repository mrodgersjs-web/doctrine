---
title: GRILL-ME-PRO — Knowledge Extraction Doctrine
version: 1.0.0
source: BUILD CARD v2 — Grill Me Pro
status: promoted
---

# GRILL-ME-PRO — Knowledge Extraction

**RULE.** Knowledge locked in someone's head is zero value. Knowledge written to a file is single-use. Knowledge embedded in a versioned, tested, self-improving skill is the asset. The loop is: interview → checkpoint → propagate → evaluate → commit. Until every gap is closed, every decision has rejected alternatives documented, and related skills are updated, the loop is NOT done.

## The laws

1. **One question at a time, always with a recommended answer.** The interviewer asks a single question, provides their own recommended answer first, and waits for the human to confirm, correct, or reject. Asking two questions at once or asking without a recommendation is a violation. The human answers; the interviewer does not fill silence.

2. **Demand specificity — reject vague terms.** "As needed", "regularly", "appropriate", "standard practice", "handle based on priority" are not acceptable answers. The interviewer must flag each occurrence and ask for an exact number, name, or threshold. "Regularly" becomes "every 6 hours". "As needed" becomes "when error rate exceeds 5%".

3. **Explore the codebase before asking the human.** If a question can be answered by reading existing files, grepping for patterns, or checking git history, do that instead of asking. The human is the last resort for knowledge, not the first. Document what was found and only escalate if gaps remain.

4. **Checkpoint every 2-3 answers, never lose progress.** After every 2-3 answers, write a checkpoint file to `brainstorm/<topic>.md`. Every checkpoint captures: algorithm/approach, key decisions (with rejected alternatives), Q&A log, highlights, and open gaps. Each checkpoint is a valid standalone document — a session can resume from any checkpoint.

5. **Progressive disclosure — stay token-efficient.** Do not load every reference file at the start. Pull detailed reference files only when the relevant decision branch is active. Use strategic compaction at logical breakpoints (after discovery phase, before propagation phase). The active context stays lean so the interview remains sharp deep into a long session.

6. **Propagation is the 50x step.** When the doc has zero remaining gaps, scan the repo for related artifacts: skills (`SKILL.md`), guides/SOPs, specs. Offer to update each one. Write a new spec in `specs/` broken into implementation waves. A completed interview that does not propagate is a documentation exercise, not knowledge extraction.

7. **Evaluate before committing.** Run the eval harness (`python3 eval-harness.py <path>`) to score the output on 5 axes: specificity (numbers/concrete names), decision coverage (chosen + rejected), gap closure (open TODOs penalized), language quality (filler words penalized), codebase exploration. Score must be > 0.60. If below, identify which axis is weak and re-interview on that gap.

## Why

Everyone on the same model gets the same baseline output. The differentiator is context — taste, voice, decisions unique to the individual. The hardest part of an AI operating system is extraction: getting knowledge out of the human's head into durable, reusable files. A quick 5-minute brain dump is never enough. The original "grill me" prompt was a single 4-sentence loop that produced a raw transcript. v2 adds structured frontmatter, action-first writing rules, progressive disclosure, propagation to related assets, an eval harness with 5 scoring axes, and a hard Definition of Done. The propagation step is the 50x multiplier — one interview can update multiple skills, guides, and specs across the repo.

## How to apply

- **Start:** Say "Use the grill-me-pro skill to extract everything about [topic]." The SKILL.md is registered at `~/.hermes/skills/grill-me-pro/SKILL.md`.
- **During:** Answer one question at a time. Be specific. The interviewer provides their recommended answer for each question.
- **Checkpoints:** Written to `brainstorm/<topic>.md` automatically. Each is a complete snapshot.
- **Propagation:** When zero gaps remain, the interviewer scans for related skills, guides, and specs, and offers to update them.
- **Evaluate:**
  ```bash
  python3 /Users/mikerodgers/Developer/RIGForge/repos/grill-me-pro/eval-harness.py /tmp/brainstorm-topic.md
  ```
- **Commit:** After propagation, commit the brainstorm doc + any updated skills/guides/specs.

## Gate criteria

| Gate | Threshold | Planted failure test |
|------|-----------|---------------------|
| Specificity | Score > 0.60 | Submit "as needed" doc → vague penalty |
| Decision coverage | Each decision has rejected alternatives | Doc with choices only, no alternatives → score < 0.60 |
| Gap closure | Zero open TODOs | Doc with 3 TODOs → gap_closure penalty |
| Language quality | Zero filler words | Doc with "delve" → language_quality penalty |
| Propagation | All related artifacts updated | Skill exists with stale content → not done |
| Eval harness | Score computed and threshold met | Run on empty doc → score < 0.60 |