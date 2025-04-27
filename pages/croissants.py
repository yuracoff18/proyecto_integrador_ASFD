import pandas as pd
import streamlit as st

# Cargar la tabla
tabla = pd.read_csv("data/compras.csv")

# Filtro: Solo Pandebono
tabla_pandebono = tabla[tabla["producto"] == "Croissant"]

# Agrupar por día solo los Pandebonos
ventas_dia = tabla_pandebono.groupby("dia")["cantidad"].sum().reset_index()

# Graficar
st.bar_chart(ventas_dia.set_index("dia"))

# Botón de volver
volver = st.button("Volver", use_container_width=True)

if volver:
    st.switch_page("pages/menu.py")
