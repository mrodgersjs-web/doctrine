#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

find . -name '*.md' ! -path './.git/*' | head -3 | grep -q .

echo "validating orchestration example flows:"
python3 examples/orchestration/validate_flows.py

echo "doctrine smoke PASS"
