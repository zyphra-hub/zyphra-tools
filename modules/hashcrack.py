DESCRIPTION = "Hash Cracker (MD5/SHA1/SHA256/SHA512)"
def run():
    import hashlib
    
    hash_target = input("Hash target: ").strip()
    wordlist_path = input("Path wordlist: ")
    hash_type = input("Type (md5/sha1/sha256/sha512): ").lower()
    
    hash_len = len(hash_target)
    hash_map = {
        32: "md5",
        40: "sha1",
        64: "sha256",
        128: "sha512"
    }
    
    if not hash_type:
        hash_type = hash_map.get(hash_len, None)
        if hash_type:
            print(f"[*] Auto-detect: {hash_type}")
    
    if not hash_type:
        print("[!] Tidak bisa mendeteksi tipe hash.")
        return
    
    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            words = f.read().splitlines()
        
        print(f"[*] Mencoba {len(words)} kata...")
        for i, word in enumerate(words):
            if hash_type == "md5":
                h = hashlib.md5(word.encode()).hexdigest()
            elif hash_type == "sha1":
                h = hashlib.sha1(word.encode()).hexdigest()
            elif hash_type == "sha256":
                h = hashlib.sha256(word.encode()).hexdigest()
            elif hash_type == "sha512":
                h = hashlib.sha512(word.encode()).hexdigest()
            else:
                print("[!] Tipe hash tidak didukung.")
                return
            
            if h == hash_target:
                print(f"\n[+] PASSWORD DITEMUKAN: {word}")
                with open("cracked.txt", "w") as f:
                    f.write(f"{hash_target}:{word}")
                return
            
            if (i+1) % 1000 == 0:
                print(f"[*] Progress: {i+1}/{len(words)}")
        
        print("[-] Password tidak ditemukan di wordlist.")
    
    except FileNotFoundError:
        print("[!] File wordlist tidak ditemukan.")
