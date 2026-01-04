import customtkinter as ctk
from app import abrir_juzgado  # tu función actual

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Rodríguez Asociados")
app.geometry("420x640")
app.resizable(False, False)

# ===== CONTENEDOR =====
frame = ctk.CTkFrame(app, fg_color="#0B0B0B")
frame.pack(fill="both", expand=True, padx=20, pady=20)

# ===== TITULO =====
titulo = ctk.CTkLabel(
    frame,
    text="RODRÍGUEZ\nASOCIADOS",
    font=("Times New Roman", 22, "bold"),
    text_color="#C9A24D",
    justify="center"
)
titulo.pack(pady=(20, 10))

sub = ctk.CTkLabel(
    frame,
    text="Chiquinquirá - Familia",
    font=("Times New Roman", 14),
    text_color="white"
)
sub.pack(pady=(0, 30))

# ===== BOTONES =====
def boton_juzgado(nombre, despacho):
    return ctk.CTkButton(
        frame,
        text=nombre,
        height=45,
        fg_color="#0B0B0B",
        border_color="#C9A24D",
        border_width=1,
        hover_color="#1A1A1A",
        text_color="white",
        font=("Times New Roman", 13),
        command=lambda: abrir_juzgado(despacho)
    )

boton_juzgado(
    "Juzgado 001",
    {
        "departamento": "BOYACÁ",
        "municipio": "CHIQUINQUIRÁ",
        "despacho": "151763110001 - JUZGADO 001 DE FAMILIA"
    }
).pack(pady=8)

boton_juzgado("Juzgado X", {...}).pack(pady=8)
boton_juzgado("Juzgado X", {...}).pack(pady=8)

app.mainloop()
