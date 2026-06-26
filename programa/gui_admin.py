import tkinter as tk
from tkinter import messagebox
from utilidades import limpiar_ventana, validar_fecha
from pais import Pais
from seleccion import Seleccion
from entrenador import Entrenador
from futbolista import Futbolista
from persistencia import guardar_paises, guardar_selecciones, guardar_jugadores

# Estilos
FONDO_OSCURO = "#0a1628"
FONDO_CARD = "#0d2137"
DORADO = "#f1c40f"
TEXTO_BLANCO = "#ffffff"
TEXTO_AZUL = "#7fb3d3"
FUENTE_TITULO = ("Arial", 18, "bold")
FUENTE_BOTON = ("Arial", 11)
FUENTE_LABEL = ("Arial", 10)

def mostrar_paises(ventana, lista_paises, mostrar_menu, lista_selecciones):
    """
    Muestra el formulario para registrar países y el listado de países registrados.
    #E: ventana (tk.Tk), lista_paises (list), mostrar_menu (function)
    #S: No retorna nada, dibuja los widgets en la ventana
    #R: La ventana debe estar inicializada correctamente
    """
    limpiar_ventana(ventana)
    ventana.configure(bg=FONDO_OSCURO)
    
    tk.Label(ventana, text="🌏 Registrar País", font=FUENTE_TITULO, bg=FONDO_OSCURO, fg=DORADO).pack(pady=10)
    
    tk.Label(ventana, text="Código FIFA:", 
         font=FUENTE_LABEL, bg=FONDO_OSCURO, fg=TEXTO_BLANCO).pack()
    entry_codigo = tk.Entry(ventana, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                        insertbackground=TEXTO_BLANCO, font=FUENTE_BOTON)
    entry_codigo.pack()
    
    tk.Label(ventana, text="Nombre:",
              font=FUENTE_LABEL, bg=FONDO_OSCURO, fg=TEXTO_BLANCO).pack()
    entry_nombre = tk.Entry(ventana, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                        insertbackground=TEXTO_BLANCO, font=FUENTE_BOTON)
    entry_nombre.pack()
    
    tk.Label(ventana, text="Continente:",
              font=FUENTE_LABEL, bg=FONDO_OSCURO, fg=TEXTO_BLANCO).pack()
    entry_continente = tk.Entry(ventana, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                        insertbackground=TEXTO_BLANCO, font=FUENTE_BOTON)
    entry_continente.pack()
   
    tk.Label(ventana, text="Ranking FIFA:", 
             font=FUENTE_LABEL, bg=FONDO_OSCURO, fg=TEXTO_BLANCO).pack()
    entry_ranking = tk.Entry(ventana, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                        insertbackground=TEXTO_BLANCO, font=FUENTE_BOTON)
    entry_ranking.pack()
    
    def registrar_pais():
        """
        Registra un pais nuevo con sus atributos
        #E: No recibe parámetros, lee los valores de los campos Entry
        #S: No retorna nada, agrega el objeto Pais a lista_paises y actualiza el listbox
        #R: La ventana debe estar inicializada correctamente
        """
        codigo = entry_codigo.get()
        nombre = entry_nombre.get()
        continente = entry_continente.get()
        ranking = entry_ranking.get()
        
        if codigo == "" or nombre == "" or continente == "" or ranking == "":
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        if not ranking.isdigit():
            messagebox.showerror("Error", "El ranking debe ser un número entero positivo")
            return
    
        nuevo_pais = Pais(codigo, nombre, continente, int(ranking))
        lista_paises.append(nuevo_pais)
        guardar_paises(lista_paises)
        
        messagebox.showinfo("Éxito", f"País {nombre} registrado correctamente")
        listbox_paises.insert(tk.END, f"{codigo} - {nombre} - {continente} - Ranking: {ranking}")

        entry_codigo.delete(0, tk.END)
        entry_nombre.delete(0, tk.END)
        entry_continente.delete(0, tk.END)
        entry_ranking.delete(0, tk.END)
       
    btn_registrar = tk.Button(ventana, text="Registrar País",font=FUENTE_BOTON, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                           activebackground="#1a3a5c", activeforeground=TEXTO_BLANCO,
                           relief="flat", padx=20, pady=10, cursor="hand2",command=registrar_pais)
    btn_registrar.pack(pady=15, fill="x", padx=40)
    
    tk.Label(ventana, text="Países registrados:",font=FUENTE_LABEL, bg=FONDO_OSCURO, fg=TEXTO_BLANCO).pack()
    listbox_paises = tk.Listbox(ventana, bg=FONDO_CARD, fg=TEXTO_BLANCO, 
                             font=FUENTE_BOTON, width=50, height=8)
    for pais in lista_paises:
        listbox_paises.insert(tk.END, f"{pais.get_codigo_fifa()} - {pais.get_nombre()} - {pais.get_continente()} - Ranking: {pais.get_ranking_fifa()}")
    listbox_paises.pack(pady=15, fill="x", padx=40)
    
    btn_volver = tk.Button(ventana, text="🔙  Volver",font=FUENTE_BOTON, bg=FONDO_CARD, fg=TEXTO_AZUL,
                           activebackground="#1a3a5c", activeforeground=TEXTO_BLANCO,
                           relief="flat", padx=20, pady=10, cursor="hand2",
                       command=lambda: mostrar_admin_paises_selecciones(ventana, lista_paises, lista_selecciones, mostrar_menu))
    btn_volver.pack(pady=15, fill="x", padx=40)

