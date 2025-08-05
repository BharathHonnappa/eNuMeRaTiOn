#!/bin/bash
SCRIPT="main.py"

if [[ ! -f "$SCRIPT" ]]; then
    echo "[!] main.py not found in current directory!"
    exit 1
fi

# Activate venv if exists
if [[ -d "venv" ]]; then
    source venv/bin/activate
fi

python3 "$SCRIPT" "$@"

