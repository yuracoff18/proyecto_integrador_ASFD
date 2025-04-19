import streamlit as st
from src.funciones import register 
st.title("Registrar usuario")

with st.form("Registro"):
    nuevo_usuario = st.text_input("Usuario")
    contraseña = st.text_input("Contraseña", type="password")
    conf_contraseña = st.text_input("Confirmar contraseña", type="password")
    register_button = st.form_submit_button("Registrar")


if register_button:
   register(nuevo_usuario, contraseña, conf_contraseña) 