def mostrar_admin_paises_selecciones(ventana, lista_paises, lista_selecciones, mostrar_menu):
    """
    Muestra el submenú de administración de países y selecciones.
    #E: ventana (tk.Tk), lista_paises (list), lista_selecciones (list), mostrar_menu (function)
    #S: No retorna nada, dibuja los widgets en la ventana
    #R: La ventana debe estar inicializada correctamente
    """
    limpiar_ventana(ventana)
    ventana.configure(bg=FONDO_OSCURO)
    
    tk.Label(ventana, text="Países y Selecciones",
             font=FUENTE_TITULO, bg=FONDO_OSCURO, fg=DORADO).pack(pady=20)
    
    btn_paises = tk.Button(ventana, text="🌎 Registrar País",
                           font=FUENTE_BOTON, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                           activebackground="#1a3a5c", activeforeground=TEXTO_BLANCO,
                           relief="flat", padx=20, pady=10, cursor="hand2",
                           command=lambda: mostrar_paises(ventana, lista_paises, mostrar_menu, lista_selecciones))
    btn_paises.pack(pady=5, fill="x", padx=40)
    
    btn_selecciones = tk.Button(ventana, text="⚽  Registrar Selección",
                           font=FUENTE_BOTON, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                           activebackground="#1a3a5c", activeforeground=TEXTO_BLANCO,
                           relief="flat", padx=20, pady=10, cursor="hand2",
                           command=lambda: mostrar_selecciones(ventana, lista_paises, lista_selecciones, mostrar_menu))
    btn_selecciones.pack(pady=5, fill="x", padx=40)
    
    btn_volver = tk.Button(ventana, text="🔙  Volver al Menú",
                           font=FUENTE_BOTON, bg=FONDO_CARD, fg=TEXTO_AZUL,
                           activebackground="#1a3a5c", activeforeground=TEXTO_BLANCO,
                           relief="flat", padx=20, pady=10, cursor="hand2",
                           command=mostrar_menu)
    btn_volver.pack(pady=15, fill="x", padx=40)
   
    
