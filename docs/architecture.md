# Architecture

```
doctrines/*.md  --+
intake/*.md      --+--> loader --> DoctrineRecord[] --> validator --> problems (empty = clean)
agent-packs/*.md --+
```

## Package

- `rig_doctrine/model.py` defines the record shape: id (file stem lowercased),
  kind (`doctrine`, `intake`, `agent-pack`), title, front matter, body, and the
  level-2 sections derived from it.
- `rig_doctrine/loader.py` walks the three kind directories, splits the
  YAML-subset front matter from the body (values are scalars, `null`, or
  quoted strings), and resolves ids. Remote and anchor links are ignored by
  `relative_links`; only local file links are checked.
- `rig_doctrine/validator.py` applies the rules below and returns `Problem`
  records (`path`, `rule`, `message`).
- `rig_doctrine/cli.py` is the `rig-doctrine` entry point: `list`, `show`,
  `validate`, each with `--json`.

## Validation rules

| Rule | Applies to | Fires when |
| --- | --- | --- |
| `body` | all | the body is empty or under 40 characters |
| `h1` | doctrine, agent-pack | doctrine: not exactly one level-1 heading; agent-pack: none |
| `sections` | doctrine, agent-pack | no level-2 section |
| `front-matter` | intake | a required key (`title`, `source`, `received`, `status`, `promoted_to`) is missing, or `status` is not one of `intake`, `candidate`, `promoted`, `retired` |
| `link` | all | a local markdown link target does not exist on disk |
| `id` | repository | two files map to the same id |

## Design notes

- Front matter parsing is a small deliberate subset, not full YAML: doctrine
  files in the wild carry simple key/value metadata and nothing else, and a
  hand-rolled parser keeps the package dependency-free.
- Links are validated against the filesystem at validation time, so a renamed
  doctrine file breaks referencing files in CI instead of at read time.
- The validator never modifies files; the CLI is read-only apart from its own
  output. This keeps `validate` safe to run in any hook or CI job.
- The corpus-wide check lives in `tests/test_validator.py`
  (`test_bundled_corpus_validates_clean`), so schema drift in doctrine text is
  caught by the same suite that tests the code.
