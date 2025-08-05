#!/bin/bash
set -e

echo "[!] ALERT: Unauthorized access detected!"
sleep 1
echo "[!] Injecting payload into system memory..."
sleep 1
echo "[!] Encrypting /home directory... (34%)"
sleep 1
echo "[!] Encrypting /home directory... (67%)"
sleep 1
echo "[!] Encryption complete. Sending decryption key to remote server..."
sleep 1
echo "[!] Attempting privilege escalation... [ROOT ACCESS GRANTED]"
sleep 1
echo "[!] Uploading sensitive files to darknet market... [OK]"
sleep 1
echo "[!] System lockdown initiated. You have 60 seconds to cancel!"
sleep 2
echo "[✔] Just kidding... Setting up environment now 😂"
sleep 1

echo "[*] Setting up eNuMeRaTiOn environment..."

if ! command -v python3 &> /dev/null; then
    echo "[!] Python3 is not installed. Please install it first."
    exit 1
fi

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip

echo "[+] Setup complete."
echo "[+] To run: source venv/bin/activate && ./generate_wordlist.sh"
