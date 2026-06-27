import tkinter as tk
from tkinter import messagebox
from utilidades import limpiar_ventana
from seleccion import Seleccion
from tkinter import ttk
   
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
    # Limpia la ventana actual antes de dibujar esta pantalla
    limpiar_ventana(ventana)
    ventana.configure(bg=FONDO_OSCURO)

    # Título principal de la pantalla
    tk.Label(ventana,text="⚙️ Configurar Mundial",font=FUENTE_TITULO,bg=FONDO_OSCURO,fg=DORADO).pack(pady=20)
    
    # Muestra cuántas selecciones hay registradas
    tk.Label(ventana,text=f"Selecciones registradas: {len(lista_selecciones)}",font=FUENTE_BOTON,bg=FONDO_OSCURO,fg=TEXTO_BLANCO).pack(pady=5)
    
    # Texto para indicar que el usuario debe ingresar la cantidad de grupos
    tk.Label(ventana,text="Cantidad de grupos:",font=FUENTE_BOTON,bg=FONDO_OSCURO,fg=TEXTO_BLANCO).pack(pady=5)

    # Entrada donde el usuario escribe la cantidad de grupos
    entry_grupos = tk.Entry(ventana,bg=FONDO_CARD,fg=TEXTO_BLANCO,insertbackground=TEXTO_BLANCO,font=FUENTE_BOTON)
    entry_grupos.pack(pady=5)

    # Cuadro donde se mostrarán los grupos ya formados
    resultado_texto = tk.Text(ventana,width=55,height=18,bg=FONDO_CARD,fg=TEXTO_BLANCO,font=("Arial", 10))
    resultado_texto.pack(pady=15)

    def configurar():
        """
        Valida la información ingresada, registra las selecciones en el mundial,
        crea los grupos y los muestra en pantalla.
        """

        # Obtiene la cantidad de grupos escrita por el usuario
        cantidad = entry_grupos.get()

        # Validar que el campo no esté vacío
        if cantidad == "":
            messagebox.showerror("Error", "Debe ingresar la cantidad de grupos")
            return
        
        # Validar que solo se ingresen números
        if not cantidad.isdigit():
            messagebox.showerror("Error", "La cantidad de grupos debe ser un número")
            return
        
        # Convertir la cantidad ingresada a número entero
        cantidad_grupos = int(cantidad)

        # Validar que la cantidad mínima de grupos sea 2
        if cantidad_grupos < 2:
            messagebox.showerror("Error", "La cantidad mínima de grupos es 2")
            return
        

        # Cada grupo clasifica 2 selecciones.
        # Esto valida que la cantidad de clasificados permita crear fases eliminatorias correctas
        clasificados_posibles = cantidad_grupos * 2
        if clasificados_posibles not in [2, 4, 8, 16, 32]:
            messagebox.showerror("Error", "La cantidad de grupos debe ser 2, 4, 8 o 16\n"
                                 "para generar 2, 4, 8, 16 o 32 clasificados")
            return
        
         # Validar que existan selecciones registradas
        if len(lista_selecciones) == 0:
            messagebox.showerror("Error", "Primero debe registrar selecciones antes de crear grupos.")
            return
        
         # Validar que cada grupo tenga exactamente 4 selecciones
        if len(lista_selecciones) != cantidad_grupos * 4:
            messagebox.showerror("Error", 
                f"La cantidad de selecciones debe ser igual a grupos x 4.\n"
                f"Tiene {len(lista_selecciones)} selecciones → use {len(lista_selecciones) // 4} grupos")
            return
        
        # Validar que cada selección tenga al menos 11 jugadores y entrenador asignado
        for seleccion in lista_selecciones:
            if len(seleccion.get_jugadores()) < 11:
                messagebox.showerror("Error", f"La selección {seleccion.get_pais().get_nombre()} debe tener al menos 11 jugadores")
                return
            if seleccion.get_entrenador() is None:
                messagebox.showerror("Error", f"La selección {seleccion.get_pais().get_nombre()} no tiene entrenador asignado")
                return

        # Registrar las selecciones en el mundial solo si todavía no se han registrado
        # Esto evita duplicarlas si el usuario presiona el botón más de una vez
        if len(mundial.get_selecciones()) == 0: 
            for seleccion in lista_selecciones:
                mundial.registrar_seleccion(seleccion)

        # Crear los grupos usando el método de la clase Mundial
        creado = mundial.crear_grupos(cantidad_grupos)

        # Si crear_grupos retorna False, se muestra un error
        if creado == False:
            messagebox.showerror("Error", "No se pudieron crear los grupos")
            return
        
        # Limpiar el cuadro de texto antes de mostrar los grupos
        resultado_texto.delete("1.0", tk.END)

        # Mostrar cada grupo y sus equipos en pantalla
        for grupo in mundial.get_grupos():
            resultado_texto.insert(tk.END, grupo.get_nombre_grupo() + "\n")

            for equipo in grupo.get_equipos():
                resultado_texto.insert(tk.END, "- " + equipo.get_pais().get_nombre() + "\n")

            resultado_texto.insert(tk.END, "\n")
        
         # Mensaje de éxito
        messagebox.showinfo("Éxito", "Grupos creados correctamente")
        # Desactivar el botón para evitar crear grupos otra vez
        btn_crear_grupos.config(state="disabled")

    # Botón para ejecutar la configuración del mundial
    btn_crear_grupos = tk.Button(ventana,text="Crear grupos",font=FUENTE_BOTON,bg=FONDO_CARD,fg=TEXTO_BLANCO,
            command=configurar)
    btn_crear_grupos.pack(pady=5, fill="x", padx=40)

    # Botón para regresar al menú principal
    tk.Button(ventana,text="🔙 Volver al menú",font=FUENTE_BOTON,bg=FONDO_CARD,fg=TEXTO_AZUL,
            command=mostrar_menu).pack(pady=5, fill="x", padx=40)
    
