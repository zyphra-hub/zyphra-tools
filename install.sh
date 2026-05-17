#!/bin/bash
# Zyphra Tools v2.0 - Universal Installer
# Support: Termux, Debian/Ubuntu, Arch Linux, Fedora

clear
echo "===================================="
echo "  Zyphra Tools v2.0 Installer"
echo "  Author: ndrael"
echo "===================================="
echo ""

# Deteksi OS
if [ -d "/data/data/com.termux" ]; then
    echo "[*] Termux detected."
    echo "[*] Updating packages..."
    pkg update -y && pkg upgrade -y
    echo "[*] Installing Python..."
    pkg install python -y
    PIP="pip"
    PYTHON="python"

elif [ -f "/etc/debian_version" ]; then
    echo "[*] Debian/Ubuntu detected."
    echo "[*] Updating packages..."
    sudo apt update && sudo apt upgrade -y
    echo "[*] Installing Python..."
    sudo apt install python3 python3-pip -y
    PIP="pip3"
    PYTHON="python3"

elif [ -f "/etc/arch-release" ]; then
    echo "[*] Arch Linux detected."
    echo "[*] Updating packages..."
    sudo pacman -Syu --noconfirm
    echo "[*] Installing Python..."
    sudo pacman -S python python-pip --noconfirm
    PIP="pip"
    PYTHON="python"

elif [ -f "/etc/fedora-release" ]; then
    echo "[*] Fedora detected."
    echo "[*] Updating packages..."
    sudo dnf update -y
    echo "[*] Installing Python..."
    sudo dnf install python3 python3-pip -y
    PIP="pip3"
    PYTHON="python3"

elif [ -f "/etc/redhat-release" ]; then
    echo "[*] RHEL/CentOS detected."
    echo "[*] Updating packages..."
    sudo yum update -y
    echo "[*] Installing Python..."
    sudo yum install python3 python3-pip -y
    PIP="pip3"
    PYTHON="python3"

elif [ -f "/etc/alpine-release" ]; then
    echo "[*] Alpine Linux detected."
    echo "[*] Updating packages..."
    apk update && apk upgrade
    echo "[*] Installing Python..."
    apk add python3 py3-pip
    PIP="pip3"
    PYTHON="python3"

elif [ "$(uname -s)" == "Darwin" ]; then
    echo "[*] macOS detected."
    echo "[*] Installing Python via Homebrew..."
    brew install python3
    PIP="pip3"
    PYTHON="python3"

else
    echo "[!] Unknown OS."
    echo "[!] Make sure Python 3 is installed."
    PIP="pip3"
    PYTHON="python3"
fi

echo ""
echo "[*] Upgrading pip..."
$PIP install --upgrade pip

echo "[*] Installing Python dependencies..."
$PIP install -r requirements.txt

echo "[*] Setting execute permission..."
chmod +x zyphra.py

echo ""
echo "===================================="
echo "  Installation Complete!"
echo "===================================="
echo ""
echo "  Run: $PYTHON zyphra.py"
echo ""
