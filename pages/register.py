import streamlit as st
from src.funciones import register 

st.image("assets/logo.png", use_container_width=True)

st.title("Registrar usuario")

with st.form("Registro"):
    nuevo_usuario = st.text_input("Usuario")
    contraseña = st.text_input("Contraseña", type="password")
    conf_contraseña = st.text_input("Confirmar contraseña", type="password")
    left, right = st.columns(2)
    register_button = left.form_submit_button("Registrar", use_container_width=True)
    volver = right.form_submit_button("Volver", use_container_width=True)


if volver:
    st.switch_page("main.py")

if register_button:
   register(nuevo_usuario, contraseña, conf_contraseña) 
