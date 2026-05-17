DESCRIPTION = "System information"
def run():
    import platform, os, socket
    print(f"""
  ┌─ SYSTEM INFO
  │ OS        : {platform.system()} {platform.release()}
  │ Arch      : {platform.machine()}
  │ Hostname  : {socket.gethostname()}
  │ User      : {os.getlogin()}
  │ Directory : {os.getcwd()}
""")
