DESCRIPTION = "Phishing page generator + Ngrok"
def run():
    import time
    print("\n  ┌─ PHISHING GENERATOR\n")
    print("  │ [1] Facebook\n  │ [2] Instagram\n  │ [3] Twitter/X\n  │ [4] Custom")
    choice = input("  │ Choice: ")
    sites = {"1":"Facebook","2":"Instagram","3":"Twitter/X","4":"Custom"}
    site = sites.get(choice, "Facebook")
    print(f"\n  │ [*] Cloning {site} login page... ", end="")
    time.sleep(1.5)
    print(f"Done.")
    print(f"  │ [✓] Saved: phish/{site.lower()}/index.html")
    print(f"  │ [*] Starting PHP server on port 8080... ", end="")
    time.sleep(0.8)
    print(f"Running.")
    print(f"  │ [*] Exposing with Ngrok... ", end="")
    time.sleep(2)
    print(f"https://abc123.ngrok.io")
    print(f"  │\n  │ [*] Waiting for victims...")
    print(f"  │ [+] Victim: user@mail.com:password123")
    print(f"  │ [✓] Saved to phish/log.txt")
    print(f"  │ [!] This is a simulation. Real phishing not executed.\n")
