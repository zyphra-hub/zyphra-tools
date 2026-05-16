DESCRIPTION = "IP Info Lookup"
def run():
    import requests
    
    ip = input("IP target: ")
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}?fields=66846719", timeout=10)
        data = r.json()
        
        if data.get("status") == "success":
            print(f"""
╔══════════════════════════════╗
║ IP INFO LOOKUP
╠══════════════════════════════╣
║ IP        : {data.get('query','?')}
║ Negara    : {data.get('country','?')} ({data.get('countryCode','?')})
║ Kota      : {data.get('city','?')}
║ Region    : {data.get('regionName','?')}
║ ISP       : {data.get('isp','?')}
║ Org       : {data.get('org','?')}
║ AS        : {data.get('as','?')}
║ Timezone  : {data.get('timezone','?')}
║ Lat/Lon   : {data.get('lat','?')}, {data.get('lon','?')}
║ ZIP       : {data.get('zip','?')}
╚══════════════════════════════╝
            """)
        else:
            print("[!] IP tidak valid atau limit API.")
    except Exception as e:
        print(f"[!] Error: {e}")
