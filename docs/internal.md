# RIG Doctrine Repo

RIG Doctrine Repo is the canonical home for RIG operating doctrine: the rules, standards, workflows, build processes, proof requirements, agent instructions, and reusable doctrine packs that make RIG systems behave consistently across Codex, Claude, Susan, Jake, MCP tools, CLIs, QNAP, GitHub, and future agents.

This repository is not meant to be another folder of notes. It is meant to become the doctrine control plane: a versioned, testable, source-cited, agent-loadable system that turns raw ideas and Recall cards into reliable operating doctrine.

## Current Intent

The first version of this repo should answer four practical questions:

1. What doctrines does RIG follow?
2. How does an AI coding agent load and obey those doctrines?
3. How does a raw insight become a durable doctrine?
4. What would a 1000x better doctrine system look like?

The current source baseline comes from the RIG Vault v10 work inside `Startup-Intelligence-OS`, including:

- 9 priority doctrine domains.
- 10 Mike-use scenario contracts.
- 180 potential client persona contracts across 9 focus verticals.
- 12 seed doctrine packages in the current vault.
- CLI and MCP-compatible command surfaces.
- QNAP mirror proof.
- Cockpit data and proofpacket artifacts.

This repo is the next split-out step: make the doctrines portable, reusable, and pullable by any agent or tool without requiring the full Startup Intelligence OS repository.

## What Belongs Here

This repo should hold durable doctrine, not transient working notes.

Put these here:

- Canonical RIG doctrines.
- Agent-facing instruction packs.
- DoneContract templates.
- ProofPacket schemas.
- GEV loop rules.
- RIG build doctrine.
- RIG AI engineering doctrine.
- RIG systems engineering doctrine.
- Studio operating doctrine.
- LinkedIn, communications, GTM, Instagram, strategy, and app-building doctrine.
- CLI and MCP usage contracts.
- Test fixtures that prove agents can load and apply doctrine.
- Source maps and evidence maps for doctrine claims.
- Versioned doctrine releases.

Do not put these here unless they have been promoted:

- Raw Recall exports.
- One-off chat transcripts.
- Unsourced claims.
- Temporary implementation notes.
- Local machine secrets.
- QNAP connection credentials.
- Private client material without a source and access policy.
- Unverified scraped content.

Raw material should start in `intake/` or in the external RIG Vault intake lane, then be promoted into doctrine only after assessment.

## Starter Repo Structure

```text
.
+-- README.md
+-- doctrines/
|   +-- canonical doctrine packs
+-- agent-packs/
|   +-- compact instructions agents can load into coding sessions
+-- schemas/
|   +-- DoneContract, ProofPacket, doctrine, source map, and promotion schemas
+-- proofpackets/
|   +-- release proof, test proof, verifier receipts, and parity proof
+-- examples/
|   +-- sample prompts, agent sessions, CLI calls, and promoted doctrine examples
+-- intake/
|   +-- temporary raw candidate material before promotion
+-- tools/
    +-- future CLI, MCP, validators, generators, and exporters
```

## What A 1000x Better Version Looks Like

A 1000x better RIG Doctrine Repo is not a bigger README. It is a living doctrine operating system.

### 1. Every Doctrine Is Agent-Executable

The repo contains doctrine packs that agents can load directly. Each pack includes the rules, examples, tests, source maps, and proof requirements needed to apply the doctrine in a real session.

Success metric:

- 95% or more of agent sessions can load the correct doctrine without manual rediscovery.

### 2. Every Claim Has Evidence

Doctrines include source maps. Claims are tied to Recall cards, build cards, GitHub commits, QNAP artifacts, human-origin markers, or external references.

Success metric:

- 95% or more of factual claims have source or marked origin.

### 3. Doctrine Promotion Is Deterministic

Raw cards and ideas move through a defined pipeline:

```text
v0 input -> v1 candidate -> v5 repeatable workflow -> v10 operating doctrine
```

Success metric:

- Card-to-assessment time is under 5 minutes.
- Assessment-to-agent-pack time is under 20 minutes.

### 4. CLI And MCP Are First-Class

The repo ships a CLI and MCP server that expose the same doctrine capabilities:

- list
- search
- get
- assess
- promote
- export
- proof
- context-for-task

Success metric:

- 100% CLI/MCP parity for public doctrine operations.

### 5. Doctrine Has Regression Tests

Every doctrine has tests that check whether agents apply it correctly.

Examples:

- Does the agent create a DoneContract before a non-trivial build?
- Does the agent emit proof before claiming PASS?
- Does the agent avoid touching protected areas?
- Does the agent load the right domain doctrine for a task?

Success metric:

- 100% of v10 doctrines have regression fixtures.

### 6. Cockpit Shows Doctrine Health

A visual cockpit shows:

- doctrine maturity
- stale doctrines
- conflicting doctrines
- missing proof
- agent usage
- QNAP parity
- test status
- next safe action

Success metric:

- User can find doctrine, proof, and next action in 3 clicks or less.

### 7. QNAP And GitHub Stay In Parity

GitHub stores canonical doctrine. QNAP stores durable mirrors, snapshots, raw intake, and heavy artifacts.

Success metric:

- Protected doctrine paths have 100% GitHub/QNAP parity.
- Sync freshness is under 24 hours.

### 8. Agents Learn From Work

After coding sessions, agents can propose doctrine updates from real work:

- new rule
- failed assumption
- better test
- stronger proof requirement
- improved prompt
- reusable build card
- retired anti-pattern

Success metric:

- At least 10 useful doctrine candidates are promoted per week.

### 9. Client Personas Become Doctrine Inputs

The repo should encode how different client personas evaluate RIG value. That turns doctrine into market-facing capability.

Success metric:

- Every focus vertical has 20 client persona contracts.
- Every persona has done criteria, good criteria, KPIs, surfaces, and proof requirements.

### 10. Doctrine Becomes A RIG Product Layer

The 1000x version can be used as:

- internal operating system
- AI agent instruction layer
- CLI package
- MCP server
- QNAP-backed knowledge system
- studio engine
- client-facing proof system
- audit trail
- onboarding pack
- build factory standard

Success metric:

- New RIG systems can cite exactly which doctrine pack they follow.

## Near-Term Implementation Roadmap

### Phase 1: Repo Baseline

- Add canonical README.
- Add starter folders.
- Import current v10 doctrine domain contracts.
- Add initial AGENTS.md.
- Add schema drafts for doctrine, DoneContract, and ProofPacket.

### Phase 2: Portable Doctrine Packs

- Split the 9 domains into doctrine packs.
- Add source maps.
- Add agent packs.
- Add examples.
- Add regression fixtures.

### Phase 3: CLI

- Build `rig-doctrine`.
- Add JSON output.
- Add golden fixtures.
- Add local validation commands.

### Phase 4: MCP

- Add MCP server.
- Mirror CLI commands as MCP tools.
- Add integration tests.
- Add client smoke checks.

### Phase 5: RAG And Retrieval

- Chunk doctrines.
- Add embeddings.
- Add hybrid search.
- Add golden retrieval evals.
- Add citation checks.

### Phase 6: Cockpit

- Add visual doctrine cockpit.
- Show domain health, proof, parity, and next actions.
- Add accessibility and responsive checks.

### Phase 7: QNAP Mirror

- Add LAN-first sync.
- Add parity checks.
- Add nightly proof.
- Add rollback path.

### Phase 8: Productization

- Publish install instructions.
- Add releases.
- Add SDK or package exports.
- Add client-facing doctrine briefs.
- Add adoption metrics.
