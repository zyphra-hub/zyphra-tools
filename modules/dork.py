DESCRIPTION = "Google Dork Scraper"
def run():
    import requests
    from bs4 import BeautifulSoup
    
    dork = input("Dork query: ")
    pages = int(input("Jumlah halaman (1-5): "))
    
    print(f"[*] Mencari: {dork}")
    for page in range(pages):
        start = page * 10
        url = f"https://www.google.com/search?q={dork}&start={start}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36"
        }
        try:
            r = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(r.text, "html.parser")
            for link in soup.find_all("a"):
                href = link.get("href", "")
                if "/url?q=" in href and "webcache" not in href:
                    clean = href.split("/url?q=")[1].split("&")[0]
                    print(f"[+] {clean}")
        except Exception as e:
            print(f"[!] Error halaman {page+1}: {e}")
