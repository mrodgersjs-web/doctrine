import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def test_runnable_example_passes():
    """examples/validate_repo.py is executed as part of the suite."""
    result = subprocess.run(
        [sys.executable, str(REPO / "examples" / "validate_repo.py")],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "doctrine corpus OK" in result.stdout
