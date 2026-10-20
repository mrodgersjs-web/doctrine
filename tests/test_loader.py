from pathlib import Path

from rig_doctrine.loader import first_h1, load_repo, parse_front_matter, relative_links
from rig_doctrine.model import AGENT_PACK, DOCTRINE, INTAKE

ROOT = Path(__file__).resolve().parents[1]


def test_parse_front_matter_absent():
    data, body = parse_front_matter("# title\nbody")
    assert data == {} and body.startswith("# title")


def test_parse_front_matter_values():
    data, body = parse_front_matter(
        '---\ntitle: "Quoted"\nstatus: intake\npromoted_to: null\n---\nbody'
    )
    assert data == {"title": "Quoted", "status": "intake", "promoted_to": None}
    assert body == "body"


def test_first_h1():
    assert first_h1("# Head\n") == "Head"
    assert first_h1("no heading") is None


def test_relative_links_filter_remote():
    body = "[a](./x.md) [b](https://example.com) [c](#anchor) [d](../y/z.md)"
    assert relative_links(body) == ["./x.md", "../y/z.md"]


def test_load_repo_counts():
    repo = load_repo(ROOT)
    counts = repo.counts()
    assert counts[DOCTRINE] >= 15
    assert counts[INTAKE] == 10
    assert counts[AGENT_PACK] == 5


def test_find_by_id_and_filename():
    repo = load_repo(ROOT)
    assert repo.find("gate-d").title.startswith("GATE-D")
    assert repo.find("GATE-D.md") is not None
    assert repo.find("missing") is None


def test_intake_title_from_front_matter():
    repo = load_repo(ROOT)
    record = repo.find("design-studio-taste-intake")
    assert record.kind == INTAKE
    assert record.title.startswith("Intake:")


def test_load_record_missing_file(tmp_path):
    import pytest

    from rig_doctrine.loader import load_record as lr

    with pytest.raises(OSError):
        lr(tmp_path / "nope.md", AGENT_PACK)
