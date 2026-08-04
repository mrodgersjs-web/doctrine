---
title: TASTE — Design Studio Taste System Doctrine
version: 1.0.0
source: BUILD CARD — RIG Design Studio Taste System Analysis, 20+ Open-Source Solutions
status: promoted
---

# TASTE — Design Studio Taste System

**RULE.** Every AI-generated UI element starts as slop (Inter font, purple gradient, generic card grid). The taste system is the filter: calibrate to a direction, inject constraints, generate within them, audit against them, reduce to essentials, gate the result. No output ships without passing all three audit hooks.

## The laws

1. **Calibrate before generate.** Every design session starts with a committed aesthetic direction — either an existing DESIGN.md or tokens extracted from a reference site. "Just make it look good" is not a direction. The direction sets the color palette, typeface pair, spacing scale, and radius tokens.

2. **Six taste contracts, six knobs.** Direction is enforced by 6 SKILL.md contracts (hierarchy, typography, color-restraint, spacing, reduction-mies, motion) tuned by 6 dimensional knobs (typography_contrast, color_restraint, spacing_density, reduction_intensity, motion_restrained, type_serifness). Every project sets all 6 knobs before the first generation.

3. **Three audit hooks, one ship gate.** Every output must pass check-ai-tone (banned words, generic phrases), check-contrast (color accessibility), and check-consistency (design token adherence) before the ship gate unlocks. The ship gate is a hard AND — one RED blocks merge.

4. **The mies reduction loop runs before polish.** Ship-gate order is: generate → audit → reduce (mies) → re-audit → ship-gate. Reducing before polishing catches 80% of taste issues. Polishing a messy layout is waste.

5. **Two colors per surface, one accent per site.** A surface is background + text + accent + border. Two colors max (neutral bg/text + one accent). The accent is exactly one hue used across the entire site — links, buttons, highlights, active states all use variations of it.

6. **No Inter, no purple gradients, no system-ui.** These are the three signatures of AI-generated slop. Banning them forces an intentional choice. The replacements: Sohne, IBM Plex Sans, GT America for sans; Tiempos, Lyon, Source Serif for serif. Accent colors from the brand palette, never purple.

7. **Whitespace is at least 40% of viewport.** Any page must have at least 40% empty pixel area (background, gap, margin). Whitespace under 30% is clutter. Measure by bounding-box ratio. If the content density exceeds 70%, the page fails the spacing taste contract.

## Why

AI agents produce functional-but-generic UI by default. Inter font, purple gradients, generic card grids — because the training data is dominated by these patterns. The taste system makes the default output fail until it's been filtered through intentional constraints. Five open-source taste projects (CodeTaste-Pro, mies, ux-ui-design-taste, taste-skills, everything-design-taste) all solve the same problem with the same core architecture: markdown contract → agent context → review hooks → gate. This doctrine standardizes the Design Studio on that shared architecture while adding the 6-knob tunability, the mies reduction loop, and a deterministic ship gate.

## How to apply

- Start each project by setting all 6 knobs in `knobs/<project>.json`.
- Load the relevant `skills/<contract>/SKILL.md` into agent context before generating.
- Generate UI within the constraints. The agent should reference the DESIGN.md for tokens and the active knob file for intensity.
- Run `python3 hooks/check-ai-tone.py <output>` — remove all flagged phrases.
- Run `python3 hooks/check-contrast.py DESIGN.md` — verify all color pairs meet 4.5:1 AA minimum.
- Run `python3 hooks/check-consistency.py <output>` — verify design token adherence.
- Apply the mies reduction loop: "why is this here" → cut copy by 50% → perfect what remains.
- Run `python3 hooks/ship-gate.py` — all 3 hooks + skills count + DESIGN.md presence must pass.
- If any check fails, fix and re-run. No sailing on red.

## Gate criteria

| Gate | Threshold | Planted failure test |
|------|-----------|---------------------|
| AI tone | Zero banned words/phrases | Generate text with "leverage" → FAIL |
| Contrast | Minimum 4.5:1 AA ratio | Use #999 on #FFF → FAIL |
| Consistency | Token values match DESIGN.md | Use non-scale spacing (18px) → FAIL |
| Skills loaded | 6+ SKILL.md contracts | Remove one → count < 6 → FAIL |
| DESIGN.md present | File exists | Missing file → FAIL |
| Ship gate | All previous pass | Single RED → gate blocked |