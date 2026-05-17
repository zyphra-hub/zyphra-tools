DESCRIPTION = "System Information"
def run():
    import platform, os, socket, sys
    
    print(f"""
╔══════════════════════════════════╗
║ SYSTEM INFORMATION
╠══════════════════════════════════╣
║ OS        : {platform.system()} {platform.release()}
║ Kernel    : {platform.version()}
║ Arch      : {platform.machine()}
║ Hostname  : {socket.gethostname()}
║ IP Local  : {socket.gethostbyname(socket.gethostname())}
║ User      : {os.getlogin()}
║ Directory : {os.getcwd()}
║ Python    : {sys.version.split()[0]}
╚══════════════════════════════════╝
    """)
