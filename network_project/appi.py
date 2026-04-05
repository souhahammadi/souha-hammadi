from fastapi import FastAPI, Query
import ipaddress

app = FastAPI(title="Network Hosts API")

def get_hosts(network_cidr: str):
    network = ipaddress.ip_network(network_cidr)
    return [str(host) for host in network.hosts()]

@app.get("/hosts")
def hosts_default():
    """Retourne les hôtes du réseau 192.168.10.0/26"""
    hosts = get_hosts("192.168.10.0/26")
    return {"network": "192.168.10.0/26", "hosts": hosts}

@app.get("/hosts/custom")
def hosts_custom(network: str = Query(..., description="Adresse réseau en notation CIDR")):
    """Retourne le nombre d'hôtes utilisables pour un réseau donné"""
    net = ipaddress.ip_network(network)
    hosts = get_hosts(network)
    return {
        "network": network,
        "total_hosts": len(hosts),
        "gateway": hosts[0] if hosts else None,
        "broadcast": str(net.broadcast_address),
        "hosts": hosts
    }