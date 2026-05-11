import ipaddress
from fastapi import FastAPI, HTTPException, Query
from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import srp

app = FastAPI(title="Network Tool API")

@app.get("/network/info")
def network_info(network: str = Query(..., description="Adresse réseau CIDR, ex: 192.168.1.0/24")):
    try:
        net = ipaddress.ip_network(network, strict=False)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Adresse réseau invalide : {e}")
    
    hosts_iter = list(net.hosts())
    gateway = str(hosts_iter[0]) if hosts_iter else None
    first_five = [str(h) for h in hosts_iter[:5]]

    return {
        "network_address": str(net.network_address),
        "broadcast_address": str(net.broadcast_address),
        "gateway": gateway,
        "num_hosts": len(hosts_iter),
        "hosts": first_five,
    }

@app.get("/mac")
def resolve_mac(ip: str = Query(..., description="Adresse IP cible, ex: 192.168.1.1")):
    # Validate IP format
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        raise HTTPException(status_code=400, detail="Adresse IP invalide")

    packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
    answered, _ = srp(packet, timeout=2, verbose=False)

    if not answered:
        raise HTTPException(status_code=404, detail="Host not found or unreachable")

    mac = answered[0][1].hwsrc
    return {"ip": ip, "mac": mac}