def mostrar_jugar_mundial(ventana, mundial, mostrar_menu):
    """
    Muestra la pantalla para jugar el mundial.
    #E: ventana (tk.Tk), mundial (Mundial), mostrar_menu (function)
    #S: No retorna nada, dibuja la pantalla para simular el mundial
    #R: El mundial debe tener grupos creados previamente
    """
    # Limpia la ventana actual
    limpiar_ventana(ventana)
    ventana.configure(bg=FONDO_OSCURO)

    # Título principal de la pantalla
    tk.Label(ventana, text="▶️ Jugar Mundial",font=FUENTE_TITULO, bg=FONDO_OSCURO,  fg=DORADO).pack(pady=20)

    # Cuadro de texto donde se mostrarán tablas, fases y campeón
    # Empieza deshabilitado para que el usuario no pueda editarlo
    resultado_texto = tk.Text(ventana, width=65, height=22, bg=FONDO_CARD, fg=TEXTO_BLANCO, font=("Arial", 10), state="disabled") 
    resultado_texto.pack(pady=10)

    def simular_grupos():
        """
        Simula todos los partidos de la fase de grupos
        y muestra las tablas de posiciones.
        """
        #Validar que los grupos ya hayan sido creados
        if len(mundial.get_grupos()) == 0:
            messagebox.showerror("Error", "Primero debe configurar los grupos.")
            return
        
        # Simular los partidos de todos los grupos
        mundial.jugar_fase_grupos()

        # Habilitar el cuadro de texto para poder escribir resultados
        resultado_texto.config(state="normal")  
        resultado_texto.delete("1.0", tk.END)

        # Mostrar las tablas de grupo
        resultado_texto.insert(tk.END, "TABLAS DE GRUPOS\n\n")
        resultado_texto.insert(tk.END, mundial.mostrar_tabla_general())

        # Bloquear el cuadro de texto nuevamente
        resultado_texto.config(state="disabled")

        # Mensaje de éxito
        messagebox.showinfo("Éxito", "Fase de grupos simulada correctamente.")
        btn_simular_fase.config(state="disabled")
        btn_simular_eliminatorias.config(state="normal")

    def simular_eliminatorias():
        """
        Simula las fases eliminatorias, determina el campeón
        y genera los reportes del mundial.
        """
        # Validar que existan grupos configurados
        if len(mundial.get_grupos()) == 0:
            messagebox.showerror("Error", "Primero debe configurar los grupos.")
            return
        
        # Ejecutar las fases eliminatorias y obtener el campeón
        campeon = mundial.determinar_campeon()

        # Habilitar el cuadro de texto para escribir los resultados
        resultado_texto.config(state="normal")
        # Mostrar las fases eliminatorias
        resultado_texto.insert(tk.END, "\nFASES ELIMINATORIAS\n\n")
        
        for fase in mundial.get_fases():  
            resultado_texto.insert(tk.END, fase.mostrar_juegos())
            resultado_texto.insert(tk.END, "\n")

        # Mostrar el campeón    
        resultado_texto.insert(tk.END, "\nCAMPEÓN\n")
        resultado_texto.insert(tk.END, campeon.get_pais().get_nombre())

        # Bloquear el cuadro de texto nuevamente
        resultado_texto.config(state="disabled")

        # Generar archivos txt con los reportes del mundial
        mundial.generar_reporte()

        # Mensaje de éxito
        messagebox.showinfo("Éxito", "Mundial finalizado correctamente.")
    
        # Desactivar el botón para evitar repetir las eliminatorias
        btn_simular_eliminatorias.config(state="disabled")

    # Botón para simular fase de grupos
    btn_simular_fase= tk.Button(ventana, text="Simular fase de grupos", font=FUENTE_BOTON, bg=FONDO_CARD, fg=TEXTO_BLANCO, command=simular_grupos)
    btn_simular_fase.pack(pady=5, fill="x", padx=40)

    # Botón para simular eliminatorias.
    # Inicia deshabilitado porque primero se debe jugar la fase de grupos.
    btn_simular_eliminatorias= tk.Button(ventana, text="Simular eliminatorias y campeón", font=FUENTE_BOTON, bg=FONDO_CARD, fg=TEXTO_BLANCO,command=simular_eliminatorias, state="disabled")
    btn_simular_eliminatorias.pack(pady=5, fill="x", padx=40)

    # Botón para regresar al menú principal
    tk.Button(ventana, text="🔙 Volver al menú", font=FUENTE_BOTON, bg=FONDO_CARD, fg=TEXTO_AZUL,
        command=mostrar_menu).pack(pady=5, fill="x", padx=40)
    
