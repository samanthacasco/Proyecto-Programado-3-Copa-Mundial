import tkinter as tk
from utilidades import centrar_ventana, limpiar_ventana
from gui_admin import mostrar_admin_paises_selecciones, mostrar_admin_entrenadores_jugadores

ventana = tk.Tk()
ventana.title("Mundial FIFA 2026")
centrar_ventana(ventana, 800, 600)
lista_paises = []
lista_selecciones = []
lista_entrenadores = []
lista_jugadores = []

def mostrar_menu():
    """
    Muestra el menu principal del programa
    #E:No recibe parámetros
    #S: No retorna nada, dibuja los widgets en la ventana
    #R: La ventana debe estar inicializada correctamente
    """
    limpiar_ventana(ventana)
    
    titulo = tk.Label(ventana, text="Mundial FIFA 2026", font=("Arial", 24))
    titulo.pack(pady=20)

    btn_paises = tk.Button(ventana, text="Administrar Países y Selecciones", 
                       command=lambda: mostrar_admin_paises_selecciones(ventana, lista_paises, lista_selecciones, mostrar_menu))
    btn_paises.pack(pady=10)
    
    btn_jugadores = tk.Button(ventana, text="Administrar Entrenadores y Jugadores", 
                              command=lambda: mostrar_admin_entrenadores_jugadores(ventana, lista_entrenadores, lista_jugadores, mostrar_menu))
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