def mostrar_selecciones(ventana, lista_paises, lista_selecciones, mostrar_menu):
    """
    Muestra el formulario para registrar una seleccion y el listado de países y selecciones registradas.
    #E: ventana (tk.Tk), lista_paises (list), mostrar_menu (function), lista_selecciones (list)
    #S: No retorna nada, dibuja los widgets en la ventana
    #R: La ventana debe estar inicializada correctamente
    """
    limpiar_ventana(ventana)
    ventana.configure(bg=FONDO_OSCURO)
    
    tk.Label(ventana, text="Registrar Seleccion", 
                font=FUENTE_TITULO, bg=FONDO_OSCURO, fg=DORADO).pack(pady=20) 
    
    tk.Label(ventana, text="Código del equipo:", 
             bg=FONDO_OSCURO, fg=TEXTO_BLANCO, font=FUENTE_LABEL).pack()
    entry_codigo_equipo = tk.Entry(ventana, bg=FONDO_CARD, fg=TEXTO_BLANCO, 
                                    insertbackground=TEXTO_BLANCO, font=FUENTE_BOTON)
    entry_codigo_equipo.pack()

    tk.Label(ventana, text="Selecciona un pais:", 
             bg=FONDO_OSCURO, fg=TEXTO_BLANCO, font=FUENTE_LABEL).pack()
    
    listbox_paises = tk.Listbox(ventana,  bg=FONDO_CARD, fg=TEXTO_BLANCO, font=FUENTE_BOTON, width=50, height=6)
    for pais in lista_paises:       
        listbox_paises.insert(tk.END, pais.get_nombre())
    listbox_paises.pack(pady=5)
    
    def registrar_seleccion():
        """
        Registra una seleccion nueva con sus atributos
        #E: No recibe parámetros, lee los valores de los campos Entry
        #S: No retorna nada, agrega el objeto Seleccion a lista_selecciones y actualiza el listbox
        #R: La ventana debe estar inicializada correctamente
        """
        codigo = entry_codigo_equipo.get()
        seleccion = listbox_paises.curselection()
        
        if codigo == "":
            messagebox.showerror("Error", "El código es obligatorio")
            return
        
        if not seleccion:
            messagebox.showerror("Error", "Debe seleccionar un país")
            return
        
        pais_elegido = lista_paises[seleccion[0]]
        nueva_seleccion = Seleccion(codigo, pais_elegido, None)
        lista_selecciones.append(nueva_seleccion)
        guardar_selecciones(lista_selecciones)
        
        listbox_seleccion.insert(tk.END, f"{codigo} - {pais_elegido.get_nombre()}")
        messagebox.showinfo("Éxito", f"Selección {codigo} registrada correctamente")
        
        entry_codigo_equipo.delete(0, tk.END)
        
    btn_registrar_selec = tk.Button(ventana, text="Registrar Selección",bg=FONDO_CARD, fg=TEXTO_BLANCO, activebackground="#1a3a5c", 
                                        activeforeground=TEXTO_BLANCO, relief="flat", padx=20, pady=10, cursor="hand2",command=registrar_seleccion)    
    btn_registrar_selec.pack(pady=10, fill="x", padx=40)

    tk.Label(ventana, text="Selecciones registradas:", bg=FONDO_OSCURO, 
                fg=TEXTO_BLANCO, font=FUENTE_LABEL).pack()
    
    listbox_seleccion = tk.Listbox(ventana, bg=FONDO_CARD, fg=TEXTO_BLANCO, font=FUENTE_BOTON, width=50, height=6)
    for seleccion in lista_selecciones:       
        listbox_seleccion.insert(tk.END, seleccion.get_codigo_equipo())
    listbox_seleccion.pack(pady=5)
    
    btn_volver = tk.Button(ventana, text="🔙  Volver", bg=FONDO_CARD, fg=TEXTO_BLANCO, activebackground="#1a3a5c", 
                            activeforeground=TEXTO_BLANCO, relief="flat", padx=20, pady=10, cursor="hand2",
                                command=lambda: mostrar_admin_paises_selecciones(ventana, lista_paises, lista_selecciones, mostrar_menu))
    btn_volver.pack(pady=10, fill="x", padx=40)

def mostrar_admin_entrenadores_jugadores(ventana, lista_entrenadores, lista_jugadores, lista_selecciones, mostrar_menu):
    """
    Muestra el submenú de administración de entrenadores y jugadores.
    #E: ventana (tk.Tk), lista_entrenadores (list), lista_jugadores (list), mostrar_menu (function)
    #S: No retorna nada, dibuja los widgets en la ventana
    #R: La ventana debe estar inicializada correctamente
    """
    limpiar_ventana(ventana)
    ventana.configure(bg=FONDO_OSCURO)
    
    tk.Label(ventana, text="Administrar Entrenadores y Jugadores",
                font=FUENTE_TITULO, bg=FONDO_OSCURO, fg=DORADO).pack(pady=20)
    
    btn_registrar_entrenador = tk.Button(ventana, text="Registrar Entrenador",bg=FONDO_CARD, fg=TEXTO_BLANCO, activebackground="#1a3a5c", 
                                activeforeground=TEXTO_BLANCO, relief="flat", padx=20, pady=10, cursor="hand2",
                                command=lambda: mostrar_entrenador(ventana, lista_entrenadores, lista_jugadores, lista_selecciones,  mostrar_menu))
    btn_registrar_entrenador.pack(pady=10, fill="x", padx=40)
    
    btn_registrar_jugador = tk.Button(ventana, text="Registrar Jugador",bg=FONDO_CARD, fg=TEXTO_BLANCO, activebackground="#1a3a5c", 
                                activeforeground=TEXTO_BLANCO, relief="flat", padx=20, pady=10, cursor="hand2"
                                ,command=lambda: mostrar_jugador(ventana, lista_entrenadores, lista_jugadores, lista_selecciones, mostrar_menu))    
    btn_registrar_jugador.pack(pady=10, fill="x", padx=40)
        
    btn_volver = tk.Button(ventana, text="🔙  Volver al Menú", bg=FONDO_CARD, fg=TEXTO_BLANCO, activebackground="#1a3a5c", 
                             activeforeground=TEXTO_BLANCO, relief="flat", padx=20, pady=10, cursor="hand2",command=mostrar_menu)
    btn_volver.pack(pady=10, fill="x", padx=40)

