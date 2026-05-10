@app.get("/gateway/")
def get_gateway (network:str):
    try:
        net = ipaddress.ip_network(network)
        hosts = list(net.hosts())
        gateway =str (hosts[0])