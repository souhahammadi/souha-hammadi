import ipaddress

def generate_hosts(network_cidr="192.168.10.0/26"):
    network = ipaddress.ip_network(network_cidr)
    hosts_list = [str(host) for host in network.hosts()]

    print("Les hôtes disponibles :")
    for host in hosts_list:
        print(host)
 
    with open("hosts.txt", "w") as f:
        for host in hosts_list:
            f.write(host + "\n")
    
    return hosts_list

if __name__ == "__main__":
    generate_hosts()