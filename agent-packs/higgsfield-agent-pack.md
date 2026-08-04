# Higgsfield Cinematic OS Agent Pack

When generating video content through the RIG studio, load this agent pack:

## Pre-flight
- Read `doctrines/HIGGSFIELD-CINEMATIC-OS.md`
- Read `intake/higgsfield-cinematic-os-intake.md`
- Run preflight linter: `python3 seedance_lint.py`

## Core commands
```bash
# Run preflight linter
python3 /Users/mikerodgers/Developer/RIGForge/repos/higgsfield-cinematic-os/seedance_lint.py

# Check model specs for a generation
python3 -c "import seedance_lint as sl; print(sl.lint_prompt('seedance_2.0', 'prompt', '16:9', 8))"

# Estimate cost before generating
python3 -c "import seedance_lint as sl; print(sl.estimate_cost('seedance_2.0', 15, '1080p'))"
```

## Routing table
| Request | Route to |
|---------|----------|
| "generate video" / "seedance" | Seedance 2.0 sub-skill → preflight |
| "cinema studio 2.5/3.0/3.5" | Corresponding Cinema tier |
| "image" / "GPT Image" | GPT Image 2.0 director |
| "ad" / "marketing" | marketing-studio sub-skill |
| "preflight" / "check" / "validate" | Pre-flight gate |

## Resolution discipline
Draft at 480p. Client review at 720p. Final delivery at 1080p. Never burn credits on 1080p drafts.