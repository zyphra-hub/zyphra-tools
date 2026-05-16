DESCRIPTION = "Port Scanner Cepat"
def run():
    import socket, threading
    
    target = input("Target IP/Domain: ")
    start_port = int(input("Port awal (default 1): ") or 1)
    end_port = int(input("Port akhir (default 1024): ") or 1024)
    
    print(f"[*] Scanning {target} [{start_port}-{end_port}]...")
    open_ports = []
    
    def scan(port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        if sock.connect_ex((target, port)) == 0:
            open_ports.append(port)
            print(f"[+] OPEN: {port}")
        sock.close()
    
    threads = []
    for port in range(start_port, end_port+1):
        t = threading.Thread(target=scan, args=(port,))
        threads.append(t)
        t.start()
        
        if len(threads) >= 50:
            for t in threads:
                t.join()
            threads = []
    
    for t in threads:
        t.join()
    
    print(f"\n[+] Total port terbuka: {len(open_ports)}")
    print(f"[+] List: {open_ports}")
