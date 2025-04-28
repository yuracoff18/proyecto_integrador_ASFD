import streamlit as st
from src import funciones


def main():
    
    st.image("assets/logo.png", use_container_width=True)

    st.title("Inicio de sesion")

    with st.form("Inicio de sesion"):
        usuario = st.text_input("",placeholder="Usuario")
        contraseña = st.text_input("", placeholder="Contraseña")

        login_button = st.form_submit_button("Iniciar sesion")

        register_button = st.form_submit_button("Registrar usuario")


    if register_button:
        st.switch_page("pages/register.py")

    if login_button:
        funciones.login(usuario, contraseña)


if __name__ == "__main__":
    main()
