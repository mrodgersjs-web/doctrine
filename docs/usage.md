# Usage depth: how doctrine is loaded, grown and retired

## Loading order for an agent session

1. Repository `AGENTS.md` (always-on operating rules).
2. The agent pack that matches the task (`agent-packs/`).
3. The promoted doctrine the pack points at (`doctrines/`).
4. Deeper material only when the task needs it.

This keeps a session grounded without loading the whole corpus at once.
`rig-doctrine list` and `rig-doctrine show <id>` are the machine entry points;
both accept `--json`.

## Maturity levels

Doctrine moves through four levels. The validator enforces the shape of what
is in the repository; promotion itself is a human judgment.

| Level | Meaning | Where it lives |
| --- | --- | --- |
| raw (v0) | Input: a card, a build lesson, an idea. Not doctrine. | outside the repo or `intake/` |
| candidate (v1) | Named idea with source, problem statement, rule, anti-patterns. | `intake/` with `status: candidate` |
| workflow (v5) | Repeatable process with triggers, instructions, tests, failure modes. | `intake/` with `status: candidate` or `promoted` |
| agent-loadable (v10) | Source evidence, doctrine text, agent pack, done contract, tests, proof requirements, version history, retirement policy. | `doctrines/` + `agent-packs/` |

The standard: if an agent cannot load it, apply it, test against it, and emit
proof for it, it is not agent-loadable doctrine.

## Intake front matter

Every intake record carries:

```yaml
title: "Intake: ..."
source: "where the text came from"
received: 2026-06-05
status: intake        # intake | candidate | promoted | retired
promoted_to: null     # or the doctrine file it became
```

## Minimum doctrine pack contract

A mature doctrine pack should carry (this is the target shape, not a
validator rule):

```yaml
id: rig-doctrine-example
name: Example Doctrine
version: 0.1.0
status: candidate
domain: engineering-capability
owner: Mike Rodgers
source_policy:
  requires_source_per_claim: true
agent_usage:
  load_when: ["task touches the relevant domain"]
  required_outputs: ["controlling_doctrine", "done_contract"]
quality_gates: ["tests_pass", "proof_paths_exist", "rollback_or_blocker_path_exists"]
```

## Proof standard

A PASS claim includes: objective, changed surfaces, commands run, test
results, proof paths, known failures, rollback or blocker path. When the work
cannot be verified, the honest status is `planned`, `candidate`, `partial`,
`blocked`, `failed`, or `needs verifier`, never PASS.

## Roadmap

- CLI commands beyond `list` / `show` / `validate` (for example assessing an
  intake record or recording a promotion) need a promotion ledger first.
- An MCP surface should mirror the CLI one-to-one, with a regression test per
  tool.
- A mirror/parity check against a second storage location is a nightly job
  that reports drift loudly.
