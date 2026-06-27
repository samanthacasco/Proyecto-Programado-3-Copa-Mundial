import tkinter as tk
from tkinter import messagebox
from utilidades import limpiar_ventana
from seleccion import Seleccion
   
FONDO_OSCURO = "#0a1628"
FONDO_CARD = "#0d2137"
DORADO = "#f1c40f"
TEXTO_BLANCO = "#ffffff"
TEXTO_AZUL = "#7fb3d3"
FUENTE_TITULO = ("Arial", 18, "bold")
FUENTE_BOTON = ("Arial", 11)

def mostrar_configurar_mundial(ventana, lista_selecciones, mundial, mostrar_menu):
    """
    Muestra la pantalla para configurar los grupos del mundial
    #E: ventana (tk.Tk), lista_selecciones (list), mundial (Mundial), mostrar_menu (function)
    #S: No retorna nada, dibuja la pantalla de configuración del mundial
    #R: Deben existir selecciones registradas previamente
    """
    limpiar_ventana(ventana)
    ventana.configure(bg=FONDO_OSCURO)

    tk.Label(ventana,text="⚙️ Configurar Mundial",font=FUENTE_TITULO,bg=FONDO_OSCURO,fg=DORADO).pack(pady=20)
    
    tk.Label(ventana,text=f"Selecciones registradas: {len(lista_selecciones)}",font=FUENTE_BOTON,bg=FONDO_OSCURO,fg=TEXTO_BLANCO).pack(pady=5)

    tk.Label(ventana,text="Cantidad de grupos:",font=FUENTE_BOTON,bg=FONDO_OSCURO,fg=TEXTO_BLANCO).pack(pady=5)

    entry_grupos = tk.Entry(ventana,bg=FONDO_CARD,fg=TEXTO_BLANCO,insertbackground=TEXTO_BLANCO,font=FUENTE_BOTON)
    entry_grupos.pack(pady=5)

    resultado_texto = tk.Text(ventana,width=55,height=18,bg=FONDO_CARD,fg=TEXTO_BLANCO,font=("Arial", 10))
    resultado_texto.pack(pady=15)

    def configurar():
        cantidad = entry_grupos.get()

        if cantidad == "":
            messagebox.showerror("Error", "Debe ingresar la cantidad de grupos")
            return

        if not cantidad.isdigit():
            messagebox.showerror("Error", "La cantidad de grupos debe ser un número")
            return

        cantidad_grupos = int(cantidad)

        if cantidad_grupos < 2:
            messagebox.showerror("Error", "La cantidad mínima de grupos es 2")
            return
        
        clasificados_posibles = cantidad_grupos * 2
        if clasificados_posibles not in [2, 4, 8, 16, 32]:
            messagebox.showerror("Error", "La cantidad de grupos debe ser 2, 4, 8 o 16\n"
                                 "para generar 2, 4, 8, 16 o 32 clasificados")
            return
        
        if len(lista_selecciones) == 0:
            messagebox.showerror("Error", "Primero debe registrar selecciones antes de crear grupos.")
            return

        if len(lista_selecciones) != cantidad_grupos * 4:
            messagebox.showerror("Error", 
                f"La cantidad de selecciones debe ser igual a grupos x 4.\n"
                f"Tiene {len(lista_selecciones)} selecciones → use {len(lista_selecciones) // 4} grupos")
            return
        
        for seleccion in lista_selecciones:
            if len(seleccion.get_jugadores()) < 11:
                messagebox.showerror("Error", f"La selección {seleccion.get_pais().get_nombre()} debe tener al menos 11 jugadores")
                return
            if seleccion.get_entrenador() is None:
                messagebox.showerror("Error", f"La selección {seleccion.get_pais().get_nombre()} no tiene entrenador asignado")
                return
            
        if len(mundial.get_selecciones()) == 0: 
            for seleccion in lista_selecciones:
                mundial.registrar_seleccion(seleccion)
 
        creado = mundial.crear_grupos(cantidad_grupos)

        if creado == False:
            messagebox.showerror("Error", "No se pudieron crear los grupos")
            return

        resultado_texto.delete("1.0", tk.END)

        for grupo in mundial.get_grupos():
            resultado_texto.insert(tk.END, grupo.get_nombre_grupo() + "\n")

            for equipo in grupo.get_equipos():
                resultado_texto.insert(tk.END, "- " + equipo.get_pais().get_nombre() + "\n")

            resultado_texto.insert(tk.END, "\n")

        messagebox.showinfo("Éxito", "Grupos creados correctamente")
        # Desactivarlos de pues de usarlo 
        btn_crear_grupos.config(state="disabled")

    btn_crear_grupos = tk.Button(ventana,text="Crear grupos",font=FUENTE_BOTON,bg=FONDO_CARD,fg=TEXTO_BLANCO,
            command=configurar)
    btn_crear_grupos.pack(pady=5, fill="x", padx=40)

    tk.Button(ventana,text="🔙 Volver al menú",font=FUENTE_BOTON,bg=FONDO_CARD,fg=TEXTO_AZUL,
            command=mostrar_menu).pack(pady=5, fill="x", padx=40)
    
