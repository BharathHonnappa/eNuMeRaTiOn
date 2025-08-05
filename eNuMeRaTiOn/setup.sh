#!/bin/bash
echo "[*] Setting up eNuMeRaTiOn environment..."

# Check Python3
if ! command -v python3 &> /dev/null; then
    echo "[!] Python3 is not installed. Please install it first."
    exit 1
fi

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

echo "[+] Setup complete."
echo "[+] To run: source venv/bin/activate && ./generate_wordlist.sh"
