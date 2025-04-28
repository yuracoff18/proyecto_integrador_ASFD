import pandas as pd
import streamlit as st

tabla = pd.read_csv("data/compras.csv")

tabla_pandebono = tabla[tabla["producto"] == "Croissant"]

tabla_pandebono_validos = tabla_pandebono[tabla_pandebono["nombre_cliente"] != "--------"]

dias_ordenados = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']

ventas_dia = tabla_pandebono.groupby("dia")["cantidad"].sum().reset_index()

ventas_dia['dia'] = pd.Categorical(ventas_dia['dia'], categories=dias_ordenados, ordered=True)
ventas_dia = ventas_dia.sort_values('dia')

st.bar_chart(ventas_dia.set_index("dia"))

promedios_dia = tabla_pandebono_validos.groupby("dia")["cantidad"].mean().reset_index()

promedios_dia['dia'] = pd.Categorical(promedios_dia['dia'], categories=dias_ordenados, ordered=True)
promedios_dia = promedios_dia.sort_values('dia')

st.write("### Promedio de croissants vendidos por cada día:")
st.dataframe(promedios_dia[['dia', 'cantidad']])

volver = st.button("Volver", use_container_width=True)

if volver:
    st.switch_page("pages/menu.py")
