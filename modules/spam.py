DESCRIPTION = "OTP bomber multi-platform"
def run():
    import time, sys
    print("\n  ┌─ OTP BOMBER\n")
    target = input("  │ Target number: ")
    count = int(input("  │ Count/platform: "))
    platforms = ["Facebook", "Instagram", "WhatsApp", "Telegram", "Shopee", "Tokopedia", "Gojek", "Grab", "Twitter/X", "TikTok"]
    print(f"\n  │ [*] Requesting OTP from {len(platforms)} platforms...")
    sent = 0
    for p in platforms:
        for i in range(count):
            sys.stdout.write(f"\r  │ [{p}] Sending OTP {i+1}/{count}...")
            sys.stdout.flush()
            time.sleep(0.15)
            sent += 1
    print(f"\n  │ [✓] {sent} OTP requests sent to {target}")
    print(f"  │ [!] This is a simulation. Real OTP not sent.\n")
