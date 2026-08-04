---
title: "Intake: Design Studio Taste System Build Card"
source: BUILD CARD — RIG Design Studio Taste System Analysis, 20+ Open-Source Solutions & Today's Build Plan.md
received: 2026-06-05
status: promoted
promoted_to: doctrines/DESIGN-STUDIO-TASTE-SYSTEM.md
---

## Source summary

Build card for a repeatable design-taste process inside RIG Design Studio. Key decisions:

1. Standardize on SKILL.md + hooks + npx skills add pattern (from 5 existing projects)
2. 6 taste contracts: hierarchy, typography, color-restraint, spacing, reduction-mies, motion
3. 6 design knobs: typography_contrast, color_restraint, spacing_density, reduction_intensity, motion_restrained, type_serifness
4. 3 audit hooks: check-ai-tone, check-contrast, check-consistency
5. 20+ open-source solutions mapped across 5 categories
6. 6-stage process: Calibrate -> Inject -> Generate -> Audit -> Reduce -> Ship

## Key claims extracted
- Every AI-generated UI starts as slop (Inter, purple gradients, generic cards)
- Mies reduction loop must run before polish
- Ship gate is a hard AND of all checks
- No Inter, no purple gradients, no system-ui

## Verification notes
3 hooks verified: clean text passes, adversarial text with banned words FAILS. 
6 skills written. Knob system present. DESIGN.md loaded with Deviation Forge direction.
Token extractor works (fetches site, extracts inline styles + CSS variables).