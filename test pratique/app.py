#souha hammadi
import ipaddress 
network_input = input ("donner une adresse reseau : ")
try:
    network = ipaddress.ip_network(network_input)
    print("adresse valider")
    print ("adresse reseau : " network.network_address)
    print ("broadcast : " network.broadcast_address)
    host = liste (network.hosts())
    print("liste des hotes : ")
    for h in hosts:
       print (h)
       gateway = hosts[0]
       print ("gateway " gateway)
       with open ("result.txt" , "w") as f :
          f.write("address reseau " + str(network))
          f.write("hosts")
          for h in hosts:
             f.write(str(h))
             print("les address est enregistrer")
except:
    print("les address ne pas enregistrer ")
