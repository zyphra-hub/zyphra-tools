DESCRIPTION = "CMS Detector"
def run():
    import requests
    
    target = input("URL target (dengan http/https): ")
    
    cms_signatures = {
        "WordPress": {
            "paths": ["/wp-content/", "/wp-admin/", "/wp-includes/"],
            "headers": ["X-Powered-By"],
            "meta": ['name="generator" content="WordPress']
        },
        "Joomla": {
            "paths": ["/administrator/", "/components/", "/templates/"],
            "meta": ['name="generator" content="Joomla']
        },
        "Drupal": {
            "paths": ["/sites/default/", "/misc/drupal.js", "/themes/"],
            "meta": ['name="generator" content="Drupal']
        },
        "Laravel": {
            "paths": ["/vendor/", "/storage/"],
            "cookies": ["laravel_session"]
        },
        "Magento": {
            "paths": ["/skin/frontend/", "/magento_version"],
            "cookies": ["frontend"]
        }
    }
    
    print(f"\n[*] Mendeteksi CMS: {target}")
    
    for cms, sigs in cms_signatures.items():
        detected = False
        
        for path in sigs.get("paths", []):
            try:
                r = requests.get(target + path, timeout=5)
                if r.status_code in [200, 403, 301, 302]:
                    print(f"[+] {cms} terdeteksi: {path}")
                    detected = True
            except:
                pass
        
        try:
            r = requests.get(target, timeout=5)
            for meta in sigs.get("meta", []):
                if meta in r.text:
                    print(f"[+] {cms} terdeteksi via meta tag")
                    detected = True
            
            for cookie in sigs.get("cookies", []):
                if cookie in str(r.cookies):
                    print(f"[+] {cms} terdeteksi via cookie")
                    detected = True
        except:
            pass
    
    print("[+] Deteksi selesai.")