def mostrar_estadisticas(ventana, mundial, mostrar_menu):
    """
    Muestra las estadísticas y rankings del mundial.
    #E: ventana (tk.Tk), mundial (Mundial), mostrar_menu (funcion)
    #S: No retorna nada, dibuja la pantalla de estadísticas
    #R: El mundial debe haberse jugado previamente
    """
    limpiar_ventana(ventana)
    ventana.configure(bg=FONDO_OSCURO)

    # Titulo de la ventana
    tk.Label(ventana,text="📊 Estadísticas / Rankings", font=FUENTE_TITULO, bg=FONDO_OSCURO, fg=DORADO).pack(pady=10)

    # Frame principal donde estara el texto y la tabla
    frame_contenido = tk.Frame(ventana, bg=FONDO_OSCURO)
    frame_contenido.pack(fill="both", expand=True, padx=20, pady=5)

    # Cuadro donde se mostraran las estadisticas 
    resultado_texto = tk.Text(frame_contenido,width=70, height=16, bg=FONDO_CARD, fg=TEXTO_BLANCO, font=("Arial", 10), state="disabled")
    resultado_texto.pack(pady=5)

    # Framepara la tabla de posiciones
    frame_tabla = tk.Frame(frame_contenido, bg=FONDO_OSCURO)
    frame_tabla.pack(fill="both", expand=True, pady=5)


    tk.Label(frame_tabla, text="TABLA GENERAL DE SELECCIONES", font=FUENTE_BOTON, bg=FONDO_OSCURO, fg=DORADO).pack(pady=5)

    # Crear tabla
    tabla_selecciones = ttk.Treeview(frame_tabla, columns=("seleccion", "pts", "gf", "gc", "dg"), show="headings", height=8)

    # Encabezados
    tabla_selecciones.heading("seleccion", text="Selección")
    tabla_selecciones.heading("pts", text="Pts")
    tabla_selecciones.heading("gf", text="GF")
    tabla_selecciones.heading("gc", text="GC")
    tabla_selecciones.heading("dg", text="DG")

    # Tamañao de las columnas
    tabla_selecciones.column("seleccion", width=180)
    tabla_selecciones.column("pts", width=50, anchor="center")
    tabla_selecciones.column("gf", width=50, anchor="center")
    tabla_selecciones.column("gc", width=50, anchor="center")
    tabla_selecciones.column("dg", width=50, anchor="center")

    tabla_selecciones.pack(pady=5)

    def mostrar_datos():

        # Habilitar cuandro de texto para escibir
        resultado_texto.config(state="normal")
        resultado_texto.delete("1.0", tk.END)

        # Vaciar la tabla por si ya tenia datos
        for item in tabla_selecciones.get_children():
            tabla_selecciones.delete(item)

        # Mostrar el campeor si ya existe
        if mundial.get_campeon() is not None:
            resultado_texto.insert(tk.END, "CAMPEÓN\n")
            resultado_texto.insert(tk.END, mundial.get_campeon().get_pais().get_nombre() + "\n\n")


        # SELECCION CON MAS GOLES 

        max_goles = -1
        selecciones_mas_goles = []

        for seleccion in mundial.get_selecciones():
            goles = seleccion.get_total_goles_favor()

            if goles > max_goles:
                max_goles = goles
                selecciones_mas_goles = [seleccion]
            elif goles == max_goles:
                selecciones_mas_goles.append(seleccion)

        resultado_texto.insert(tk.END, "SELECCIÓN(ES) CON MÁS GOLES\n")
        for seleccion in selecciones_mas_goles:
            resultado_texto.insert(tk.END, seleccion.get_pais().get_nombre() +
                " | Goles: " + str(max_goles) + "\n")

        resultado_texto.insert(tk.END, "\n")

        # SELECCIONES CON MAS TARJETAS AMARILLAS

        max_amarillas = -1
        selecciones_mas_amarillas = []

        for seleccion in mundial.get_selecciones():
            amarillas = seleccion.get_total_tarjetas_amarillas()

            if amarillas > max_amarillas:
                max_amarillas = amarillas
                selecciones_mas_amarillas = [seleccion]
            elif amarillas == max_amarillas:
                selecciones_mas_amarillas.append(seleccion)

        resultado_texto.insert(tk.END, "SELECCIÓN(ES) CON MÁS TARJETAS AMARILLAS\n")
        for seleccion in selecciones_mas_amarillas:
            resultado_texto.insert(tk.END, seleccion.get_pais().get_nombre() +
                " | Amarillas: " + str(max_amarillas) + "\n")

        resultado_texto.insert(tk.END, "\n")

        # SELECCIONES CON MAS TARJETAS ROJAS
        max_rojas = -1
        selecciones_mas_rojas = []

        for seleccion in mundial.get_selecciones():
            rojas = seleccion.get_total_tarjetas_rojas()

            if rojas > max_rojas:
                max_rojas = rojas
                selecciones_mas_rojas = [seleccion]
            elif rojas == max_rojas:
                selecciones_mas_rojas.append(seleccion)

        resultado_texto.insert(tk.END, "SELECCIÓN(ES) CON MÁS TARJETAS ROJAS\n")
        for seleccion in selecciones_mas_rojas:
            resultado_texto.insert(tk.END, seleccion.get_pais().get_nombre() +
                " | Rojas: " + str(max_rojas) + "\n")

        resultado_texto.insert(tk.END, "\nRANKING DE GOLEADORES\n\n")

        # Guardar todos los jugadores junto con su seleccion
        jugadores = []
        for seleccion in mundial.get_selecciones():
            for jugador in seleccion.get_jugadores():
                jugadores.append([jugador, seleccion])

        # Ordenar por cantidad de goles
        for i in range(len(jugadores)):
            for j in range(len(jugadores) - 1):
                if jugadores[j][0].get_goles() < jugadores[j + 1][0].get_goles():
                    jugadores[j], jugadores[j + 1] = jugadores[j + 1], jugadores[j]

        # Mostrar unicamente a quienes anotaron al menos un gol
        for dato in jugadores:
            jugador = dato[0]
            seleccion = dato[1]

            if jugador.get_goles() > 0:
                resultado_texto.insert(
                    tk.END,
                    jugador.get_nombre() + " " + jugador.get_apellido() +
                    " | " + seleccion.get_pais().get_nombre() +
                    " | Goles: " + str(jugador.get_goles()) + "\n")
                
        # TARJETAS POR SELECCIÓN

        resultado_texto.insert(tk.END, "\nTARJETAS POR SELECCIÓN\n\n")

        for seleccion in mundial.get_selecciones():
            resultado_texto.insert(tk.END, seleccion.get_pais().get_nombre() +
                " | Amarillas: " + str(seleccion.get_total_tarjetas_amarillas()) +
                " | Rojas: " + str(seleccion.get_total_tarjetas_rojas()) + "\n")
            
        # TABLA GENERAL DE SELECCIONES

        tabla_general = []

        # Recorre todos los grupos y guarda sus tablas en una sola lista
        for grupo in mundial.get_grupos():
            tabla = grupo.calcular_tabla()

            for fila in tabla:
                tabla_general.append(fila)

         # Ordenar tabla general:
        # 1. puntos
        # 2. diferencia de goles
        # 3. goles a favor
        for i in range(len(tabla_general)):
            for j in range(len(tabla_general) - 1):
                if tabla_general[j][1] < tabla_general[j + 1][1]:
                    tabla_general[j], tabla_general[j + 1] = tabla_general[j + 1], tabla_general[j]
                elif tabla_general[j][1] == tabla_general[j + 1][1]:
                    if tabla_general[j][4] < tabla_general[j + 1][4]:
                        tabla_general[j], tabla_general[j + 1] = tabla_general[j + 1], tabla_general[j]
                    elif tabla_general[j][4] == tabla_general[j + 1][4]:
                        if tabla_general[j][2] < tabla_general[j + 1][2]:
                            tabla_general[j], tabla_general[j + 1] = tabla_general[j + 1], tabla_general[j]

        # Insertar datos ordenados en la tabla visual
        for fila in tabla_general:
            seleccion = fila[0]
            puntos = fila[1]
            goles_favor = fila[2]
            goles_contra = fila[3]
            diferencia = fila[4]

            tabla_selecciones.insert("", tk.END, values=( seleccion.get_pais().get_nombre(), puntos, goles_favor, goles_contra, diferencia))

        # Bloquear el cuadro de texto para que el usuario no lo edite
        resultado_texto.config(state="disabled")
        # Desactivar el botón después de mostrar estadísticas
        btn_mostrar.config(state="disabled")

    # Botón para mostrar las estadísticas
    btn_mostrar = tk.Button(ventana, text="Mostrar estadísticas", font=FUENTE_BOTON, bg=FONDO_CARD, fg=TEXTO_BLANCO, command=mostrar_datos)
    btn_mostrar.pack(pady=5, fill="x", padx=40)

    # Botón para regresar al menú principal
    tk.Button( ventana, text="🔙 Volver al menú", font=FUENTE_BOTON, bg=FONDO_CARD, fg=TEXTO_AZUL, command=mostrar_menu).pack(pady=5, fill="x", padx=40)