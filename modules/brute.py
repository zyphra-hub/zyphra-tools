DESCRIPTION = "Brute force login FB/IG"
def run():
    import time, sys, random
    print("\n  ┌─ BRUTE FORCE\n")
    target = input("  │ Email/User   : ")
    platform = input("  │ Platform (FB/IG): ")
    wordlist = input("  │ Wordlist path : ")
    total = 50  # simulasi
    print(f"\n  │ [*] Trying {total} passwords...")
    found = None
    for i in range(1, total+1):
        sys.stdout.write(f"\r  │ [{i}/{total}] Trying...")
        sys.stdout.flush()
        time.sleep(0.05)
        if i == random.randint(10, 40):
            found = "hunter2"
            break
    print(f"\n  │ [+] Password found: {found}")
    print(f"  │ [✓] Saved to found.txt")
    print(f"  │ [!] This is a simulation. Real brute force not executed.\n")
