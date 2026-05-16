DESCRIPTION = "DNS Enumeration"
def run():
    try:
        import dns.resolver
    except:
        print("[!] Install: pip install dnspython")
        return
    
    domain = input("Domain target: ")
    record_types = ["A", "AAAA", "MX", "NS", "TXT", "CNAME", "SOA", "SRV", "CAA"]
    
    print(f"\n[ DNS LOOKUP: {domain} ]")
    for rtype in record_types:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            print(f"\n[{rtype}]")
            for ans in answers:
                print(f"  -> {ans.to_text()}")
        except dns.resolver.NoAnswer:
            print(f"[{rtype}] No records")
        except dns.resolver.NXDOMAIN:
            print(f"[{rtype}] Domain tidak ada")
            break
        except Exception as e:
            print(f"[{rtype}] Error: {e}")
