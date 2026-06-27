import tkinter as tk
from tkinter import messagebox
from utilidades import limpiar_ventana
from seleccion import Seleccion
   
# Colores
FONDO_OSCURO = "#0a1628"
FONDO_CARD = "#0d2137"
FONDO2 = "#4384b6"
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

    # Frame principal donde estara el resumen y estadisticas
    frame_contenido = tk.Frame(ventana, bg=FONDO_OSCURO)
    frame_contenido.pack(fill="both", expand=True, padx=20, pady=5)

    # Cuadro donde se mostraran las estadisticas 
    resultado_texto = tk.Text(frame_contenido,width=70, height=16, bg=FONDO_CARD, fg=TEXTO_BLANCO, font=("Arial", 10), state="disabled")
    resultado_texto.pack(pady=5)

    def mostrar_datos():
        """
        Muestra el resumen de estadísticas del mundial incluyendo campeón,
        selección con más goles y selecciones con más tarjetas.
        #E: No recibe parámetros, lee los datos del objeto mundial
        #S: No retorna nada, escribe los resultados en el cuadro de texto
        #R: El mundial debe haberse jugado previamente para tener datos
        """
        # Habilitar cuandro de texto para escibir
        resultado_texto.config(state="normal")
        resultado_texto.delete("1.0", tk.END)


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
            

        # Bloquear el cuadro de texto para que el usuario no lo edite
        resultado_texto.config(state="disabled")
        # Desactivar el botón después de mostrar estadísticas
        btn_mostrar.config(state="disabled")

  
    btn_mostrar = tk.Button(ventana, text="Mostrar Resumen", font=FUENTE_BOTON, bg=FONDO_CARD, fg=TEXTO_BLANCO, command=mostrar_datos)
    btn_mostrar.pack(pady=5, fill="x", padx=40)

    tk.Button( ventana, text="Ver ranking de goleadores", font=FUENTE_BOTON, bg=FONDO_CARD,  fg=TEXTO_BLANCO,
        command=lambda: mostrar_ventana_ranking_goleadores(ventana, mundial, mostrar_menu)).pack(pady=5, fill="x", padx=40)

    tk.Button( ventana, text="Ver tarjetas por selección",font=FUENTE_BOTON, bg=FONDO_CARD, fg=TEXTO_BLANCO,
        command=lambda: mostrar_ventana_tarjetas_seleccion(ventana, mundial, mostrar_menu)).pack(pady=5, fill="x", padx=40)

    tk.Button(ventana,text="Ver tabla general", font=FUENTE_BOTON, bg=FONDO_CARD, fg=TEXTO_BLANCO,
        command=lambda: mostrar_ventana_tabla_general(ventana, mundial, mostrar_menu)).pack(pady=5, fill="x", padx=40)
    
    # Botón para regresar al menú principal
    tk.Button( ventana, text="🔙 Volver al menú", font=FUENTE_BOTON, bg=FONDO_CARD, fg=TEXTO_AZUL, 
        command=mostrar_menu).pack(pady=5, fill="x", padx=40)

