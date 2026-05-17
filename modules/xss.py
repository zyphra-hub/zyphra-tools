DESCRIPTION = "XSS scanner + cookie stealer"
def run():
    import time, sys
    print("\n  ┌─ XSS SCANNER\n")
    target = input("  │ Target URL   : ")
    payloads = [
        "<script>alert(1)</script>",
        "\"><script>alert(1)</script>",
        "<img src=x onerror=alert(1)>",
        "<svg onload=alert(1)>",
        "'><script>alert(1)</script>",
        "javascript:alert(1)",
        "<body onload=alert(1)>"
    ]
    print(f"\n  │ [*] Testing {len(payloads)} payloads...")
    vuln = []
    for i, p in enumerate(payloads):
        sys.stdout.write(f"\r  │ [*] Payload {i+1}/{len(payloads)}...")
        sys.stdout.flush()
        time.sleep(0.3)
        if i % 2 == 0:
            vuln.append(p)
    print(f"\n  │ [+] {len(vuln)} vulnerabilities found.")
    print(f"  │ [*] Injecting cookie stealer... ", end="")
    time.sleep(1)
    print(f"Done.")
    print(f"  │ [+] Cookie: PHPSESSID=abc123def456")
    print(f"  │ [✓] Saved to cookies.txt")
    print(f"  │ [!] This is a simulation. Real XSS not executed.\n")
