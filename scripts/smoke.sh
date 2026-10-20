#!/usr/bin/env bash
# Smoke: the doctrine corpus must load and validate.
set -euo pipefail
cd "$(dirname "$0")/.."
PY="${PYTHON:-python3}"
if command -v rig-doctrine >/dev/null 2>&1; then
  rig-doctrine validate
else
  "$PY" -m rig_doctrine.cli validate
fi
echo "doctrine smoke PASS"
