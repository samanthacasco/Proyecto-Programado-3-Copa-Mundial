import tkinter as tk
from utilidades import centrar_ventana, limpiar_ventana
from gui_admin import mostrar_paises

ventana = tk.Tk()
ventana.title("Mundial FIFA 2026")
centrar_ventana(ventana, 800, 600)
lista_paises = []

def mostrar_menu():
    limpiar_ventana(ventana)
    
    titulo = tk.Label(ventana, text="Mundial FIFA 2026", font=("Arial", 24))
    titulo.pack(pady=20)

    btn_paises = tk.Button(ventana, text="Administrar Países y Selecciones", 
                       command=lambda: mostrar_paises(ventana, lista_paises, mostrar_menu))
    btn_paises.pack(pady=10)

    btn_jugadores = tk.Button(ventana, text="Administrar Entrenadores y Jugadores")
    btn_jugadores.pack(pady=10)

    btn_configurar = tk.Button(ventana, text="Configurar Mundial")
    btn_configurar.pack(pady=10)

    btn_jugar = tk.Button(ventana, text="Jugar Mundial")
    btn_jugar.pack(pady=10)

    btn_estadisticas = tk.Button(ventana, text="Ver Estadísticas / Rankings")
    btn_estadisticas.pack(pady=10)

    btn_salir = tk.Button(ventana, text="Salir", command=ventana.destroy)
    btn_salir.pack(pady=10)

mostrar_menu()
ventana.mainloop()
