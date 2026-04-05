import socket
target = input ("enter traget IP:")
start_port = int(input("start port:"))
end_port = int(input("end port:"))
print(f"\nScanning {target} from port {start_port} to {end_port}...\n")
for port in range(start_port, end_port + 1):
    try:
        sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
             print(f"[OPEN] port {port}")
        sock.close()
    except KeyboardInterrupt:
        print("\nStopped by user")
        break
    except socket.error:
        print("Host not responding")
        break