def mostrar_ventana_tabla_general(ventana, mundial, mostrar_menu):
    """
    Muestra una ventana con la tabla general de selecciones.
    #E: mundial (Mundial)
    #S: No retorna nada, muestra la tabla general ordenada
    #R: El mundial debe tener grupos creados y jugados
    """

    # Crear una ventana independiente
    limpiar_ventana(ventana)
    ventana.title("Tabla General de Selecciones")
    ventana.configure(bg=FONDO_OSCURO)
    ventana.geometry("1000x650")

    # Título de la ventana
    tk.Label( ventana, text="TABLA GENERAL DE SELECCIONES", font=FUENTE_TITULO, bg=FONDO_OSCURO, fg=DORADO ).pack(pady=15)

    # Frame donde se dibujará la tabla
    frame_tabla = tk.Frame(ventana, bg=FONDO_OSCURO)
    frame_tabla.pack(padx=20, pady=10)

    # Encabezados de la tabla
    encabezados = ["#", "Selección", "Pts", "GF", "GC", "DG", "Fase"]

    # Crear la fila de encabezados
    for columna in range(len(encabezados)):
        ancho = 15
        if columna == 6:
            ancho = 22
        tk.Label(frame_tabla, text=encabezados[columna], font=("Arial", 11, "bold"), bg=FONDO2, fg=TEXTO_BLANCO, width=ancho, relief="solid", borderwidth=1 ).grid(row=0, column=columna)

    # Lista donde se guardará la tabla completa
    tabla_general = []

    # Recorrer cada grupo y agregar su tabla a la tabla general
    for grupo in mundial.get_grupos():

        tabla = grupo.calcular_tabla()

        for fila in tabla:
            tabla_general.append(fila)

    # Ordenar la tabla por:
    # 1. Puntos
    # 2. Diferencia de goles
    # 3. Goles a favor
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

    # Número de posición que aparecerá en la primera columna
    posicion = 1

    # Mostrar cada selección en una fila de la tabla
    for fila in tabla_general:

        seleccion = fila[0]
        puntos = fila[1]
        goles_favor = fila[2]
        goles_contra = fila[3]
        diferencia = fila[4]

        # Datos que se mostrarán en la fila
        datos = [posicion, seleccion.get_pais().get_nombre(), puntos, goles_favor, goles_contra, diferencia, seleccion.get_fase_alcanzada()]

        # Crear cada columna de la fila
        for columna in range(len(datos)):
            ancho = 15
            if columna == 6:
                ancho = 22
            tk.Label( frame_tabla, text=datos[columna], font=("Arial", 10), bg=FONDO_OSCURO, fg=TEXTO_BLANCO, width=ancho, relief="solid", borderwidth=1 ).grid(row=posicion, column=columna)

        # Aumentar el número de posición para la siguiente selección
        posicion += 1

    # Botón para cerrar la ventana
    tk.Button(ventana, text="Volver a estadísticas",  font=FUENTE_BOTON,  bg=FONDO_CARD,  fg=TEXTO_BLANCO, command=lambda: mostrar_estadisticas(ventana, mundial, mostrar_menu) ).pack(pady=15)

def mostrar_ventana_ranking_goleadores(ventana, mundial, mostrar_menu):
    """
    Muestra una ventana con el ranking de goleadores.
    #E: mundial (Mundial)
    #S: No retorna nada, muestra el ranking de goleadores
    #R: El mundial debe haberse jugado previamente
    """

    # Crear una nueva ventana independiente
    limpiar_ventana(ventana)
    ventana.title("Ranking de Goleadores")
    ventana.configure(bg=FONDO_OSCURO)
    ventana.geometry("750x600")

    # Título de la ventana
    tk.Label(ventana, text="RANKING DE GOLEADORES", font=FUENTE_TITULO, bg=FONDO_OSCURO, fg=DORADO).pack(pady=15)

    # Frame que contiene la tabla y el scroll
    frame_principal = tk.Frame(ventana, bg=FONDO_OSCURO)
    frame_principal.pack(pady=10)

    canvas = tk.Canvas(frame_principal, bg=FONDO_OSCURO, highlightthickness=0, width=640, height=400)
    canvas.pack(side="left")

    scroll = tk.Scrollbar(frame_principal, orient="vertical", command=canvas.yview)
    scroll.pack(side="left", fill="y")

    canvas.configure(yscrollcommand=scroll.set)

    # Frame donde se dibujará la tabla
    frame_tabla = tk.Frame(canvas, bg=FONDO_OSCURO)

    canvas.create_window((320, 0), window=frame_tabla, anchor="nw")

    # Actualizar el área desplazable cuando cambie el contenido
    frame_tabla.bind( "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")) )
    # Encabezados de la tabla
    encabezados = ["#", "Jugador", "Selección", "Goles"]

    # Crear la fila de encabezados
    for columna in range(len(encabezados)):
        tk.Label( frame_tabla, text=encabezados[columna], font=("Arial", 11, "bold"), bg=FONDO2,  fg=TEXTO_BLANCO, width=18, relief="solid", borderwidth=1).grid(row=0, column=columna)

    # Lista donde se almacenarán todos los jugadores junto con su selección
    jugadores = []

    # Recorrer todas las selecciones y guardar sus jugadores
    for seleccion in mundial.get_selecciones():
        for jugador in seleccion.get_jugadores():
            jugadores.append([jugador, seleccion])

    # Ordenar los jugadores de mayor a menor cantidad de goles
    for i in range(len(jugadores)):
        for j in range(len(jugadores) - 1):

            if jugadores[j][0].get_goles() < jugadores[j + 1][0].get_goles():
                jugadores[j], jugadores[j + 1] = jugadores[j + 1], jugadores[j]

    # Posición que ocupará cada jugador en el ranking
    posicion = 1

    # Mostrar únicamente los jugadores que anotaron al menos un gol
    for dato in jugadores:

        jugador = dato[0]
        seleccion = dato[1]

        if jugador.get_goles() > 0:

            # Datos que se mostrarán en cada fila
            datos = [posicion, jugador.get_nombre() + " " + jugador.get_apellido(), seleccion.get_pais().get_nombre(), jugador.get_goles()]

            # Crear las columnas de la fila
            for columna in range(len(datos)):
                tk.Label(frame_tabla, text=datos[columna],font=("Arial", 10), bg=FONDO_OSCURO,  fg=TEXTO_BLANCO, width=18, relief="solid", borderwidth=1 ).grid(row=posicion, column=columna)

            # Aumentar la posición para el siguiente jugador
            posicion += 1

    # Botón para cerrar la ventana
    tk.Button( ventana, text="Volver a estadísticas", font=FUENTE_BOTON, bg=FONDO_CARD,  fg=TEXTO_BLANCO, command=lambda: mostrar_estadisticas(ventana, mundial, mostrar_menu)).pack(pady=(20, 15))


