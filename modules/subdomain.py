DESCRIPTION = "Subdomain Finder"
def run():
    import requests
    import threading
    
    domain = input("Domain target (contoh: google.com): ")
    wordlist_path = "wordlists/subdomains.txt"
    
    try:
        with open(wordlist_path, "r") as f:
            subs = f.read().splitlines()
    except FileNotFoundError:
        print("[!] wordlists/subdomains.txt tidak ada. Membuat default...")
        import os
        os.makedirs("wordlists", exist_ok=True)
        default_subs = ["www","mail","ftp","admin","blog","shop","api","dev","test","staging","portal","remote","secure","vpn","cdn","webmail","smtp","pop","ns1","ns2"]
        with open(wordlist_path, "w") as f:
            for s in default_subs:
                f.write(s + "\n")
        subs = default_subs
    
    print(f"[*] Mencari {len(subs)} subdomain...")
    found = []
    lock = threading.Lock()
    
    def check(sub):
        url = f"http://{sub}.{domain}"
        try:
            r = requests.get(url, timeout=3, headers={"User-Agent": "Mozilla/5.0"})
            with lock:
                found.append(f"{url} [{r.status_code}]")
                print(f"[+] {url} [{r.status_code}]")
        except:
            pass
    
    threads = []
    for sub in subs:
        t = threading.Thread(target=check, args=(sub,))
        threads.append(t)
        t.start()
        
        if len(threads) >= 20:
            for t in threads:
                t.join()
            threads = []
    
    for t in threads:
        t.join()
    
    print(f"\n[+] Ditemukan: {len(found)} subdomain")
    with open(f"subdomain_{domain}.txt", "w") as f:
        for item in found:
            f.write(item + "\n")
    print(f"[+] Tersimpan: subdomain_{domain}.txt")
