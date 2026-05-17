DESCRIPTION = "IP info + geolocation lookup"
def run():
    import time
    print("\n  ┌─ IP INFO\n")
    ip = input("  │ IP target: ")
    print(f"\n  │ [*] Querying ip-api.com... ", end="")
    time.sleep(1)
    print(f"Done.\n")
    print(f"  │ IP          : {ip}")
    print(f"  │ Country     : United States (US)")
    print(f"  │ City        : Mountain View")
    print(f"  │ Region      : California")
    print(f"  │ ISP         : Google LLC")
    print(f"  │ Coordinates : 37.4056, -122.0775")
    print(f"  │ Timezone    : America/Los_Angeles")
    print(f"  │ [!] This is a simulation. Real lookup needs internet.\n")
