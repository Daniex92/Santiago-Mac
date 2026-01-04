import streamlit as st
from juzgados import JUZGADOS

# Configuración visual de la página
st.set_page_config(page_title="Rodríguez Asociados", page_icon="⚖️")

# Estilo para que parezca una App (Botones dorados y fondo oscuro)
st.markdown("""
    <style>
    .main { background-color: #000000; }
    .stButton>button {
        width: 100%;
        border-radius: 25px;
        border: 2px solid #C9A24D;
        background-color: transparent;
        color: white;
        height: 3.5em;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #C9A24D;
        color: black;
        border: 2px solid #C9A24D;
    }
    h1 { color: #C9A24D; text-align: center; font-family: 'serif'; }
    p { color: white; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("RODRÍGUEZ ASOCIADOS")
st.write("Seleccione el juzgado para abrir el portal oficial")

# Crear los botones funcionales
for nombre, url in JUZGADOS.items():
    # Creamos un botón normal, pero al hacer clic usamos un componente de link oculto
    if st.button(nombre):
        js = f"window.open('{url}')"  # Este comando le dice al navegador: "abre esta web"
        st.components.v1.html(f"<script>{js}</script>", height=0)
        st.success(f"Abriendo {nombre}...")

# Pie de página
st.markdown("---")
st.caption("Sistema de Gestión Judicial - Chiquinquirá")
