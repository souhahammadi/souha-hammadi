import streamlit as st
import requests

st.title("Explorateur de réseau")

with st.form("network_form"):
    network = st.text_input("Adresse réseau (ex: 192.168.10.0/26)")
    submitted = st.form_submit_button("Afficher les hôtes")

if submitted:
    try:
        response = requests.get(f"http://127.0.0.1:8000/hosts/custom?network={network}")
        data = response.json()
        
        st.write(f"**Réseau:** {data['network']}")
        st.write(f"**Nombre d'hôtes utilisables:** {data['total_hosts']}")
        st.write(f"**Passerelle:** {data['gateway']}")
        st.write(f"**Adresse broadcast:** {data['broadcast']}")
        
        st.write("**Liste des hôtes disponibles :**")
        for h in data["hosts"]:
            st.write(h)
    except Exception as e:
        st.error(f"Erreur: {e}")