def mostrar_entrenador(ventana, lista_entrenadores, lista_jugadores, lista_selecciones, mostrar_menu):
    """
    Muestra el formulario para registrar un entrenador y el listado de selecciones registradas.
    #E: ventana (tk.Tk), lista_entrenadores (list), mostrar_menu (function), lista_jugadores (list)
    #S: No retorna nada, dibuja los widgets en la ventana
    #R: La ventana debe estar inicializada correctamente
    """
    limpiar_ventana(ventana)
    ventana.configure(bg=FONDO_OSCURO)

    canvas = tk.Canvas(ventana, bg=FONDO_OSCURO, highlightthickness=0)
    scrollbar = tk.Scrollbar(ventana, orient="vertical", command=canvas.yview)
    
    frame = tk.Frame(canvas, bg=FONDO_OSCURO)
    frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    
    canvas.create_window((300, 0), window=frame, anchor="n")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    
    scrollbar.pack(side="right", fill="y")

    tk.Label(frame, text="Registrar Entrenador",
             font=FUENTE_TITULO, bg=FONDO_OSCURO, fg=DORADO).pack(pady=20)

    tk.Label(frame, text="Nombre:",
             bg=FONDO_OSCURO, fg=TEXTO_BLANCO, font=FUENTE_LABEL).pack()
    entry_nombre_entrenador = tk.Entry(frame, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                                       insertbackground=TEXTO_BLANCO, font=FUENTE_BOTON)
    entry_nombre_entrenador.pack()

    tk.Label(frame, text="Apellido:",
             bg=FONDO_OSCURO, fg=TEXTO_BLANCO, font=FUENTE_LABEL).pack()
    entry_apellido_entrenador = tk.Entry(frame, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                                         insertbackground=TEXTO_BLANCO, font=FUENTE_BOTON)
    entry_apellido_entrenador.pack()

    tk.Label(frame, text="Fecha nacimiento (DD/MM/AAAA):",
             bg=FONDO_OSCURO, fg=TEXTO_BLANCO, font=FUENTE_LABEL).pack()
    entry_fecha_naci_entrenador = tk.Entry(frame, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                                           insertbackground=TEXTO_BLANCO, font=FUENTE_BOTON)
    entry_fecha_naci_entrenador.pack()

    tk.Label(frame, text="Nacionalidad:",
             bg=FONDO_OSCURO, fg=TEXTO_BLANCO, font=FUENTE_LABEL).pack()
    entry_nacionalidad_entrenador = tk.Entry(frame, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                                             insertbackground=TEXTO_BLANCO, font=FUENTE_BOTON)
    entry_nacionalidad_entrenador.pack()

    tk.Label(frame, text="Licencia:",
             bg=FONDO_OSCURO, fg=TEXTO_BLANCO, font=FUENTE_LABEL).pack()
    entry_licencia_entrenador = tk.Entry(frame, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                                         insertbackground=TEXTO_BLANCO, font=FUENTE_BOTON)
    entry_licencia_entrenador.pack()

    tk.Label(frame, text="Años de experiencia:",
             bg=FONDO_OSCURO, fg=TEXTO_BLANCO, font=FUENTE_LABEL).pack()
    entry_anios_exp_entrenador = tk.Entry(frame, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                                          insertbackground=TEXTO_BLANCO, font=FUENTE_BOTON)
    entry_anios_exp_entrenador.pack()

    tk.Label(frame, text="Sistema de juego:",
             bg=FONDO_OSCURO, fg=TEXTO_BLANCO, font=FUENTE_LABEL).pack()
    entry_sistema_juego_entrenador = tk.Entry(frame, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                                              insertbackground=TEXTO_BLANCO, font=FUENTE_BOTON)
    entry_sistema_juego_entrenador.pack()

    tk.Label(frame, text="Selecciona una seleccion:",
             bg=FONDO_OSCURO, fg=TEXTO_BLANCO, font=FUENTE_LABEL).pack()
    listbox_seleccion = tk.Listbox(frame, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                                   font=FUENTE_BOTON, width=50, height=6)
    for seleccion in lista_selecciones:
        listbox_seleccion.insert(tk.END, seleccion.get_codigo_equipo())
    listbox_seleccion.pack(pady=5)

    def registrar_entrenador():
        """
        Registra un entrenador nuevo con sus atributos
        #E: No recibe parámetros, lee los valores de los campos Entry
        #S: No retorna nada, agrega el objeto Entrenador a lista_entrenadores y actualiza el listbox
        #R: La ventana debe estar inicializada correctamente
        """
        nombre = entry_nombre_entrenador.get()
        apellido = entry_apellido_entrenador.get()
        fecha_nacimiento = entry_fecha_naci_entrenador.get()
        nacionalidad = entry_nacionalidad_entrenador.get()
        licencia = entry_licencia_entrenador.get()
        anios_exp = entry_anios_exp_entrenador.get()
        sistema_juego = entry_sistema_juego_entrenador.get()
        seleccion = listbox_seleccion.curselection()

        if nombre == "" or apellido == "" or fecha_nacimiento == "" or nacionalidad == "" or licencia == "" or anios_exp == "" or sistema_juego == "":
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        if not validar_fecha(fecha_nacimiento):
            messagebox.showerror("Error", "La fecha debe tener el formato DD/MM/AAAA")
            return
        if not anios_exp.isdigit():
            messagebox.showerror("Error", "Los años de experiencia debe ser un número entero positivo")
            return

        nuevo_entrenador = Entrenador(nombre, apellido, fecha_nacimiento, nacionalidad,
                                      licencia, int(anios_exp), sistema_juego)
        if seleccion:
            seleccion_elegida = lista_selecciones[seleccion[0]]
            seleccion_elegida.asignar_entrenador(nuevo_entrenador)

        lista_entrenadores.append(nuevo_entrenador)
        messagebox.showinfo("Éxito", f"Entrenador {nombre} registrado correctamente")
        listbox_entrenadores.insert(tk.END, f"{nombre} {apellido} - {licencia} - {anios_exp} años")

        entry_nombre_entrenador.delete(0, tk.END)
        entry_apellido_entrenador.delete(0, tk.END)
        entry_fecha_naci_entrenador.delete(0, tk.END)
        entry_nacionalidad_entrenador.delete(0, tk.END)
        entry_licencia_entrenador.delete(0, tk.END)
        entry_anios_exp_entrenador.delete(0, tk.END)
        entry_sistema_juego_entrenador.delete(0, tk.END)

    tk.Button(frame, text="Registrar Entrenador", bg=FONDO_CARD, fg=TEXTO_BLANCO,
              activebackground="#1a3a5c", activeforeground=TEXTO_BLANCO,
              relief="flat", padx=20, pady=10, cursor="hand2",
              command=registrar_entrenador).pack(pady=10, fill="x", padx=40)

    tk.Label(frame, text="Entrenadores registrados:",
             bg=FONDO_OSCURO, fg=TEXTO_BLANCO, font=FUENTE_LABEL).pack()
    listbox_entrenadores = tk.Listbox(frame, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                                      font=FUENTE_BOTON, width=50, height=6)
    listbox_entrenadores.pack(pady=5)

    tk.Button(frame, text="🔙 Volver", bg=FONDO_CARD, fg=TEXTO_AZUL,
              activebackground="#1a3a5c", activeforeground=TEXTO_BLANCO,
              relief="flat", padx=20, pady=10, cursor="hand2",
              command=lambda: mostrar_admin_entrenadores_jugadores(
                  ventana, lista_entrenadores, lista_jugadores,
                  lista_selecciones, mostrar_menu)).pack(pady=10, fill="x", padx=40)

