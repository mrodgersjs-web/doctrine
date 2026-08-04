# IQRSQPI — Engineering Doctrine (RIG App Studio)

**RULE for all RIG App Studio buildout — no exceptions.** Adapts Mike's canonical
website doctrine (`~/rig-design-studio/process/IQRSQPI-DOCTRINE.md`) to full-stack
engineering. Same spine, engineering content. The cure never ships before the
diagnosis is researched. Question → research → question → research, until we are
**"very, very comfortable we have good answers."** Confidence is the gate, not the
calendar.

Declared 2026-06-04 by Mike, stepping back to set process before building.

---

## The spine (run once per STEP)

**I — Q — R — S — Q — (R) — P — I**

| Step | Name | Engineering content | Done when |
|---|---|---|---|
| **I** | INTENT | What the studio IS / ISN'T, what it's great at, the KPIs. One sentence, deletable-test-proof. | Remove it and the studio has no reason to exist. |
| **Q** | QUESTIONS | 100+ questions from the world-class **persona panel** (below). Surface every unknown. Do NOT guess. | The question set spans every persona lens + every layer of the lattice. |
| **R** | RESEARCH | Answer every load-bearing question with evidence — scrape GitHub repos, OSS frameworks, plug-and-play solutions; find what we do NOT have to rebuild. Parallel lanes. | Every load-bearing question has an answer + source + grade (HIGH/MED/LOW). No bare claims. |
| **S** | SPEC | Full **value-stream + lattice** spec: archetypes 1–4, every layer, what is **deterministic** vs **probabilistic**. Tag every line AUTO / DRAFT / FLAG. | All lines resolved on paper + tagged. |
| **Q** | QUALITY (re-question) | Interrogate the spec: right people? right processes? right solutions? **where are the gaps**, what must we build? The spec generates new questions. | Residual-question list written. Nothing DRAFT treated as settled. |
| **(R)** | RESEARCH again | Research the new questions, then **loop Q ⇄ R again — at least 3× per step** — until the loop is DRY. | A full Q⇄R pass surfaces no new load-bearing unknown. |
| **P** | PLAN | Lock it. The **ultra plan** is earned here (never before). Freeze decisions, write the plan + decisions log. | Step is 🟢. Gate passed. Plan written. |
| **I** | IMPLEMENT | Build it — code / CLI / MCP / app / backend — RODA-style DevOps build-out + proof gates. | The slice ships and passes its proof gates. |

**The heart is the Q ⇄ R loop.** The two research rounds are the *minimum*; loop until dry.

---

## The recursive / fractal operating model

Exactly as Mike framed it: *"go as many layers deep as we need once we understand
intent — then do that again every single time, for each step and each layer."*

```
IQRSQPI  ── the macro spine, run once per STEP
   └── at every STEP and every LAYER, two engines drive the Q⇄R loop:
        • ITERATIVE DEPTH  → generates the 100+ questions from N persona lenses
        • RED TEAM (adversarial) → tries to REFUTE every answer before acceptance
   └── loop Q ⇄ R  ≥3× per step, until DRY
   └── GATE → Mike approves → next step. Nothing advances on a guess.
```

## Prototype-led loops (Mike's refinement, 2026-06-04)

The Q⇄R loop is **driven by throwaway prototypes, not abstract questions.** Each loop is:

**MOCK → QUESTIONS → RESEARCH (reactions)** — run **3×**, learning off each.

1. **MOCK** — quickly build a throwaway prototype of *what it could look like / how it
   could work*. Concrete beats abstract: the mock makes the questions sharp and gives
   research something real to react to.
2. **QUESTIONS** — interrogate the mock (persona panel + Mike). What works, what's wrong,
   what's missing, what surprised us.
3. **RESEARCH (reactions)** — research how the best tools/people actually handle this, and
   how people react to *this* mock. Feed it back into the next mock.

Three prototype loops per hard problem, each cheaper to throw away than the spec it
de-risks. **The prototype is research-by-experiment** — it answers questions a survey
cannot ("what would this even look/feel like?"). A mock can stand in for a research round
when the unknown is experiential. Mocks are throwaway by default; nothing a mock proves
becomes a decision until it survives the Q⇄R it triggers.

## The persona panel (the Questions engine)

Every Questions step asks from these world-class lenses — at minimum:

- **DevOps / SRE** — deploy, scale, observability, rollback, reliability
- **Staff backend architect** — data, APIs, services, state, consistency
- **Frontend lead** — architecture, performance, accessibility, maintainability
- **UX / UI designer** — the build experience + the generated product's UX
- **Security engineer** — secrets, authz, supply chain, blast radius
- **QA / test automation** — what proves "it works", how it can't lie
- **Product manager** — value, scope discipline, archetype fit
- **The end-user / founder (Mike)** — does it actually solve the real job
- **AI-codegen systems expert** — the det/prob boundary, robust-not-vibe

## The laws

1. **Confidence is the gate, not the calendar.**
2. **No DRAFT silently becomes a decision** — it gets more research or escalates to Mike.
3. **Evidence is graded and sourced** (HIGH / MED / LOW + source).
4. **Research before every component AND every layer** — not just the whole.
5. **Deterministic before agentic** (RIG doctrine): the *generator* must be robust
   even where the *output* uses AI. Vibe-coding does not produce a robust app.
6. **Adversarial red-team every load-bearing answer before it is accepted.**

## Artifacts

- `docs/process/` — this doctrine + INTENT.md (the standing rules)
- `docs/iqrsqpi/<step>/` — per-step `questions.md`, `research.md`, `spec.md`,
  `redteam.md`, `decisions.md`. Every step leaves a graded paper trail.

## Gates

Each step ends at a **Mike gate**. The studio (and any product it builds) advances
only when the loop is dry and Mike is comfortable. ProofPacket or it did not happen.

---

*Version 1 · 2026-06-04 · adapted from the canonical website IQRSQPI for full-stack
engineering. Parent rule: [[iqrsqpi-doctrine]] / [[give-think-doctrine]].*
