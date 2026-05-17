#!/usr/bin/env python3
# ZYPHRA TOOLS v2.0 (beta) - Simulasi
# Author: ndrael
import os, sys, time

R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
C = "\033[1;36m"
W = "\033[1;37m"
N = "\033[0m"

BANNER = f"""
{G} _____           _               
|__  /   _ _ __ | |__  _ __ __ _ 
  / / | | | '_ \\| '_ \\| '__/ _` |
 / /| |_| | |_) | | | | | | (_| |
/____\\__, | .__/|_| |_|_|  \\__,_|
     |___/|_| {W}by: ndrael{N}
"""

MODULES_DIR = "modules"

def load_modules():
    modules = {}
    if os.path.exists(MODULES_DIR):
        for file in os.listdir(MODULES_DIR):
            if file.endswith(".py") and file != "__init__.py":
                name = file[:-3]
                try:
                    mod = __import__(f"{MODULES_DIR}.{name}", fromlist=["run", "DESCRIPTION"])
                    modules[name] = mod
                except:
                    pass
    return modules

def show_main():
    os.system("clear")
    print(BANNER)
    print(f"  {W}Tools   = Zyphra-tools{N}")
    print(f"  {W}Version = 2.0 (beta){N}")
    print(f"  {G}Status  = Online{N}\n")
    print(f"  {W}[*] Type /menu for command list.{N}")
    print(f"  {W}[*] Type /help for assistance.{N}")

def show_menu():
    print(f"""
  {R}┌─ ATTACK:{N}
  {R}│{N} {W}/ddos          = UDP Flood + proxy rotation{N}
  {R}│{N} {W}/deface        = Mass deface upload exploit{N}
  {R}│{N} {W}/sql           = SQL injection auto exploit{N}
  {R}│{N} {W}/xss           = XSS scanner + cookie stealer{N}
  {R}│{N} {W}/brute         = Brute force login FB/IG{N}
  {R}│{N} {W}/phish         = Phishing page generator + Ngrok{N}
  {R}│{N} {W}/spam          = OTP bomber multi-platform{N}

  {Y}┌─ SPY:{N}
  {Y}│{N} {W}/ipinfo        = IP info + geolocation lookup{N}
  {Y}│{N} {W}/whois         = WHOIS domain lookup{N}
  {Y}│{N} {W}/dns           = DNS enumeration all records{N}
  {Y}│{N} {W}/subdomain     = Subdomain brute force finder{N}
  {Y}│{N} {W}/port          = Port scanner + service detect{N}
  {Y}│{N} {W}/cms           = CMS + technology detector{N}

  {C}┌─ SYSTEM:{N}
  {C}│{N} {W}/menu          = Show command list{N}
  {C}│{N} {W}/help          = Contact support{N}
  {C}│{N} {W}/clear         = Clear screen{N}
  {C}│{N} {W}/exit          = Exit bot{N}
""")

def show_help():
    print(f"""
  {W}Contact support:{N}
  Email: ndrael@proton.me

  atau buat issue di:
  https://github.com/zyphra-hub/zyphra-tools
""")

def main():
    show_main()
    modules = load_modules()

    while True:
        try:
            cmd = input(f"\n{W}┌─[zyphra@attacker]─[~]\n└──╼ ${N} ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{R}[!] Exiting...{N}")
            sys.exit(0)

        if cmd in ["/exit", "exit"]:
            print(f"{R}[!] Shutting down...{N}")
            time.sleep(0.5)
            sys.exit(0)
        elif cmd == "/clear":
            show_main()
        elif cmd == "/menu":
            show_menu()
        elif cmd == "/help":
            show_help()
        elif cmd.startswith("/"):
            cmd_name = cmd[1:]
            if cmd_name in modules:
                try:
                    modules[cmd_name].run()
                except Exception as e:
                    print(f"{R}[!] Error: {e}{N}")
            else:
                print(f"{R}[!] Unknown command. Type /menu{N}")
        else:
            print(f"{R}[!] Use '/' prefix. Example: /menu{N}")

if __name__ == "__main__":
    main()