def mostrar_jugador(ventana, lista_entrenadores, lista_jugadores, lista_selecciones, mostrar_menu):
    """
    Muestra el formulario para registrar un jugador y el listado de selecciones registradas.
    #E: ventana (tk.Tk), lista_entrenadores (list), mostrar_menu (function), lista_jugadores (list), lista_seleccion(list)
    #S: No retorna nada, dibuja los widgets en la ventana
    #R: La ventana debe estar inicializada correctamente
    """
    limpiar_ventana(ventana)
    ventana.configure(bg=FONDO_OSCURO)

    canvas = tk.Canvas(ventana, bg=FONDO_OSCURO, highlightthickness=0)
    scrollbar = tk.Scrollbar(ventana, orient="vertical", command=canvas.yview)
    
    frame = tk.Frame(canvas, bg=FONDO_OSCURO)
    frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    
    canvas.create_window((300, 0), window=frame, anchor="n")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    
    scrollbar.pack(side="right", fill="y")

    tk.Label(frame, text="Registrar Jugador",
             font=FUENTE_TITULO, bg=FONDO_OSCURO, fg=DORADO).pack(pady=20)

    tk.Label(frame, text="Nombre:", bg=FONDO_OSCURO, fg=TEXTO_BLANCO, font=FUENTE_LABEL).pack()
    entry_nombre_jugador = tk.Entry(frame, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                                    insertbackground=TEXTO_BLANCO, font=FUENTE_BOTON)
    entry_nombre_jugador.pack()

    tk.Label(frame, text="Apellido:", bg=FONDO_OSCURO, fg=TEXTO_BLANCO, font=FUENTE_LABEL).pack()
    entry_apellido_jugador = tk.Entry(frame, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                                      insertbackground=TEXTO_BLANCO, font=FUENTE_BOTON)
    entry_apellido_jugador.pack()

    tk.Label(frame, text="Fecha nacimiento (DD/MM/AAAA):",
             bg=FONDO_OSCURO, fg=TEXTO_BLANCO, font=FUENTE_LABEL).pack()
    entry_fecha_naci_jugador = tk.Entry(frame, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                                        insertbackground=TEXTO_BLANCO, font=FUENTE_BOTON)
    entry_fecha_naci_jugador.pack()

    tk.Label(frame, text="Nacionalidad:", bg=FONDO_OSCURO, fg=TEXTO_BLANCO, font=FUENTE_LABEL).pack()
    entry_nacionalidad_jugador = tk.Entry(frame, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                                          insertbackground=TEXTO_BLANCO, font=FUENTE_BOTON)
    entry_nacionalidad_jugador.pack()

    tk.Label(frame, text="Dorsal (1-99):", bg=FONDO_OSCURO, fg=TEXTO_BLANCO, font=FUENTE_LABEL).pack()
    entry_dorsal_jugador = tk.Entry(frame, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                                    insertbackground=TEXTO_BLANCO, font=FUENTE_BOTON)
    entry_dorsal_jugador.pack()

    tk.Label(frame, text="Posicion:", bg=FONDO_OSCURO, fg=TEXTO_BLANCO, font=FUENTE_LABEL).pack()
    entry_posicion_jugador = tk.Entry(frame, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                                      insertbackground=TEXTO_BLANCO, font=FUENTE_BOTON)
    entry_posicion_jugador.pack()

    tk.Label(frame, text="Puntaje individual (1-100):",
             bg=FONDO_OSCURO, fg=TEXTO_BLANCO, font=FUENTE_LABEL).pack()
    entry_puntaje_jugador = tk.Entry(frame, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                                     insertbackground=TEXTO_BLANCO, font=FUENTE_BOTON)
    entry_puntaje_jugador.pack()

    tk.Label(frame, text="Selecciona una seleccion:",
             bg=FONDO_OSCURO, fg=TEXTO_BLANCO, font=FUENTE_LABEL).pack()
    listbox_seleccion = tk.Listbox(frame, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                                   font=FUENTE_BOTON, width=50, height=6)
    for seleccion in lista_selecciones:
        listbox_seleccion.insert(tk.END, seleccion.get_codigo_equipo())
    listbox_seleccion.pack(pady=5)

    def registrar_jugador():
        """
        Registra un jugador nuevo con sus atributos
        #E: No recibe parámetros, lee los valores de los campos Entry
        #S: No retorna nada, agrega el objeto Futbolista a lista_jugadores y actualiza el listbox
        #R: La ventana debe estar inicializada correctamente
        """
        nombre = entry_nombre_jugador.get()
        apellido = entry_apellido_jugador.get()
        fecha_nacimiento = entry_fecha_naci_jugador.get()
        nacionalidad = entry_nacionalidad_jugador.get()
        dorsal = entry_dorsal_jugador.get()
        posicion = entry_posicion_jugador.get()
        puntaje = entry_puntaje_jugador.get()
        seleccion = listbox_seleccion.curselection()

        if nombre == "" or apellido == "" or fecha_nacimiento == "" or nacionalidad == "" or dorsal == "" or posicion == "" or puntaje == "":
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        if not validar_fecha(fecha_nacimiento):
            messagebox.showerror("Error", "La fecha debe tener el formato DD/MM/AAAA")
            return
        if not dorsal.isdigit():
            messagebox.showerror("Error", "El dorsal debe ser un número entero positivo")
            return
        dorsal_num = int(dorsal)
        if dorsal_num < 1 or dorsal_num > 99:
            messagebox.showerror("Error", "El dorsal debe ser un número entre 1 y 99")
            return
        if not puntaje.isdigit():
            messagebox.showerror("Error", "El puntaje debe ser un número entero positivo")
            return
        puntaje_num = int(puntaje)
        if puntaje_num < 1 or puntaje_num > 100:
            messagebox.showerror("Error", "El puntaje debe ser un número entre 1 y 100")
            return

        nuevo_jugador = Futbolista(nombre, apellido, fecha_nacimiento, nacionalidad,
                                   dorsal_num, posicion, puntaje_num)
        if seleccion:
            seleccion_elegida = lista_selecciones[seleccion[0]]
            seleccion_elegida.agregar_jugador(nuevo_jugador)

        lista_jugadores.append(nuevo_jugador)
        guardar_jugadores(lista_jugadores)
        messagebox.showinfo("Éxito", f"Jugador {nombre} registrado correctamente")
        listbox_jugadores.insert(tk.END, f"#{dorsal} {nombre} {apellido} - {posicion}")

        entry_nombre_jugador.delete(0, tk.END)
        entry_apellido_jugador.delete(0, tk.END)
        entry_fecha_naci_jugador.delete(0, tk.END)
        entry_nacionalidad_jugador.delete(0, tk.END)
        entry_dorsal_jugador.delete(0, tk.END)
        entry_posicion_jugador.delete(0, tk.END)
        entry_puntaje_jugador.delete(0, tk.END)

    tk.Button(frame, text="Registrar Jugador", bg=FONDO_CARD, fg=TEXTO_BLANCO,
              activebackground="#1a3a5c", activeforeground=TEXTO_BLANCO,
              relief="flat", padx=20, pady=10, cursor="hand2",
              command=registrar_jugador).pack(pady=10, fill="x", padx=40)

    tk.Label(frame, text="Jugadores registrados:",
             bg=FONDO_OSCURO, fg=TEXTO_BLANCO, font=FUENTE_LABEL).pack()
    listbox_jugadores = tk.Listbox(frame, bg=FONDO_CARD, fg=TEXTO_BLANCO,
                               font=FUENTE_BOTON, width=50, height=6)
    for jugador in lista_jugadores:
        listbox_jugadores.insert(tk.END, f"#{jugador.get_dorsal()} {jugador.get_nombre()} {jugador.get_apellido()} - {jugador.get_posicion()}")
    listbox_jugadores.pack(pady=5)

    tk.Button(frame, text="🔙 Volver", bg=FONDO_CARD, fg=TEXTO_AZUL,
              activebackground="#1a3a5c", activeforeground=TEXTO_BLANCO,
              relief="flat", padx=20, pady=10, cursor="hand2",
              command=lambda: mostrar_admin_entrenadores_jugadores(
                  ventana, lista_entrenadores, lista_jugadores,
                  lista_selecciones, mostrar_menu)).pack(pady=10, fill="x", padx=40)
