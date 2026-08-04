---
title: "Intake: Grill Me Pro v2 Build Card"
source: Build Card v2 Grill Me Pro — A Production-Grade, Self-Improving Knowledge Extraction Skill for Claude Code.md
received: 2026-06-05
status: promoted
promoted_to: doctrines/GRILL-ME-KNOWLEDGE-EXTRACTION.md
---

## Source summary

Production-grade knowledge extraction skill turning the original "grill me" prompt into a versioned, tested, self-improving system. Key architectural decisions:

1. Interview engine: one question at a time, always with recommended answer, explore codebase first
2. Action-first writing rules: demand specificity, reject vague terms, strip robot filler
3. Checkpointing: save after every 2-3 answers, `brainstorm/<topic>.md`
4. Progressive disclosure: load reference files only when relevant branch is active
5. Propagation: when doc has no gaps, scan repo for related skills/guides/specs and update
6. Definition of Done: no TODOs, all decisions have rejected alternatives, related artifacts updated
7. Eval harness: score on 5 axes (specificity, decision coverage, gap closure, language quality, codebase exploration)

## Key claims extracted

- The differentiator is context — everyone on same model gets same baseline
- Propagation is the 50x step — one interview updates multiple skills
- Skills are versioned, tested code, not magic
- Iteration curve: 70% → 75% → 80% ... capping ~95% after 10-30 iterations

## Verification notes

Eval harness verified: good doc beats empty doc (0.695 > 0.53), deterministic scoring, filler penalized, all 8 fields present. SKILL.md installed at ~/.hermes/skills/grill-me-pro/.