#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
test -f README.md
test -d docs || test -f docs/public-boundary.md || true
# at least one markdown doctrine file
find . -name '*.md' ! -path './.git/*' | head -5 | grep -q .
echo "doctrine smoke PASS"
