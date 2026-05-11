import streamlit as st 
import requests 
import pandas as pd 

API_BASE = "http://localhost:8000"

st.set_page_config(page_title="Network Tool")
st.title("Network Tool")

st.header("Analyse de réseau")
cidr_input = st.text_input (
    "address reseau CIDR"
     placeholder="ex : 192.168.1.0/24",
)

if st.button("analyser"):
    try:
        r = request.get(
            f"{API_BASE}/network/info",
            params={"network":cidr}
        )
        if r.status_code == 200:
            data = r.json()
            st.success("analyse reussie")
            st.write("informations")
            st.write(f"Adresse réseau : {data['network_address']}")
            st.write(f"Broadcast : {data['broadcast_address']}")
            st.write(f"Passerelle : {data['gateway']}")
            st.write(f"Nombre d'hôtes : {data['num_hosts']}")
            st.write("premieres address")
            df = pd.DataFrame(data["hosts"], columns=["IP"])
            st.dataframe(df)
        else:
          st.error("addresse invalide")

    except:
        st.error("imposible de contacter l'API")
        st.header("Résolution MAC")
        ip = st.text_input("Adresse IP", placeholder="192.168.1.1")
        if st.button("Résoudre"):
             try:
                r = requests.get(
            f"{API_BASE}/mac",
            params={"ip": ip}
        )
                if r.status_code == 200:
                  data = r.json()
                  st.success("MAC trouvée")
                  st.write(f"IP : {data['ip']}")
                  st.write(f"MAC : {data['mac']}")
                else:
                   st.error("Hôte introuvable")
             except:
                st.error("Impossible de contacter l'API")