def mostrar_ventana_tarjetas_seleccion(ventana, mundial, mostrar_menu):
    """
    Muestra una ventana con las tarjetas acumuladas por selección.
    #E: mundial (Mundial)
    #S: No retorna nada, muestra una tabla con tarjetas amarillas y rojas
    #R: El mundial debe haberse jugado previamente
    """

    limpiar_ventana(ventana)
    ventana.title("Tarjetas por Selección")
    ventana.configure(bg=FONDO_OSCURO)
    ventana.geometry("750x600")

    # Título de la ventana
    tk.Label(ventana, text="TARJETAS POR SELECCIÓN", font=FUENTE_TITULO, bg=FONDO_OSCURO,  fg=DORADO).pack(pady=15)

    # Frame donde se dibujará la tabla
    frame_tabla = tk.Frame(ventana, bg=FONDO_OSCURO)
    frame_tabla.pack(padx=20, pady=10)

    # Encabezados de la tabla
    encabezados = ["#", "Selección", "Amarillas", "Rojas"]

    # Crear la fila de encabezados
    for columna in range(len(encabezados)):
        tk.Label(frame_tabla, text=encabezados[columna], font=("Arial", 11, "bold"), bg=FONDO2, fg=TEXTO_BLANCO, width=18, relief="solid",borderwidth=1).grid(row=0, column=columna)

    # Copiar las selecciones para ordenarlas sin modificar la lista original
    selecciones = mundial.get_selecciones()[:]

    # Ordenar por total de tarjetas, de mayor a menor
    for i in range(len(selecciones)):
        for j in range(len(selecciones) - 1):
            
            total_actual = (selecciones[j].get_total_tarjetas_amarillas() + selecciones[j].get_total_tarjetas_rojas())
            total_siguiente = (selecciones[j + 1].get_total_tarjetas_amarillas() + selecciones[j + 1].get_total_tarjetas_rojas())

            if total_actual < total_siguiente:
                selecciones[j], selecciones[j + 1] = selecciones[j + 1], selecciones[j]

    posicion = 1

    # Mostrar cada selección en una fila
    for seleccion in selecciones:
        datos = [posicion, seleccion.get_pais().get_nombre(), seleccion.get_total_tarjetas_amarillas(), seleccion.get_total_tarjetas_rojas()]

        # Crear columnas de la fila
        for columna in range(len(datos)):
            tk.Label(frame_tabla, text=datos[columna], font=("Arial", 10), bg=FONDO_OSCURO, fg=TEXTO_BLANCO, width=18, relief="solid", borderwidth=1).grid(row=posicion, column=columna)

        posicion += 1

    # Botón para cerrar la ventana
    tk.Button(ventana, text="Volver a estadísticas", font=FUENTE_BOTON, bg=FONDO_CARD, fg=TEXTO_BLANCO,
        command=lambda: mostrar_estadisticas(ventana, mundial, mostrar_menu)).pack(pady=15)
