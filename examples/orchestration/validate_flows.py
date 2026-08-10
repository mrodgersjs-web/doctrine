#!/usr/bin/env python3
"""Structural validator for the Kestra flows in flows/.

This is a real gate, not an existence check. It fails on:
  - unparseable YAML
  - missing required top-level keys (id, namespace, tasks)
  - duplicate task ids inside a flow
  - a task or trigger `type:` that is not a known Kestra class

The last check matters most. Plugin fully-qualified class names are the easiest thing
to hallucinate when authoring flows with an AI assistant: an invented path like
`io.kestra.plugin.core.http.HttpRequest` looks correct and fails only at runtime, in
production, on the unhappy path. CORE_CLASSES below is pinned from the Kestra source
tree (core/src/main/java/io/kestra/plugin/core) so a wrong path goes red here instead.

Exit 0 = all flows valid. Exit 1 = at least one problem, all problems printed.
"""
from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("FAIL: PyYAML not installed — run: pip install -r requirements.txt", file=sys.stderr)
    raise SystemExit(1)

# Pinned from kestra-io/kestra core/src/main/java/io/kestra/plugin/core.
# Extend deliberately, with the source path that proves the class exists.
CORE_CLASSES = {
    "io.kestra.plugin.core.http.Request",
    "io.kestra.plugin.core.http.Download",
    "io.kestra.plugin.core.http.SseRequest",
    "io.kestra.plugin.core.log.Log",
    "io.kestra.plugin.core.log.PurgeLogs",
    "io.kestra.plugin.core.trigger.Schedule",
    "io.kestra.plugin.core.trigger.ScheduleOnDates",
    "io.kestra.plugin.core.trigger.Webhook",
    "io.kestra.plugin.core.trigger.Flow",
    "io.kestra.plugin.core.flow.If",
    "io.kestra.plugin.core.flow.Dag",
    "io.kestra.plugin.core.flow.Loop",
    "io.kestra.plugin.core.flow.LoopUntil",
    "io.kestra.plugin.core.flow.Parallel",
    "io.kestra.plugin.core.flow.Sequential",
    "io.kestra.plugin.core.flow.Subflow",
    "io.kestra.plugin.core.flow.Switch",
    "io.kestra.plugin.core.flow.Pause",
    "io.kestra.plugin.core.flow.Sleep",
    "io.kestra.plugin.core.flow.AllowFailure",
    "io.kestra.plugin.core.flow.WorkingDirectory",
}

REQUIRED_TOP_LEVEL = ("id", "namespace", "tasks")


def walk_typed(node, found: list[tuple[str, str]], where: str = "") -> None:
    """Collect every (id, type) pair anywhere in the tree — tasks nest arbitrarily."""
    if isinstance(node, dict):
        if "type" in node and isinstance(node["type"], str):
            found.append((node.get("id", where or "<anonymous>"), node["type"]))
        for key, value in node.items():
            walk_typed(value, found, where=node.get("id", where))
    elif isinstance(node, list):
        for item in node:
            walk_typed(item, found, where)


def collect_task_ids(node, ids: list[str]) -> None:
    if isinstance(node, dict):
        if "id" in node and "type" in node:
            ids.append(node["id"])
        for value in node.values():
            collect_task_ids(value, ids)
    elif isinstance(node, list):
        for item in node:
            collect_task_ids(item, ids)


def validate(path: Path) -> list[str]:
    problems: list[str] = []
    try:
        flow = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        return [f"{path.name}: unparseable YAML — {exc}"]

    if not isinstance(flow, dict):
        return [f"{path.name}: top level is {type(flow).__name__}, expected a mapping"]

    for key in REQUIRED_TOP_LEVEL:
        if key not in flow:
            problems.append(f"{path.name}: missing required top-level key '{key}'")

    if not isinstance(flow.get("tasks"), list) or not flow.get("tasks"):
        problems.append(f"{path.name}: 'tasks' must be a non-empty list")

    ids: list[str] = []
    collect_task_ids(flow.get("tasks"), ids)
    collect_task_ids(flow.get("triggers"), ids)
    duplicates = {i for i in ids if ids.count(i) > 1}
    for dup in sorted(duplicates):
        problems.append(f"{path.name}: duplicate task/trigger id '{dup}'")

    typed: list[tuple[str, str]] = []
    walk_typed(flow.get("tasks"), typed)
    walk_typed(flow.get("triggers"), typed)
    for task_id, fqcn in typed:
        if fqcn.startswith("io.kestra.plugin.core.") and fqcn not in CORE_CLASSES:
            problems.append(
                f"{path.name}: task '{task_id}' uses unknown core class '{fqcn}' "
                f"(not present in the pinned Kestra core plugin set)"
            )
        elif not fqcn.startswith("io.kestra.plugin."):
            problems.append(
                f"{path.name}: task '{task_id}' type '{fqcn}' is not a Kestra plugin FQCN"
            )
    return problems


def main() -> int:
    root = Path(__file__).resolve().parent / "flows"
    files = sorted(root.glob("*.yml")) + sorted(root.glob("*.yaml"))
    if not files:
        print(f"FAIL: no flow files found in {root}", file=sys.stderr)
        return 1

    all_problems: list[str] = []
    for path in files:
        problems = validate(path)
        status = "FAIL" if problems else "ok"
        print(f"  [{status}] {path.name}")
        all_problems.extend(problems)

    if all_problems:
        print(f"\n{len(all_problems)} problem(s):", file=sys.stderr)
        for problem in all_problems:
            print(f"  - {problem}", file=sys.stderr)
        return 1

    print(f"\n{len(files)} flow(s) valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
