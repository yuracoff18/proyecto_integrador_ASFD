import streamlit as st
import json
import time

# ---------------------------------------------------------
# Diccionarios
days = {
        "Mon": "Lun",
        "Tue": "Mar",
        "Wed": "Mie",
        "Thu": "Jue",
        "Fra": "Vie",
        "Sut": "Sab",
        "Sun": "Dom"
        }

months = {
        "Jan": "Ene",
        "Feb": "Feb",
        "Mar": "Mar",
        "Apr": "Abr",
        "May": "May",
        "Jun": "Jun",
        "Jul": "Jul",
        "Aug": "Ago",
        "Sep": "Sep",
        "Oct": "Oct",
        "Nov": "Nov",
        "Dec": "Dic"
        }
# ----------------------------------------------------------


# Funcion de login en main.py
def login(usuario: str, contraseña: str):
    with open("data/usuarios.txt", "r") as usuarios:
        for l in usuarios:
            l = l.strip()
            if l == f"{usuario},{contraseña}":
                usuarios.close()
                st.switch_page("pages/menu.py")
    st.error("Usuario no encontrado")
    return

# Funcion de registro en register.py
def register(usuario: str, contraseña: str, conf: str):
    if contraseña != conf:
        st.error("Las contraseñas no coinciden")
        return

    with open("data/usuarios.txt", "r") as usuarios_r:
        for l in usuarios_r:
            l = l.strip()
            if l.startswith(f"{usuario},"):
                st.error("Usuario ya registrado")
                return

    # Si no está registrado:
    with open("data/usuarios.txt", "a") as usuarios:
        usuarios.write(f"{usuario},{contraseña}\n")
    st.switch_page("main.py")

# FUncion para cargar las configuraciones hechas previamente
def cargar_opciones():
    configuraciones = []
    with open("data/parametros.txt", "r") as config:
        configuraciones = config.readline().split(",")
        config.close()
        return configuraciones

# Funcion de guardar parametros de creacion de pandebono y croissant
def guardar_opciones(queso_p, azucar_p, almidon_p, masa_p, mantequilla_p, leche_p, queso_c, azucar_c, almidon_c, masa_c, mantequilla_c, leche_c):
    with open("data/parametros.txt", "w") as parametros:
        parametros.write(f"{queso_p}, {azucar_p}, {almidon_p}, {masa_p}, {mantequilla_p}, {leche_p}, {queso_c}, {azucar_c}, {almidon_c}, {masa_c}, {mantequilla_c}, {leche_c}\n")
        parametros.close()
        st.success("Se guardaron las configuraciones")
        return

    
# Funcion de guardar parametros de creacion de pandebono y croissant
def guardar_opciones_json(queso_p, azucar_p, almidon_p, masa_p, mantequilla_p, leche_p, queso_c, azucar_c, almidon_c, masa_c, mantequilla_c, leche_c):
    ingredientes = {
                "q_p": queso_p,
                "a_p": azucar_p,
                "al_p": almidon_p,
                "m_p": masa_p,
                "man_p": mantequilla_p,
                "l_p": leche_p,
                "q_c": queso_c,
                "a_c": azucar_c,
                "al_c": almidon_c,
                "m_c": masa_c,
                "man_c": mantequilla_c,
                "l_c": leche_c,
            }
    with open("data/ingredientes.txt", "w") as parametros:
        parametros.write(json.dumps(ingredientes))
        parametros.close()
        st.success("Se guardaron las configuraciones")
        return


def cargar_configuraciones_json():
    with open("data/ingredientes.txt", "r") as parametros:
        configuraciones = json.loads(parametros.readline())
        parametros.close()
        return configuraciones

