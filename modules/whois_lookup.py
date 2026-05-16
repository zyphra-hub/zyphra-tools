DESCRIPTION = "WHOIS Lookup"
def run():
    try:
        import whois
    except:
        print("[!] Install: pip install python-whois")
        return
    
    domain = input("Domain target (contoh: google.com): ")
    
    try:
        w = whois.whois(domain)
        print(f"\n[ WHOIS: {domain} ]")
        print(f"Domain Name : {w.domain_name}")
        print(f"Registrar   : {w.registrar}")
        print(f"WHOIS Server: {w.whois_server}")
        print(f"Creation    : {w.creation_date}")
        print(f"Expiration  : {w.expiration_date}")
        print(f"Updated     : {w.updated_date}")
        print(f"Name Servers: {w.name_servers}")
        print(f"Status      : {w.status}")
        print(f"Emails      : {w.emails}")
        print(f"Organization: {w.org}")
        print(f"Country     : {w.country}")
    except Exception as e:
        print(f"[!] Gagal: {e}")
