DESCRIPTION = "WHOIS domain lookup"
def run():
    import time
    print("\n  ┌─ WHOIS LOOKUP\n")
    domain = input("  │ Domain: ")
    print(f"\n  │ [*] Querying WHOIS... ", end="")
    time.sleep(1.5)
    print(f"Done.\n")
    print(f"  │ Domain      : {domain}")
    print(f"  │ Registrar   : MarkMonitor Inc.")
    print(f"  │ Creation    : 1997-09-15")
    print(f"  │ Expiration  : 2028-09-14")
    print(f"  │ Name Server : ns1.{domain}")
    print(f"  │ Organization: Google LLC")
    print(f"  │ Country     : US")
    print(f"  │ [!] This is a simulation. Real WHOIS needs internet.\n")
