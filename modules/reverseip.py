DESCRIPTION = "Reverse IP Lookup"
def run():
    import requests
    
    ip = input("IP target: ")
    
    print(f"[*] Reverse IP: {ip}")
    
    # API 1: HackerTarget
    try:
        r = requests.get(f"https://api.hackertarget.com/reverseiplookup/?q={ip}", timeout=10)
        if r.status_code == 200 and "error" not in r.text.lower():
            print("\n[ HackerTarget Results ]")
            for line in r.text.strip().split("\n"):
                print(f"  -> {line}")
    except:
        print("[-] HackerTarget API gagal.")
    
    # API 2: YouGetSignal (mirror)
    try:
        r = requests.post(
            "https://domains.yougetsignal.com/domains.php",
            data={"remoteAddress": ip},
            timeout=10
        )
        data = r.json()
        if data.get("status") == "Success":
            print("\n[ YouGetSignal Results ]")
            print(f"  Total: {data.get('domainCount', 0)} domain")
            for domain in data.get("domainArray", []):
                print(f"  -> {domain[0]}")
    except:
        pass
