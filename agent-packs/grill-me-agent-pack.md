# Grill Me Pro Knowledge Extraction Agent Pack

When extracting knowledge from a human into reusable assets, load this agent pack:

## Pre-flight
- Read `doctrines/GRILL-ME-KNOWLEDGE-EXTRACTION.md`
- Read `intake/grill-me-pro-intake.md`
- Ensure SKILL.md is registered: `ls ~/.hermes/skills/grill-me-pro/SKILL.md`

## Core loop
1. **Ask one question** → provide recommended answer → wait for response
2. **Demand specifics** — reject "as needed", "regularly", "appropriate"
3. **Explore codebase** before asking the human
4. **Checkpoint** every 2-3 answers to `brainstorm/<topic>.md`
5. **Propagate** - when no gaps remain, scan for related skills/guides/specs

## Eval commands
```bash
# Evaluate a brainstorm doc
python3 /Users/mikerodgers/Developer/RIGForge/repos/grill-me-pro/eval-harness.py /path/to/brainstorm/doc.md

# Self-test
python3 /Users/mikerodgers/Developer/RIGForge/repos/grill-me-pro/eval_harness.py
```

## Definition of Done
- [ ] All gaps closed (no TODOs)
- [ ] Every decision has rejected alternatives
- [ ] Vague terms replaced with specific numbers/names/thresholds
- [ ] Related skills/guides/specs updated
- [ ] Eval harness score > 0.60