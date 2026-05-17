DESCRIPTION = "Subdomain brute force finder"
def run():
    import time, sys, random
    print("\n  ┌─ SUBDOMAIN FINDER\n")
    domain = input("  │ Domain: ")
    total = 50
    found = 0
    print(f"\n  │ [*] Brute forcing {total} subdomains...")
    for i in range(1, total+1):
        sys.stdout.write(f"\r  │ [{i}/{total}] Testing...")
        sys.stdout.flush()
        time.sleep(0.04)
        if random.randint(1,10) > 7:
            found += 1
    print(f"\n  │ [✓] Found {found} subdomains.")
    print(f"  │ [!] This is a simulation. Real results may vary.\n")
