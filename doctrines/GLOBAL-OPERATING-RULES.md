# RIG Global Operating Rules

These rules promote the provided RIG doctrines into global operating guidance for this repository and for agents working from it.

## Status

- Version: 2
- Promoted: 2026-06-05
- Source: User-provided doctrine intake in session context on 2026-06-05.
- Scope: Global rules for RIG doctrine work, design work, engineering work, implementation planning, review, and agent behavior.

## Prime directive

Treat doctrine as executable operating guidance. Do not treat it as prose decoration, inspiration, or optional framing.

Every non-trivial change must identify:

1. Objective.
2. Changed surfaces.
3. Verification command or review procedure.
4. Proof path.

## Global doctrine stack

Run these doctrines as the default order of operations for website, product-page, conversion, product, service, generator, and engineering work.

### Design / conversion track

| Layer | Doctrine | Global rule |
|---|---|---|
| 0 | Audience & Intent Foundation | Establish who lands, why they land, persona share, confidence grade, and kill-condition from evidence before designing or asserting the visitor mind. |
| 1 | GIVE↔THINK | Map what the work gives and what the recipient thinks beat by beat before designing, writing, or implementing. |
| 1.5 | Commitment Ladder | Escalate asks one rung at a time. No ask may exceed the current THINK-state. Proof precedes ask. |
| 2 | IQRSQPI | For each node/component: Intent → Questions → Research → Spec → Quality⇄Research until dry → Plan → Implement. Confidence is the gate, not the calendar. |
| Gate A | 27-Persona Panel | Craft must pass the expert panel threshold and hard vetoes before shipping meaningful design/copy/motion decisions. |
| Gate B | Buyer Panel | Sale/intent must pass the relevant buyer. Beautiful-but-won't-book still fails. |

### Build / engineering track

| Layer | Doctrine | Global rule |
|---|---|---|
| Root | RIG Build Method | Every product/service runs the engineering counterpart to the design method. Nothing advances on a guess; proof or it didn't happen. |
| Spine | IQRSQPI Engineering | Run Intent → Questions → Research → Spec → Quality⇄Research → Plan → Implement per step and layer, with prototype-led loops and adversarial red-team. |
| Proof | Proof or It Didn't Happen | Nothing is done, fixed, green, or working until a real command output, gate result, or artifact hash proves it. |
| Non-vacuity | Adversarial Verification | Every gate and load-bearing claim must be plant-failure verified: break it, watch RED, restore. |
| Determinism | Deterministic Before Agentic | Build the deterministic floor first; AI only fills narrow named slots; generator control/verification stays AI-free. |
| Safety | Gate-D | No outward or irreversible action without explicit typed human approval; SKIP/UNAVAILABLE is never a fake PASS. |
| Reproducibility | Reproducibility & Pinning | Claim only the reproducibility tier you can prove; exact pins, real digests, secrets by reference. |
| Execution | Phase Discipline | Build in dependency order; each phase builds, adversarially verifies, verifies the real tree, then commits on green. |

## Always-on rules

### 1. Map the mind before the page

- Do not design a page, section, node, offer, CTA, or narrative arc until the relevant THINK-state is named.
- The GIVE must answer the current THINK and set up the next THINK.
- Unvalidated THINK is a guess and must be marked as such.

### 2. Evidence before assertion

- Do not assert persona, intent, market state, buyer readiness, proof strength, engineering readiness, reproducibility, or correctness without source evidence or an explicit confidence grade.
- Keep raw intake separate from promoted doctrine.
- If evidence is missing, mark the line DRAFT or FLAG and resolve it through research or escalation.

### 3. Proof before ask / proof before done

- No rung asks before it gives.
- No cold visitor is asked for money before the ladder earns that ask.
- Paid/scoped offerings appear only at the earned commitment rung; full engagements appear only at the sign rung.
- No engineering claim is accepted as done until a real command output, gate result, or artifact hash proves it.

### 4. Run IQRSQPI for every meaningful node or engineering step

For every meaningful component, page beat, transition, offer, doctrine pack, product step, generator layer, or engineering phase:

1. Name the one-sentence intent.
2. Write the unknowns/questions.
3. Research every load-bearing question.
4. Draft the spec with AUTO / DRAFT / FLAG tags where applicable.
5. Re-question the spec.
6. Loop research until no load-bearing unknown remains.
7. Plan only after the loop is dry.
8. Implement only after plan and gates pass.

### 5. Dual-gate design decisions

- Craft gate: use the 27-Persona Panel for meaningful design, copy, motion, positioning, performance, accessibility, conversion, and scale decisions.
- Buyer gate: use the Buyer Panel for sales/booking/intent decisions.
- A change that is beautiful but fails the buyer is not done.
- A change that converts but violates performance or accessibility hard vetoes is not done.

### 6. Engineering gates are adversarial and empirical

- A gate that cannot be made RED with a planted failure is theater, not proof.
- Verify the artifact, not the report.
- Treat `done = all(blocking_gates_pass)` as a computed hard AND.
- Build deterministic substrate before agentic slots.
- Pin exact dependencies and base digests; never inline secrets.
- Stop before outward/irreversible actions and require explicit typed human approval.

### 7. Agent behavior going forward

When acting as an agent in this repository:

- Start from the doctrine stack, not personal taste.
- Prefer small, verifiable doctrine packs over broad unsourced essays.
- State the objective and proof path for non-trivial changes.
- Preserve exact doctrine language where it is canonical.
- Do not claim a doctrine is v10 unless it has source evidence, an agent pack, tests, proof requirements, and a versioned release path.
- Do not include credentials, private client material, or machine-specific secrets.
- If a request conflicts with these global rules, flag the conflict and propose a compliant path.

## Canonical doctrine references

The operating rules above are derived from these doctrine surfaces:

### Design / conversion

- `COMMITMENT-LADDER-DOCTRINE.md`
- `GIVE-THINK-DOCTRINE.md`
- `IQRSQPI-DOCTRINE.md`
- `RIG-DESIGN-METHOD.md`
- `THE-27-PANEL.md`
- `THE-BUYER-PANEL.md`

### Build / engineering

- `RIG-BUILD-METHOD.md`
- `IQRSQPI-ENGINEERING.md`
- `INTENT.md`
- `PROOF-OR-IT-DIDNT-HAPPEN.md`
- `ADVERSARIAL-VERIFICATION.md`
- `DETERMINISTIC-BEFORE-AGENTIC.md`
- `GATE-D.md`
- `REPRODUCIBILITY-AND-PINNING.md`
- `PHASE-DISCIPLINE.md`

When those files exist as promoted doctrine in this repository, this global rule file governs their use as always-on operating guidance.
