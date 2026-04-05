import streamlit as st

st.title("Mon App Streamlit")
name = st.text_input("Ton nom :")
if st.button("Dis Bonjour"):
    st.write(f"Bonjour {name} !")