"""rig-doctrine: load, inspect and validate the doctrine repository.

Public API:
    load_repo(root)          -> Repo (all records + problems)
    validate_repo(root)      -> list[Problem]
    DoctrineRecord, Repo, Problem
"""

from .loader import Repo, load_repo
from .model import DoctrineRecord
from .validator import Problem, validate_record, validate_repo

__version__ = "0.1.0"

__all__ = [
    "DoctrineRecord",
    "Problem",
    "Repo",
    "__version__",
    "load_repo",
    "validate_record",
    "validate_repo",
]
