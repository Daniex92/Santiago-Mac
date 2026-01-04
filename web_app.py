import streamlit as st
from juzgados import JUZGADOS
import webbrowser

# Configuración de la página
st.set_page_config(page_title="Rodríguez Asociados", page_icon="⚖️")

# Estilo visual (Dorado y Negro)
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        border: 2px solid #C9A24D;
        background-color: black;
        color: white;
        height: 3em;
    }
    .stButton>button:hover {
        background-color: #C9A24D;
        color: black;
    }
    h1 { color: #C9A24D; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("RODRÍGUEZ ASOCIADOS")
st.subheader("Chiquinquirá - Familia")

# Botones de Juzgados
for nombre, url in JUZGADOS.items():
    if st.button(nombre):
        # En la web, esto abre una pestaña nueva
        st.write(f"Abriendo: {nombre}...")
        st.markdown(f'<meta http-equiv="refresh" content="0;URL={url}">', unsafe_allow_html=True)