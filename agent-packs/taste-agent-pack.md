# RIG Design Studio Taste Agent Pack

## Pre-flight
- Read `doctrines/DESIGN-STUDIO-TASTE-SYSTEM.md`
- Read `intake/design-studio-taste-intake.md`
- Verify DESIGN.md exists at repo root
- Set all 6 knobs for the project

## Core commands
```bash
# Extract tokens from a reference site
python3 bin/token-extractor.py https://reference-site.com --format design-md > DESIGN.md

# Run quality hooks
python3 hooks/check-ai-tone.py .
python3 hooks/check-contrast.py DESIGN.md
python3 hooks/check-consistency.py skills/

# Final gate before merge
python3 hooks/ship-gate.py
```

## 6-Stage Process
1. **Calibrate** -- set DESIGN.md direction + 6 knobs
2. **Inject** -- load relevant SKILL.md contracts
3. **Generate** -- build within constraints, reference DESIGN.md
4. **Audit** -- run 3 hooks, fix all findings
5. **Reduce** -- mies loop: "why is this here" -> cut copy 50% -> perfect what remains
6. **Ship** -- run ship-gate, must PASS all checks

## Taste Contracts (6)
| Skill | When to load | Key rule |
|-------|-------------|----------|
| hierarchy | Every page/section | One hero per viewport, heading levels are structural |
| typography | Every design | No Inter, use the scale, two typefaces max |
| color-restraint | Every design | Two colors per surface, one accent per site |
| spacing | Every layout | Whitespace is layout, scale is definitive |
| reduction-mies | Before polish | "Why is this here" -> cut -> perfect |
| motion | Animations/interactions | 200-400ms, cubic-bezier, no auto-play |

## Knobs (6)
| Knob | Default | When to tune |
|------|---------|-------------|
| typography_contrast | 0.8 | Editorial/publishing -> 0.9+ |
| color_restraint | 0.9 | Brand-heavy -> 0.95+ |
| spacing_density | 0.4 | Dashboard/table -> 0.3 |
| reduction_intensity | 0.85 | Minimalist -> 0.9+ |
| motion_restrained | 0.9 | Motion-heavy -> 0.5 |
| type_serifness | 0.3 | Editorial -> 0.7+ |