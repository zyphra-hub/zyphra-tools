DESCRIPTION = "DNS enumeration all records"
def run():
    import time, sys
    print("\n  ┌─ DNS ENUMERATION\n")
    domain = input("  │ Domain: ")
    records = ["A", "AAAA", "MX", "NS", "TXT", "CNAME", "SOA", "SRV", "CAA"]
    print(f"\n  │ [*] Querying {len(records)} record types...")
    for r in records:
        sys.stdout.write(f"\r  │ [*] Fetching {r} record...")
        sys.stdout.flush()
        time.sleep(0.25)
    print(f"\n  │ [✓] Done.\n")
    print(f"  │ [A]     : 142.250.80.46")
    print(f"  │ [AAAA]  : 2404:6800:4003:c00::46")
    print(f"  │ [MX]    : smtp.{domain} (10)")
    print(f"  │ [NS]    : ns1.{domain}")
    print(f"  │ [TXT]   : v=spf1 include:_spf.{domain} ~all")
    print(f"  │ [✓] All records fetched.")
    print(f"  │ [!] This is a simulation. Real DNS needs internet.\n")
