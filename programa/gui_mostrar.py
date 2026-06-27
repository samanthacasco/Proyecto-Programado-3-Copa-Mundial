import tkinter as tk

# Estilos
FONDO_OSCURO = "#0a1628"
FONDO_CARD = "#0d2137"
DORADO = "#f1c40f"
TEXTO_BLANCO = "#ffffff"
FUENTE_TITULO = ("Arial", 16, "bold")

def mostrar_ventana_datos(titulo, texto):
    """
    Abre una ventana nueva con scroll que muestra el texto recibido.
    #E: titulo (str), texto (str)
    #S: No retorna nada, abre una ventana Toplevel con los datos
    #R: titulo y texto deben ser str
    """
    ventana_datos = tk.Toplevel()
    ventana_datos.title(titulo)
    ventana_datos.geometry("600x500")
    ventana_datos.configure(bg=FONDO_OSCURO)

    tk.Label(ventana_datos, text=titulo, font=FUENTE_TITULO,
             bg=FONDO_OSCURO, fg=DORADO).pack(pady=15)

    # Text con scrollbar para mostrar los datos
    frame_texto = tk.Frame(ventana_datos, bg=FONDO_OSCURO)
    frame_texto.pack(pady=10, padx=20, fill="both", expand=True)

    scrollbar = tk.Scrollbar(frame_texto)
    scrollbar.pack(side="right", fill="y")

    caja_texto = tk.Text(frame_texto, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                         font=("Arial", 10), yscrollcommand=scrollbar.set,
                         wrap="word")
    caja_texto.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=caja_texto.yview)

    caja_texto.insert("1.0", texto)
    caja_texto.config(state="disabled")  # solo lectura

    tk.Button(ventana_datos, text="Cerrar", font=("Arial", 11),
              bg=FONDO_CARD, fg=TEXTO_BLANCO, relief="flat",
              padx=20, pady=10, cursor="hand2",
              command=ventana_datos.destroy).pack(pady=10, fill="x", padx=40)
