from pathlib import Path

from rig_doctrine.loader import load_record, load_repo
from rig_doctrine.model import AGENT_PACK, DOCTRINE, INTAKE
from rig_doctrine.validator import Problem, validate_record, validate_repo

ROOT = Path(__file__).resolve().parents[1]


def make(tmp_path, name, text, kind):
    p = tmp_path / name
    p.write_text(text)
    return load_record(p, kind)


GOOD_DOCTRINE = "# Title\n\n## Why\n\nSome doctrine text long enough to count as a body.\n"
GOOD_INTAKE = (
    "---\ntitle: t\nsource: s\nreceived: 2026-06-05\nstatus: intake\npromoted_to: null\n---\n"
    "\n## Summary\n\nIntake body text long enough to count as a body here.\n"
)
GOOD_PACK = "# Pack\n\n## Steps\n\nAgent instructions long enough to count as a body.\n"


def rules(problems):
    return {p.rule for p in problems}


def test_good_records_pass(tmp_path):
    assert validate_record(make(tmp_path, "a.md", GOOD_DOCTRINE, DOCTRINE)) == []
    assert validate_record(make(tmp_path, "b.md", GOOD_INTAKE, INTAKE)) == []
    assert validate_record(make(tmp_path, "c.md", GOOD_PACK, AGENT_PACK)) == []


def test_short_body_rejected(tmp_path):
    assert "body" in rules(validate_record(make(tmp_path, "a.md", "# T\n", DOCTRINE)))


def test_doctrine_single_h1(tmp_path):
    text = "# One\n\n# Two\n\n## S\n\nBody text long enough to count as a body.\n"
    assert "h1" in rules(validate_record(make(tmp_path, "a.md", text, DOCTRINE)))


def test_doctrine_needs_section(tmp_path):
    text = "# One\n\nBody text long enough to count as a body, but no sections.\n"
    assert "sections" in rules(validate_record(make(tmp_path, "a.md", text, DOCTRINE)))


def test_intake_missing_keys(tmp_path):
    text = "---\ntitle: t\n---\n\n## S\n\nIntake body text long enough to count here.\n"
    problems = validate_record(make(tmp_path, "a.md", text, INTAKE))
    assert "front-matter" in rules(problems)
    assert any("source" in p.message for p in problems)


def test_intake_bad_status(tmp_path):
    text = GOOD_INTAKE.replace("status: intake", "status: wat")
    assert any("status" in p.message for p in validate_record(make(tmp_path, "a.md", text, INTAKE)))


def test_pack_needs_h1_and_sections(tmp_path):
    text = "Agent instructions long enough to count as a body, with no headings."
    problems = validate_record(make(tmp_path, "a.md", text, AGENT_PACK))
    assert {"h1", "sections"} <= rules(problems)


def test_broken_relative_link(tmp_path):
    text = GOOD_DOCTRINE + "\nSee [x](./missing-file.md).\n"
    problems = validate_record(make(tmp_path, "a.md", text, DOCTRINE))
    assert "link" in rules(problems)
    assert any("missing-file.md" in p.message for p in problems)


def test_duplicate_ids_in_repo(tmp_path):
    sub = tmp_path / "doctrines"
    sub.mkdir()
    (sub / "a.md").write_text(GOOD_DOCTRINE)
    other = tmp_path / "intake"
    other.mkdir()
    (other / "a.md").write_text(GOOD_INTAKE)
    from rig_doctrine.loader import load_repo as lr

    problems = validate_repo(lr(tmp_path))
    assert any(p.rule == "id" for p in problems)


def test_problem_str():
    assert "x.md" in str(Problem("x.md", "rule", "message"))


def test_bundled_corpus_validates_clean():
    """The schema checks run over the real repository on every test run."""
    problems = validate_repo(load_repo(ROOT))
    assert problems == [], [str(p) for p in problems]
