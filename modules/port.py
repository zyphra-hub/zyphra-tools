DESCRIPTION = "Port scanner + service detect"
def run():
    import time, sys, random
    print("\n  ┌─ PORT SCANNER\n")
    target = input("  │ Target: ")
    start = int(input("  │ Start port: ") or 1)
    end = int(input("  │ End port: ") or 1024)
    total = end - start + 1
    open_ports = []
    print(f"\n  │ [*] Scanning {total} ports...")
    for port in range(start, end+1):
        sys.stdout.write(f"\r  │ [*] Port {port}/{end}...")
        sys.stdout.flush()
        time.sleep(0.005)
        if random.randint(1, 100) <= 3:
            open_ports.append(port)
    print(f"\n  │ [✓] {len(open_ports)} ports open.")
    for p in open_ports[:10]:
        print(f"  │     {p}")
    if len(open_ports) > 10:
        print(f"  │     ... and {len(open_ports)-10} more")
    print(f"  │ [!] This is a simulation. Real scan may differ.\n")
