import streamlit as st
import time
from src.funciones import cargar_tabla_ventas

# Limpieza de inputs si venimos de un "guardar"
if st.session_state.get("limpiar_campos", False):
    for key in [
        "nombre_cliente_pandebono", "cantidad_pandebonos", 
        "nombre_cliente_croissant", "cantidad_croissants"
    ]:
        st.session_state[key] = ""
    st.session_state["limpiar_campos"] = False





st.markdown("<h1 style='text-align: center; margin-bottom: 20px;'>Ingreso de ventas</h1>", unsafe_allow_html=True)

left, right = st.columns(2)

nombre_p = left.text_input("Nombre cliente pandebono", key="nombre_cliente_pandebono")
pandebonos = left.text_input("Pandebonos vendidos", key="cantidad_pandebonos")

nombre_c = right.text_input("Nombre cliente croissant", key="nombre_cliente_croissant")
croissants = right.text_input("Croissants vendidos", key="cantidad_croissants")


confirm = left.button("Confirmar compra", use_container_width=True)
back = right.button("Volver", use_container_width=True)


if back:
    st.switch_page("pages/menu.py")


if confirm:
    if nombre_p != "" and pandebonos != "":
        cargar_tabla_ventas(nombre=nombre_p, cantidad=int(pandebonos))

    if nombre_c != "" and croissants != "":
        cargar_tabla_ventas(nombre=nombre_c, cantidad=int(croissants))
    
    st.session_state["limpiar_campos"] = True
    st.success("Venta guardada con exito")
    time.sleep(1.5) 
    st.rerun()