def mostrar_jugar_mundial(ventana, mundial, mostrar_menu):
    """
    Muestra la pantalla para jugar el mundial.
    #E: ventana (tk.Tk), mundial (Mundial), mostrar_menu (function)
    #S: No retorna nada, dibuja la pantalla para simular el mundial
    #R: El mundial debe tener grupos creados previamente
    """
    limpiar_ventana(ventana)
    ventana.configure(bg=FONDO_OSCURO)

    tk.Label(ventana, text="▶️ Jugar Mundial",font=FUENTE_TITULO, bg=FONDO_OSCURO,  fg=DORADO).pack(pady=20)

    resultado_texto = tk.Text(ventana, width=65, height=22, bg=FONDO_CARD,
                          fg=TEXTO_BLANCO, font=("Arial", 10),
                          state="disabled") 
    resultado_texto.pack(pady=10)

    def simular_grupos():
        if len(mundial.get_grupos()) == 0:
            messagebox.showerror("Error", "Primero debe configurar los grupos.")
            return

        mundial.jugar_fase_grupos()

        resultado_texto.config(state="normal")  
        resultado_texto.delete("1.0", tk.END)
        resultado_texto.insert(tk.END, "TABLAS DE GRUPOS\n\n")
        resultado_texto.insert(tk.END, mundial.mostrar_tabla_general())
        resultado_texto.config(state="disabled")

        messagebox.showinfo("Éxito", "Fase de grupos simulada correctamente.")
        btn_simular_fase.config(state="disabled")
        btn_simular_eliminatorias.config(state="normal")

    def simular_eliminatorias():
        if len(mundial.get_grupos()) == 0:
            messagebox.showerror("Error", "Primero debe configurar los grupos.")
            return

        campeon = mundial.determinar_campeon()

        resultado_texto.config(state="normal")
        resultado_texto.insert(tk.END, "\nFASES ELIMINATORIAS\n\n")
        
        for fase in mundial.get_fases():  
            resultado_texto.insert(tk.END, fase.mostrar_juegos())
            resultado_texto.insert(tk.END, "\n")
            
        resultado_texto.insert(tk.END, "\nCAMPEÓN\n")
        resultado_texto.insert(tk.END, campeon.get_pais().get_nombre())
        resultado_texto.config(state="disabled")

        mundial.generar_reporte()

        messagebox.showinfo("Éxito", "Mundial finalizado correctamente.")
        
        btn_simular_eliminatorias.config(state="disabled")

    btn_simular_fase= tk.Button(ventana, text="Simular fase de grupos", font=FUENTE_BOTON, bg=FONDO_CARD, fg=TEXTO_BLANCO,
        command=simular_grupos)
    btn_simular_fase.pack(pady=5, fill="x", padx=40)

    btn_simular_eliminatorias= tk.Button(ventana, text="Simular eliminatorias y campeón", font=FUENTE_BOTON, bg=FONDO_CARD, fg=TEXTO_BLANCO,
        command=simular_eliminatorias, state="disabled")
    btn_simular_eliminatorias.pack(pady=5, fill="x", padx=40)

    tk.Button(ventana, text="🔙 Volver al menú", font=FUENTE_BOTON, bg=FONDO_CARD, fg=TEXTO_AZUL,
        command=mostrar_menu).pack(pady=5, fill="x", padx=40)
    
