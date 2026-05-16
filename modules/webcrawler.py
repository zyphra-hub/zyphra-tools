DESCRIPTION = "Web Crawler & Link Extractor"
def run():
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin, urlparse
    import time
    
    target_url = input("URL target (dengan http/https): ")
    depth = int(input("Kedalaman crawl (1-3): ") or 1)
    
    visited = set()
    to_visit = [target_url]
    domain = urlparse(target_url).netloc
    all_links = []
    
    for current_depth in range(depth):
        next_to_visit = []
        print(f"\n[*] Depth {current_depth+1}: {len(to_visit)} URL")
        
        for url in to_visit:
            if url in visited:
                continue
            
            visited.add(url)
            try:
                r = requests.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
                soup = BeautifulSoup(r.text, "html.parser")
                
                for link in soup.find_all("a", href=True):
                    href = urljoin(url, link["href"])
                    if urlparse(href).netloc == domain and href not in visited:
                        next_to_visit.append(href)
                        all_links.append(href)
                        print(f"[+] {href}")
                
                time.sleep(0.5)
            except Exception as e:
                print(f"[-] Gagal: {url} | {e}")
        
        to_visit = list(set(next_to_visit))
    
    print(f"\n[+] Total link ditemukan: {len(all_links)}")
    with open(f"crawl_{domain}.txt", "w") as f:
        for link in all_links:
            f.write(link + "\n")
    print(f"[+] Tersimpan: crawl_{domain}.txt")
