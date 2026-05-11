from scapy.all import ARP, Ether, srp
import sys

def scan(cidr):
    print(f"\nScan réseau : {cidr}\n")

    packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=cidr)

    result = srp(packet, timeout=1, verbose=0)[0]

    print("IP Address\t\tMAC Address")
    print("-" * 40)

    for sent, received in result:
        print(f"{received.psrc}\t\t{received.hwsrc}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python3 arp_scan.py 192.168.1.0/24")
    else:
        scan(sys.argv[1])