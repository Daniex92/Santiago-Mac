import customtkinter as ctk
from navegador import abrir_juzgado
from juzgados import JUZGADOS

# Configuración de apariencia
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Rodríguez Asociados")
app.geometry("420x640")
app.resizable(False, False)

# ===== CONTENEDOR PRINCIPAL =====
frame = ctk.CTkFrame(app, fg_color="black")
frame.pack(fill="both", expand=True, padx=20, pady=20)

# ===== TÍTULOS =====
titulo = ctk.CTkLabel(
    frame,
    text="RODRÍGUEZ\nASOCIADOS",
    font=("Times New Roman", 24, "bold"),
    text_color="white",
    justify="center"
)
titulo.pack(pady=(20, 5))

sub = ctk.CTkLabel(
    frame,
    text="Oficina de abogados",
    font=("Times New Roman", 15),
    text_color="#C9A24D"
)
sub.pack(pady=(0, 30))

# ===== GENERACIÓN AUTOMÁTICA DE BOTONES =====
# Este bucle recorre tu archivo juzgados.py y crea los botones con el estilo nuevo
for nombre, datos in JUZGADOS.items():
    btn = ctk.CTkButton(
        frame,
        text=nombre,
        height=45,
        fg_color="#0B0B0B",
        border_color="#C9A24D",
        border_width=1,
        hover_color="#1A1A1A",
        text_color="white",
        font=("Times New Roman", 14),
        # Usamos d=datos para que el lambda capture el valor correcto en cada vuelta
        command=lambda d=datos: abrir_juzgado(d)
    )
    btn.pack(pady=8, fill="x", padx=20)

app.mainloop()