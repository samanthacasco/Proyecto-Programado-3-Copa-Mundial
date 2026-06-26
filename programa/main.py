import tkinter as tk
from utilidades import centrar_ventana, limpiar_ventana
from gui_admin import mostrar_admin_paises_selecciones, mostrar_admin_entrenadores_jugadores
from mundial import Mundial
from gui_mundial import mostrar_configurar_mundial, mostrar_jugar_mundial, mostrar_estadisticas
from persistencia import cargar_paises, cargar_selecciones, cargar_jugadores
# Estilos
FONDO_OSCURO = "#0a1628"
FONDO_CARD = "#0d2137"
VERDE_CANCHA = "#2ecc71"
DORADO = "#f1c40f"
TEXTO_BLANCO = "#ffffff"
TEXTO_AZUL = "#7fb3d3"
ROJO_SALIR = "#e57373"
FUENTE_TITULO = ("Arial", 22, "bold")
FUENTE_BOTON = ("Arial", 11)

ventana = tk.Tk()
ventana.title("Mundial FIFA 2026")
centrar_ventana(ventana, 600, 600)

lista_paises = []
lista_selecciones = []
lista_entrenadores = []
lista_jugadores = []

# Cargar datos guardados al iniciar
lista_paises = cargar_paises()
lista_selecciones = cargar_selecciones(lista_paises)
lista_jugadores = cargar_jugadores()

mundial = Mundial("Mundial FIFA 2026", 2026) 

def mostrar_menu():
    limpiar_ventana(ventana)
    ventana.configure(bg=FONDO_OSCURO)
    
    tk.Label(ventana, text="⚽ Mundial FIFA 2026",
             font=FUENTE_TITULO, bg=FONDO_OSCURO, fg=DORADO).pack(pady=30)
    
    tk.Label(ventana, text="Sistema de gestión del torneo",
             font=("Arial", 10), bg=FONDO_OSCURO, fg=TEXTO_AZUL).pack(pady=0)
    
    btn_paises = tk.Button(ventana, text="🌎 Administrar Países y Selecciones",
                           font=FUENTE_BOTON, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                           activebackground="#1a3a5c", activeforeground=TEXTO_BLANCO,
                           relief="flat", padx=20, pady=10, cursor="hand2",
                           command=lambda: mostrar_admin_paises_selecciones(ventana, lista_paises, lista_selecciones, mostrar_menu))
    btn_paises.pack(pady=5, fill="x", padx=40)
    
    btn_jugadores = tk.Button(ventana, text="👥  Administrar Entrenadores y Jugadores",
                           font=FUENTE_BOTON, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                           activebackground="#1a3a5c", activeforeground=TEXTO_BLANCO,
                           relief="flat", padx=20, pady=10, cursor="hand2", 
                              command=lambda: mostrar_admin_entrenadores_jugadores(ventana, lista_entrenadores, lista_jugadores, lista_selecciones, mostrar_menu))
    btn_jugadores.pack(pady=5, fill="x", padx=40)

    btn_configurar = tk.Button(ventana, text="⚙️  Configurar Mundial",
                           font=FUENTE_BOTON, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                           activebackground="#1a3a5c", activeforeground=TEXTO_BLANCO,
                           relief="flat", padx=20, pady=10, cursor="hand2",
                                command=lambda: mostrar_configurar_mundial(ventana, lista_selecciones, mundial, mostrar_menu))
    btn_configurar.pack(pady=5, fill="x", padx=40)
    
    btn_jugar = tk.Button(ventana, text="▶️ Jugar Mundial",
                           font=FUENTE_BOTON, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                           activebackground="#1a3a5c", activeforeground=TEXTO_BLANCO,
                           relief="flat", padx=20, pady=10, cursor="hand2",
                            command=lambda: mostrar_jugar_mundial(ventana, mundial, mostrar_menu))
    btn_jugar.pack(pady=5, fill="x", padx=40)
    
    btn_estadisticas = tk.Button(ventana, text="📊 Ver Estadísticas/Rankings",
                           font=FUENTE_BOTON, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                           activebackground="#1a3a5c", activeforeground=TEXTO_BLANCO,
                           relief="flat", padx=20, pady=10, cursor="hand2",
                                    command=lambda: mostrar_estadisticas(ventana, mundial, mostrar_menu))
    btn_estadisticas.pack(pady=5, fill="x", padx=40)
    
    btn_salir = tk.Button(ventana, text="Salir",
                           font=FUENTE_BOTON, bg=FONDO_CARD, fg=ROJO_SALIR,
                           activebackground="#1a3a5c", activeforeground=TEXTO_BLANCO,
                           relief="flat", padx=20, pady=10, cursor="hand2", command=ventana.destroy)
    btn_salir.pack(pady=5, fill="x", padx=40)


mostrar_menu()
ventana.mainloop()
