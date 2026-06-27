import tkinter as tk
from utilidades import limpiar_ventana

FONDO_OSCURO = "#0a1628"
FONDO_CARD = "#0d2137"
DORADO = "#f1c40f"
TEXTO_BLANCO = "#ffffff"
FUENTE_TITULO = ("Arial", 18, "bold")

def mostrar_ventana_datos(ventana, titulo, texto):
    """
    Limpia la ventana y muestra un título y texto con scroll.
    #E: ventana (tk.Tk), titulo (str), texto (str)
    #S: No retorna nada, dibuja el contenido en la ventana
    #R: ventana debe estar inicializada correctamente
    """
    limpiar_ventana(ventana)
    ventana.configure(bg=FONDO_OSCURO)

    tk.Label(ventana, text=titulo, font=FUENTE_TITULO,
             bg=FONDO_OSCURO, fg=DORADO).pack(pady=15)

    frame_texto = tk.Frame(ventana, bg=FONDO_OSCURO)
    frame_texto.pack(pady=10, padx=20, fill="both", expand=True)

    scrollbar = tk.Scrollbar(frame_texto)
    scrollbar.pack(side="right", fill="y")

    caja_texto = tk.Text(frame_texto, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                         font=("Arial", 10), yscrollcommand=scrollbar.set,
                         wrap="word")
    caja_texto.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=caja_texto.yview)

    caja_texto.insert("1.0", texto)
    caja_texto.config(state="disabled")