def mostrar_estadisticas(ventana, mundial, mostrar_menu):
    """
    Muestra las estadísticas y rankings del mundial.
    #E: ventana (tk.Tk), mundial (Mundial), mostrar_menu (function)
    #S: No retorna nada, dibuja la pantalla de estadísticas
    #R: El mundial debe haberse jugado previamente
    """
    limpiar_ventana(ventana)
    ventana.configure(bg=FONDO_OSCURO)

    tk.Label(ventana, text="📊 Estadísticas / Rankings", font=FUENTE_TITULO, bg=FONDO_OSCURO, fg=DORADO).pack(pady=20)

    resultado_texto = tk.Text(ventana,width=70, height=25,bg=FONDO_CARD, fg=TEXTO_BLANCO, font=("Arial", 10))
    resultado_texto.pack(pady=10)

    def mostrar_datos():
        resultado_texto.delete("1.0", tk.END)

        if mundial.get_campeon() is not None:
            resultado_texto.insert(tk.END, "CAMPEÓN\n")
            resultado_texto.insert(tk.END, mundial.get_campeon().get_pais().get_nombre() + "\n\n")

        # Mostrar selccion con mas goles
        max_goles = -1
        seleccion_mas_goles = None

        for seleccion in mundial.get_selecciones():
            goles = seleccion.get_total_goles_favor()

            if goles > max_goles:
                max_goles = goles
                selecciones_mas_goles = [seleccion]

            elif goles == max_goles:
                selecciones_mas_goles.append(seleccion)
                
        resultado_texto.insert(tk.END, "SELECCIÓN(ES) CON MÁS GOLES\n")
        for seleccion in selecciones_mas_goles:
            resultado_texto.insert(tk.END,
                seleccion.get_pais().get_nombre() +
                " | Goles: " + str(max_goles) + "\n")

        resultado_texto.insert(tk.END, "\n")

        # Mostrar selccion con mas tarjetas amarillas
        max_amarillas = -1    
        selecciones_mas_amarillas = None
        for seleccion in mundial.get_selecciones():
            amarillas= seleccion.get_total_tarjetas_amarillas()

            if amarillas > max_amarillas:
                max_amarillas = amarillas
                selecciones_mas_amarillas = [seleccion]
            elif amarillas == max_amarillas:
                selecciones_mas_amarillas.append(seleccion)

        resultado_texto.insert(tk.END, "SELECCIÓN(ES) CON MÁS TARJETAS AMARILLAS\n")
        
        for seleccion in selecciones_mas_amarillas:
            resultado_texto.insert(tk.END,
                seleccion.get_pais().get_nombre() +
                " | Amarillas: " + str(max_amarillas) + "\n")

        resultado_texto.insert(tk.END, "\n")
            
        # Mostrar selccion con mas tarjetas rojas
        max_rojas = -1
        seleccion_mas_rojas = [ ]
        for seleccion in mundial.get_selecciones():
                rojas = seleccion.get_total_tarjetas_rojas()

                if rojas > max_rojas:
                    max_rojas = rojas
                    selecciones_mas_rojas = [seleccion]
                elif rojas == max_rojas:
                    selecciones_mas_rojas.append(seleccion)

        resultado_texto.insert(tk.END, "SELECCIÓN(ES) CON MÁS TARJETAS ROJAS\n")

        for seleccion in selecciones_mas_rojas:
            resultado_texto.insert(tk.END,
                seleccion.get_pais().get_nombre() +
                " | Rojas: " + str(max_rojas) + "\n")

        resultado_texto.insert(tk.END, "\n")
                    
        resultado_texto.insert(tk.END, "RANKING DE GOLEADORES\n\n")

        jugadores = []
        for seleccion in mundial.get_selecciones():
            for jugador in seleccion.get_jugadores():
                jugadores.append([jugador, seleccion])

        for i in range(len(jugadores)):
            for j in range(len(jugadores) - 1):
                if jugadores[j][0].get_goles() < jugadores[j + 1][0].get_goles():
                    jugadores[j], jugadores[j + 1] = jugadores[j + 1], jugadores[j]

        for dato in jugadores:
            jugador = dato[0]
            seleccion = dato[1]

            if jugador.get_goles() > 0:
                resultado_texto.config(state="normal") 
                resultado_texto.insert(
                    tk.END,
                    jugador.get_nombre() + " " + jugador.get_apellido() +
                    " | " + seleccion.get_pais().get_nombre() +
                    " | Goles: " + str(jugador.get_goles()) + "\n")

        resultado_texto.insert(tk.END, "\nTARJETAS POR SELECCIÓN\n\n")

        for seleccion in mundial.get_selecciones():
            resultado_texto.insert(
                tk.END,
                seleccion.get_pais().get_nombre() +
                " | Amarillas: " + str(seleccion.get_total_tarjetas_amarillas()) +
                " | Rojas: " + str(seleccion.get_total_tarjetas_rojas()) + "\n")
        
        resultado_texto.config(state="disabled")

        # Desactiva el botón para que no vuelva a ejecutarse
        btn_mostrar.config(state="disabled")

    # Guardar boton en una variable 
    btn_mostrar = tk.Button(ventana, text="Mostrar estadísticas", font=FUENTE_BOTON, bg=FONDO_CARD,fg=TEXTO_BLANCO,
    command=mostrar_datos)
    btn_mostrar.pack(pady=5, fill="x", padx=40)

    tk.Button(ventana, text="🔙 Volver al menú", font=FUENTE_BOTON, bg=FONDO_CARD, fg=TEXTO_AZUL,
        command=mostrar_menu).pack(pady=5, fill="x", padx=40)
    

"""
mostrar seleccion ocn mas goles"""