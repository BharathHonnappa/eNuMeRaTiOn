#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR" || exit 1

if [[ ! -f "main.py" ]]; then
    echo "[!] main.py not found! Exiting..."
    exit 1
fi

echo "[*] Launching eNuMeRaTiOn..."
python3 main.py
