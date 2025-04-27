import streamlit as st


st.markdown("<h1 style='text-align: center; margin-bottom: 20px;'>Bienvenido</h1>", unsafe_allow_html=True)

left, mid, right = st.columns(3)
datos = mid.button("Ingresar datos de venta", use_container_width=True)
pandebonos_graficas = mid.button("Ver grafico de pandebono", use_container_width=True)
croissants = mid.button("Ver grafico de croissant",use_container_width=True)
mid.button("Generar reporte", use_container_width=True)
configuracion = mid.button("Configuracion",use_container_width=True)
cerrar_sesion = mid.button("Cerrar sesion",use_container_width=True)



if croissants:
    st.switch_page("pages/croissants.py")

if pandebonos_graficas:
    st.switch_page("pages/pandebonos.py")

if datos:
    st.switch_page("pages/ingreso_ventas.py")

if configuracion:
    st.switch_page("pages/configuration.py")

if cerrar_sesion:
    st.switch_page("main.py")
