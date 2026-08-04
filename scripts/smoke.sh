#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."; find . -name '*.md' ! -path './.git/*' | head -3 | grep -q .
echo "doctrine smoke PASS"
