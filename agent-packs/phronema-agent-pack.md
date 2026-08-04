# Phronema Agent Pack

When building or operating a Phronema compiled intelligence studio, load this agent pack:

## Pre-flight
- Read `doctrines/PHRONEMA-COMPILED-INTELLIGENCE.md`
- Read `intake/phronema-paramount-intake.md`
- Verify evidence pipeline exists and passes adversarial tests
- Verify AuditOfficer is immutable and logs are append-only

## Core commands
```bash
# Run the full daily intelligence cycle
python3 agents/conductor/conductor_agent.py

# Run a single source through the evidence pipeline
python3 -c "from pipeline.evidence_pipeline import EvidencePipeline; ep=EvidencePipeline('source','content'); ep.stage_raw(); ep.stage_normalize()"

# Verify governance gates
python3 governance/audit_officer.py

# Check scrape ledger
python3 ledger/scrape_ledger.py

# Generate ProofPacket
python3 -c "from agents.conductor.conductor_agent import ConductorAgent; ConductorAgent().run_daily_cycle()"
```

## Gates to enforce
| Gate | Test command |
|------|-------------|
| Evidence quality floor | `python3 pipeline/evidence_pipeline.py` — must show ALL PASS |
| Source hash required | Inject claim without hash → AuditOfficer must RED |
| 70/30 deterministic floor | Run with 50/50 agentic/det split → must RED |
| Deviation gate | Promote signal at 0.3 confidence → must RED |
| ProofPacket seal | Modify proof → hash mismatch → RED |