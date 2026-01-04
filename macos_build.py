import streamlit as st
# Importamos tus datos reales
from juzgados import JUZGADOS

st.set_page_config(page_title="Rodríguez Asociados", page_icon="⚖️")

# Estilo Dorado y Negro (Inspirado en tu app.py)
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1 { color: #C9A24D; text-align: center; font-family: 'serif'; }
    .stButton>button {
        width: 100%;
        border-radius: 15px;
        border: 1px solid #C9A24D;
        background-color: #0B0B0B;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("RODRÍGUEZ ASOCIADOS")

# Usamos los datos de juzgados.py
for nombre, info in JUZGADOS.items():
    if st.button(nombre):
        despacho = info["despacho"] # Extraído de juzgados.py
        st.info(f"Copia esto: {despacho}")
        
        # Enlace al portal
        url = "https://publicacionesprocesales.ramajudicial.gov.co/web/publicaciones-procesales/inicio"
        js = f"window.open('{url}')"
        st.components.v1.html(f"<script>{js}</script>", height=0)