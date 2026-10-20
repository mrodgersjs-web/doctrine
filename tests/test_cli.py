import json
from pathlib import Path

from rig_doctrine.cli import main

ROOT = Path(__file__).resolve().parents[1]


def test_list_json(capsys):
    assert main(["--root", str(ROOT), "list", "--json"]) == 0
    data = json.loads(capsys.readouterr().out)
    assert data["counts"]["intake"] == 10


def test_list_by_kind(capsys):
    assert main(["--root", str(ROOT), "list", "--kind", "agent-pack"]) == 0
    out = capsys.readouterr().out
    assert "taste-agent-pack" in out and "gate-d" not in out


def test_show_json(capsys):
    assert main(["--root", str(ROOT), "show", "gate-d", "--json"]) == 0
    data = json.loads(capsys.readouterr().out)
    assert data["kind"] == "doctrine" and "The laws" in data["sections"]


def test_show_text(capsys):
    assert main(["--root", str(ROOT), "show", "gate-d"]) == 0
    assert "GATE-D" in capsys.readouterr().out


def test_show_unknown():
    assert main(["--root", str(ROOT), "show", "ghost"]) == 2


def test_validate_repo_ok(capsys):
    assert main(["--root", str(ROOT), "validate"]) == 0
    assert "OK" in capsys.readouterr().out


def test_validate_json_ok(capsys):
    assert main(["--root", str(ROOT), "validate", "--json"]) == 0
    data = json.loads(capsys.readouterr().out)
    assert data["ok"] is True


def test_validate_one_file(capsys):
    assert main(["--root", str(ROOT), "validate", str(ROOT / "doctrines" / "GATE-D.md")]) == 0


def test_validate_failing_file(tmp_path, capsys):
    bad = tmp_path / "doctrines"
    bad.mkdir()
    f = bad / "broken.md"
    f.write_text("# T\n\n## S\n\nSee [x](./gone.md) for more detail here.\n")
    assert main(["--root", str(tmp_path), "validate"]) == 1
    assert "FAILED" in capsys.readouterr().out
