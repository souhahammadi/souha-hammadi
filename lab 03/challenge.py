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