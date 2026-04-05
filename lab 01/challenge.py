import socket
targets = input("Enter target IPs :")
ports = input("Enter ports : ")
targets_list = [t.strip() for t in targets.split(",")]
ports_list = [int(p.strip()) for p in ports.split(",")]
for target in targets_list:
    print(f"\nScanning {target}...\n")
    for port in ports_list:
        try:
            sock = socket.socket()
            socket.setdefaulttimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[OPEN] {target}:{port}")
                sock.close()
        except: 
            pass