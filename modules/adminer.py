DESCRIPTION = "Admin Page Finder"
def run():
    import requests
    import threading
    
    target = input("URL target (dengan http/https): ").rstrip("/")
    
    admin_paths = [
        "/admin", "/login", "/wp-admin", "/wp-login.php",
        "/administrator", "/panel", "/cp", "/cpanel",
        "/admin/login", "/admin/index.php", "/admin/admin",
        "/admincp", "/moderator", "/user/login", "/auth",
        "/dashboard", "/controlpanel", "/manage",
        "/backend", "/admin.php", "/login.php",
        "/signin", "/sign-in", "/log-in", "/adminarea",
        "/master", "/siteadmin", "/sysadmin", "/admin1",
        "/admin2", "/admin3", "/admin4", "/admin5",
        "/secure", "/webadmin", "/admin/login.php",
        "/admin/log-in.php", "/admin/signin.php",
        "/adminpanel", "/staff", "/staff/login",
        "/member", "/members", "/portal", "/acp",
        "/cms/admin", "/admin/account", "/admin.php3",
        "/admin.php4", "/admin.cgi", "/admin.html"
    ]
    
    print(f"[*] Mencari admin page di {target}...")
    found = []
    lock = threading.Lock()
    
    def check(path):
        url = target + path
        try:
            r = requests.get(url, timeout=5, allow_redirects=False)
            status = r.status_code
            if status in [200, 301, 302, 403]:
                with lock:
                    found.append(f"{url} [{status}]")
                    print(f"[+] {url} [{status}]")
        except:
            pass
    
    threads = []
    for path in admin_paths:
        t = threading.Thread(target=check, args=(path,))
        threads.append(t)
        t.start()
        
        if len(threads) >= 20:
            for t in threads:
                t.join()
            threads = []
    
    for t in threads:
        t.join()
    
    print(f"\n[+] Total ditemukan: {len(found)}")
    if found:
        with open(f"admin_{target.replace('://','_').replace('/','_')}.txt", "w") as f:
            for item in found:
                f.write(item + "\n")
