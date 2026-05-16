#!/bin/bash
echo "[*] Installing Zyphra Tools..."
pkg update -y && pkg upgrade -y
pkg install python -y
pkg install git -y
pip install --upgrade pip
pip install -r requirements.txt
chmod +x zyphra.py
echo "[+] Installation complete!"
echo "[+] Run: python zyphra.py"
