import streamlit as st
import time
from src.funciones import cargar_configuraciones_json, guardar_opciones_json

# Limpieza de inputs si venimos de un "guardar"
if st.session_state.get("limpiar_campos", False):
    for key in [
        "queso_pandebono", "almidon_pandebono", "mantequilla_pandebono",
        "azucar_pandebono", "masa_pandebono", "leche_pandebono",
        "queso_croissant", "almidon_croissant", "mantequilla_croissant",
        "azucar_croissant", "masa_croissant", "leche_croissant"
    ]:
        st.session_state[key] = ""
    st.session_state["limpiar_campos"] = False

prev_conf = cargar_configuraciones_json()

# Crear columnas principales
left, right = st.columns(2)

# Sección Pandebono
left.markdown("<h2 style='text-align: center; margin-bottom: 20px;'>Pandebono</h2>", unsafe_allow_html=True)
left_l, right_l = left.columns(2)

queso_p = left_l.text_input("Queso por pandebono", key="queso_pandebono", placeholder=f"{prev_conf["q_p"]} g")
almidon_p = left_l.text_input("Almidon por pandebono", key="almidon_pandebono", placeholder=f"{prev_conf["al_p"]} g")
mantequilla_p = left_l.text_input("Mantequilla por pandebono", key="mantequilla_pandebono", placeholder=f"{prev_conf["man_p"]} g")

azucar_p = right_l.text_input("Azucar por pandebono", key="azucar_pandebono", placeholder=f"{prev_conf["a_p"]} g")
masa_p = right_l.text_input("Masa arepa por pandebono", key="masa_pandebono", placeholder=f"{prev_conf["m_p"]} g")
leche_p = right_l.text_input("Leche por pandebono", key="leche_pandebono", placeholder=f"{prev_conf["l_p"]} ml")

# Espacio entre secciones
st.markdown("---")

# Sección Croissant
right.markdown("<h2 style='text-align: center; margin-bottom: 20px;'>Croissant</h2>", unsafe_allow_html=True)
left_r, right_r = right.columns(2)

queso_c = left_r.text_input("Queso por croissant", key="queso_croissant", placeholder=f"{prev_conf["q_c"]} g")
almidon_c = left_r.text_input("Almidon por croissant", key="almidon_croissant", placeholder=f"{prev_conf["al_c"]} g")
mantequilla_c = left_r.text_input("Mantequilla por croissant", key="mantequilla_croissant", placeholder=f"{prev_conf["man_c"]} g")

azucar_c = right_r.text_input("Azucar por croissant", key="azucar_croissant", placeholder=f"{prev_conf["a_c"]} g")
masa_c = right_r.text_input("Masa arepa por croissant", key="masa_croissant", placeholder=f"{prev_conf["m_c"]} g")
leche_c = right_r.text_input("Leche por croissant", key="leche_croissant", placeholder=f"{prev_conf["l_c"]} ml")

# Botones
st.markdown("###")
end_left, end_right = st.columns(2)

guardar = end_left.button("Guardar", use_container_width=True)
volver = end_right.button("volver", use_container_width=True)

if volver:
    st.switch_page("pages/menu.py")

if guardar:
    guardar_opciones_json(
        queso_p=queso_p, almidon_p=almidon_p, mantequilla_p=mantequilla_p,
        azucar_p=azucar_p, masa_p=masa_p, leche_p=leche_p,
        queso_c=queso_c, almidon_c=almidon_c, mantequilla_c=mantequilla_c,
        azucar_c=azucar_c, masa_c=masa_c, leche_c=leche_c
    )
    st.session_state["limpiar_campos"] = True
    time.sleep(1.5) 
    st.rerun()
