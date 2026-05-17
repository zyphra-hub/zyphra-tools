#!/bin/bash

# ====================================
# Zyphra Tools v2.0 Installer
# Author: ndrael
# ====================================

clear

GREEN='\033[0;32m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${CYAN}"
echo "===================================="
echo "     Zyphra Tools v2.0 Installer"
echo "===================================="
echo -e "${NC}"

# Check requirements.txt
if [ ! -f "requirements.txt" ]; then
    echo -e "${RED}[!] requirements.txt not found.${NC}"
    exit 1
fi

# OS Detection
if [ -d "/data/data/com.termux" ]; then

    echo -e "${GREEN}[*] Termux detected.${NC}"

    pkg update -y && pkg upgrade -y
    pkg install python git -y

    PYTHON="python"
    PIP="pip"

elif [ -f "/etc/debian_version" ]; then

    echo -e "${GREEN}[*] Debian / Ubuntu detected.${NC}"

    sudo apt update && sudo apt upgrade -y
    sudo apt install python3 python3-pip git -y

    PYTHON="python3"
    PIP="pip3"

elif [ -f "/etc/arch-release" ]; then

    echo -e "${GREEN}[*] Arch Linux detected.${NC}"

    sudo pacman -Syu --noconfirm
    sudo pacman -S python python-pip git --noconfirm

    PYTHON="python"
    PIP="pip"

elif [ -f "/etc/fedora-release" ]; then

    echo -e "${GREEN}[*] Fedora detected.${NC}"

    sudo dnf update -y
    sudo dnf install python3 python3-pip git -y

    PYTHON="python3"
    PIP="pip3"

elif [ -f "/etc/alpine-release" ]; then

    echo -e "${GREEN}[*] Alpine Linux detected.${NC}"

    apk update && apk upgrade
    apk add python3 py3-pip git

    PYTHON="python3"
    PIP="pip3"

elif [ "$(uname -s)" == "Darwin" ]; then

    echo -e "${GREEN}[*] macOS detected.${NC}"

    if ! command -v brew &> /dev/null; then
        echo -e "${RED}[!] Homebrew not installed.${NC}"
        echo "Install Homebrew first:"
        echo "/bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
        exit 1
    fi

    brew install python3 git

    PYTHON="python3"
    PIP="pip3"

else

    echo -e "${RED}[!] Unsupported OS.${NC}"
    exit 1

fi

echo ""
echo -e "${GREEN}[*] Installing dependencies...${NC}"

$PYTHON -m pip install --upgrade pip
$PYTHON -m pip install -r requirements.txt

echo ""
echo -e "${GREEN}[✓] Installation complete!${NC}"
echo ""
echo "Run the tool with:"
echo ""
echo "    $PYTHON zyphra.py"
echo ""
