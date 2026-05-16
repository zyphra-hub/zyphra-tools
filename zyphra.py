#!/usr/bin/env python3
# ZYPHRA TOOLS v1.0 - Attacker Bot
# Author: ndrael
import os, sys, importlib, time, subprocess

R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
C = "\033[1;36m"
W = "\033[1;37m"
N = "\033[0m"

BANNER = f"""
{C} _____           _               ____   ___ _____ 
|__  /   _ _ __ | |__  _ __ __ _| __ ) / _ \\_   _|
  / / | | | '_ \\| '_ \\| '__/ _` |  _ \\| | | || |  
 / /| |_| | |_) | | | | | | (_| | |_) | |_| || |  
/____\\__, | .__/|_| |_|_|  \\__,_|____/ \\___/ |_|  
     |___/|_|                                     {N}
"""

BOX = f"""
{R}╔══════════════════════════════════════════════════╗
║         ZYPHRA TOOLS v1.0 - ATTACKER BOT        ║
╠══════════════════════════════════════════════════╣
║  AUTHOR   : ndrael                              ║
║  TYPE     : Multi-Attack Bot                    ║
║  MODULES  : 22 loaded                           ║
║  STATUS   : Ready                               ║
╚══════════════════════════════════════════════════╝{N}
"""

MODULES_DIR = "modules"

def load_modules():
    modules = {}
    if not os.path.exists(MODULES_DIR):
        os.mkdir(MODULES_DIR)
    for file in os.listdir(MODULES_DIR):
        if file.endswith(".py") and file != "__init__.py":
            name = file[:-3]
            try:
                mod = importlib.import_module(f"{MODULES_DIR}.{name}")
                modules[name] = mod
            except Exception as e:
                pass
    return modules

def show_help(modules):
    print(f"\n{Y}[ COMMAND LIST ]{N}\n")
    attack_cmds = {
        "/ddos": "Serangan DoS ke target",
        "/spam": "Spam SMS/WA/Call",
        "/phish": "Generate halaman phising",
        "/deface": "Mass deface situs vuln",
        "/brute": "Brute force login",
        "/dork": "Google dorking",
        "/sql": "SQL injection scanner",
        "/xss": "XSS scanner & inject",
        "/port": "Port scanner cepat",
        "/ipinfo": "Info lengkap IP target",
        "/whois": "WHOIS lookup domain",
        "/dnslookup": "DNS enumeration",
        "/subdomain": "Cari subdomain",
        "/cmsdetect": "Deteksi CMS target",
        "/adminer": "Cari admin page",
        "/reverseip": "Reverse IP lookup",
        "/webcrawler": "Crawling situs",
        "/bomber": "Email bomber massal",
        "/hashcrack": "Crack hash",
        "/payload": "Generate backdoor",
        "/info": "Info sistem",
    }
    sys_cmds = {
        "/help": "Tampilkan ini",
        "/menu": "Menu interaktif",
        "/clear": "Bersihkan layar",
        "/exit": "Keluar",
    }
    print(f"{R}[ ATTACK COMMANDS ]{N}")
    for cmd, desc in attack_cmds.items():
        print(f"  {G}{cmd:<15}{N} - {desc}")
    print(f"\n{Y}[ SYSTEM COMMANDS ]{N}")
    for cmd, desc in sys_cmds.items():
        print(f"  {G}{cmd:<15}{N} - {desc}")
    print()

def main():
    os.system("clear")
    print(BANNER)
    print(BOX)
    print(f"{G}[ INFO ] Bot siap menerima perintah{N}")
    print(f"{G}[ INFO ] Ketik /help untuk daftar command{N}")
    print(f"{G}[ INFO ] Ketik /menu untuk menu interaktif{N}\n")
    
    modules = load_modules()

    while True:
        try:
            cmd = input(f"{W}┌─[zyphra@attacker]─[~]\n└──╼ ${N} ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{R}[!] Keluar...{N}")
            sys.exit(0)

        if cmd in ["/exit", "exit"]:
            print(f"{R}[!] Mematikan Zyphra...{N}")
            time.sleep(0.5)
            sys.exit(0)
        elif cmd == "/clear":
            os.system("clear")
            print(BANNER)
            print(BOX)
        elif cmd == "/help":
            show_help(modules)
        elif cmd == "/menu":
            show_help(modules)
        elif cmd == "/info":
            if "info" in modules:
                modules["info"].run()
            else:
                print(f"{R}[!] Modul info rusak{N}")
        elif cmd.startswith("/"):
            cmd_name = cmd[1:]
            if cmd_name in modules:
                try:
                    modules[cmd_name].run()
                except Exception as e:
                    print(f"{R}[!] Error: {e}{N}")
            else:
                print(f"{R}[!] Command tidak dikenal. Ketik /help{N}")
        else:
            print(f"{R}[!] Gunakan awalan '/' {N}")

if __name__ == "__main__":
    main()
