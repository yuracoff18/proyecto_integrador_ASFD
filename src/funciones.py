import streamlit as st
import pandas as pd
import os
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
        "Jan": "01",
        "Feb": "02",
        "Mar": "03",
        "Apr": "04",
        "May": "05",
        "Jun": "06",
        "Jul": "07",
        "Aug": "08",
        "Sep": "09",
        "Oct": "10",
        "Nov": "11",
        "Dec": "12"
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


def guardar_precio(precio_p, precio_c):
    with open("data/precios.txt", "w") as precios:
        precios.write(f"{precio_p},{precio_c}\n")
        precios.close()
        return

def cargar_precios():
    with open("data/precios.txt", "r") as precios:
        ans = precios.readline().split(",")
        return ans



def cargar_tabla_ventas(nombre, cantidad, nombre_producto):
    local = time.asctime()
    local = local.split()
    local[0] = days[local[0]]
    local[1] = months[local[1]]
    true_local = [local[i] for i in [0,1,2,4]]

    # Fecha actual organizada Año-mes-dia
    time_data = f"{true_local[3]}-{true_local[1]}-{true_local[2]}"

    nueva_compra = {
        "nombre_cliente": nombre,
        "dia": true_local[0],
        "fecha": time_data,
        "producto": nombre_producto,
        "cantidad": cantidad,
            }

    df = pd.DataFrame([nueva_compra])
    df['fecha'] = pd.to_datetime(df['fecha'])
    path_csv = 'data/compras.csv'
    if not os.path.isfile(path_csv):
        df.to_csv(path_csv, index=False)
    else:
        df.to_csv(path_csv, mode='a', header=False, index=False)
    return
