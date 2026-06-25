import tkinter as tk
from tkinter import messagebox
from utilidades import centrar_ventana, limpiar_ventana
from pais import Pais
from seleccion import Seleccion
from entrenador import Entrenador
from futbolista import Futbolista
 
def mostrar_paises(ventana, lista_paises, mostrar_menu, lista_selecciones):
    """
    Muestra el formulario para registrar países y el listado de países registrados.
    #E: ventana (tk.Tk), lista_paises (list), mostrar_menu (function)
    #S: No retorna nada, dibuja los widgets en la ventana
    #R: La ventana debe estar inicializada correctamente
    """
    limpiar_ventana(ventana)
    
    tk.Label(ventana, text="Registrar País", font=("Arial", 16)).pack(pady=10)
    
    tk.Label(ventana, text="Código FIFA:").pack()
    entry_codigo = tk.Entry(ventana)
    entry_codigo.pack()
    
    tk.Label(ventana, text="Nombre:").pack()
    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack()
    
    tk.Label(ventana, text="Continente:").pack()
    entry_continente = tk.Entry(ventana)
    entry_continente.pack()
   
    tk.Label(ventana, text="Ranking FIFA:").pack()
    entry_ranking = tk.Entry(ventana)
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
        messagebox.showinfo("Éxito", f"País {nombre} registrado correctamente")
        listbox_paises.insert(tk.END, f"{codigo} - {nombre} - {continente} - Ranking: {ranking}")

        entry_codigo.delete(0, tk.END)
        entry_nombre.delete(0, tk.END)
        entry_continente.delete(0, tk.END)
        entry_ranking.delete(0, tk.END)
       
    btn_registrar = tk.Button(ventana, text="Registrar País", command=registrar_pais)
    btn_registrar.pack(pady=10)
    
    tk.Label(ventana, text="Países registrados:").pack()
    listbox_paises = tk.Listbox(ventana, width=50, height=8)
    listbox_paises.pack(pady=5)
    
    btn_volver = tk.Button(ventana, text="Volver", 
                       command=lambda: mostrar_admin_paises_selecciones(ventana, lista_paises, lista_selecciones, mostrar_menu))
    btn_volver.pack(pady=10)

def mostrar_admin_paises_selecciones(ventana, lista_paises, lista_selecciones, mostrar_menu):
    """
    Muestra el submenú de administración de países y selecciones.
    #E: ventana (tk.Tk), lista_paises (list), lista_selecciones (list), mostrar_menu (function)
    #S: No retorna nada, dibuja los widgets en la ventana
    #R: La ventana debe estar inicializada correctamente
    """
    limpiar_ventana(ventana)
    
    tk.Label(ventana, text="Administrar Países y Selecciones", font=("Arial", 16)).pack(pady=20)
    
    btn_paises = tk.Button(ventana, text="Registrar País",
                           command=lambda: mostrar_paises(ventana, lista_paises, mostrar_menu, lista_selecciones))
    btn_paises.pack(pady=10)
    
    btn_selecciones = tk.Button(ventana, text="Registrar Selección",
        command=lambda: mostrar_selecciones(ventana, lista_paises, lista_selecciones, mostrar_menu))    
    btn_selecciones.pack(pady=10)
        
    btn_volver = tk.Button(ventana, text="Volver al Menú", command=mostrar_menu)
    btn_volver.pack(pady=10)
   
    
def mostrar_selecciones(ventana, lista_paises, lista_selecciones, mostrar_menu):
    """
    Muestra el formulario para registrar una seleccion y el listado de países y selecciones registradas.
    #E: ventana (tk.Tk), lista_paises (list), mostrar_menu (function), lista_selecciones (list)
    #S: No retorna nada, dibuja los widgets en la ventana
    #R: La ventana debe estar inicializada correctamente
    """
    limpiar_ventana(ventana)
    
    tk.Label(ventana, text="Registrar Seleccion", font=("Arial", 16)).pack(pady=20) 
    
    tk.Label(ventana, text="Código del equipo:").pack()
    entry_codigo_equipo = tk.Entry(ventana)
    entry_codigo_equipo.pack()

    tk.Label(ventana, text="Selecciona un pais:").pack()
    
    listbox_paises = tk.Listbox(ventana, width=50, height=6)
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
        
        listbox_seleccion.insert(tk.END, f"{codigo} - {pais_elegido.get_nombre()}")
        messagebox.showinfo("Éxito", f"Selección {codigo} registrada correctamente")
        
        entry_codigo_equipo.delete(0, tk.END)
        
    btn_registrar_selec = tk.Button(ventana, text="Registrar Selección",
                                    command=registrar_seleccion)    
    btn_registrar_selec.pack(pady=10)

    tk.Label(ventana, text="Selecciones registradas:").pack()
    
    listbox_seleccion = tk.Listbox(ventana, width=50, height=6)
    for seleccion in lista_selecciones:       
        listbox_seleccion.insert(tk.END, seleccion.get_codigo_equipo())
    listbox_seleccion.pack(pady=5)
    
    btn_volver = tk.Button(ventana, text="Volver", 
                       command=lambda: mostrar_admin_paises_selecciones(ventana, lista_paises, lista_selecciones, mostrar_menu))
    btn_volver.pack(pady=10)

def mostrar_admin_entrenadores_jugadores(ventana, lista_entrenadores, lista_jugadores, lista_selecciones, mostrar_menu):
    """
    Muestra el submenú de administración de entrenadores y jugadores.
    #E: ventana (tk.Tk), lista_entrenadores (list), lista_jugadores (list), mostrar_menu (function)
    #S: No retorna nada, dibuja los widgets en la ventana
    #R: La ventana debe estar inicializada correctamente
    """
    limpiar_ventana(ventana)
    
    tk.Label(ventana, text="Administrar Entrenadores y Jugadores", font=("Arial", 16)).pack(pady=20)
    
    btn_entrenador = tk.Button(ventana, text="Registrar Entrenador",
                           command=lambda: mostrar_entrenador(ventana, lista_entrenadores, lista_jugadores, lista_selecciones,  mostrar_menu))
    btn_entrenador.pack(pady=10)
    
    btn_jugador = tk.Button(ventana, text="Registrar Jugador",
        command=lambda: mostrar_jugador(ventana, lista_entrenadores, lista_jugadores, lista_selecciones, mostrar_menu))    
    btn_jugador.pack(pady=10)
        
    btn_volver = tk.Button(ventana, text="Volver al Menú", command=mostrar_menu)
    btn_volver.pack(pady=10)

def mostrar_entrenador(ventana, lista_entrenadores, lista_jugadores, lista_selecciones, mostrar_menu):
    """
    Muestra el formulario para registrar un entrenador y el listado de selecciones registradas.
    #E: ventana (tk.Tk), lista_entrenadores (list), mostrar_menu (function), lista_jugadores (list)
    #S: No retorna nada, dibuja los widgets en la ventana
    #R: La ventana debe estar inicializada correctamente
    """
    limpiar_ventana(ventana)
    
    tk.Label(ventana, text="Registrar Entrenador", font=("Arial", 16)).pack(pady=20) 
    
    tk.Label(ventana, text="Nombre:").pack()
    entry_nombre_entrenador = tk.Entry(ventana)
    entry_nombre_entrenador.pack()
    
    tk.Label(ventana, text="Apellido:").pack()
    entry_apellido_entrenador = tk.Entry(ventana)
    entry_apellido_entrenador.pack()
    
    tk.Label(ventana, text="Fecha nacimiento:").pack()
    entry_fecha_naci_entrenador = tk.Entry(ventana)
    entry_fecha_naci_entrenador.pack()
    
    tk.Label(ventana, text="Nacionalidad:").pack()
    entry_nacionalidad_entrenador = tk.Entry(ventana)
    entry_nacionalidad_entrenador.pack()
    
    tk.Label(ventana, text="Licencia:").pack()
    entry_licencia_entrenador = tk.Entry(ventana)
    entry_licencia_entrenador.pack()
    
    tk.Label(ventana, text="Años de experiencia:").pack()
    entry_anios_exp_entrenador = tk.Entry(ventana)
    entry_anios_exp_entrenador.pack()
    
    tk.Label(ventana, text="Sistema de juego:").pack()
    entry_sistema_juego_entrenador = tk.Entry(ventana)
    entry_sistema_juego_entrenador.pack()


    tk.Label(ventana, text="Selecciona una seleccion:").pack()
    
    listbox_seleccion = tk.Listbox(ventana, width=50, height=6)
    
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
        
        if not anios_exp.isdigit():
            messagebox.showerror("Error", "Los años de experiencia debe ser un número entero positivo")
            return
        
        nuevo_entrenador = Entrenador(nombre, apellido, fecha_nacimiento, nacionalidad, licencia, int(anios_exp), sistema_juego)
        if seleccion:
            seleccion_elegida = lista_selecciones[seleccion[0]]
            seleccion_elegida.asignar_entrenador(nuevo_entrenador)
            
        lista_entrenadores.append(nuevo_entrenador)
        messagebox.showinfo("Éxito", f"Entrenador {nombre} registrado correctamente")
        listbox_entrenadores.insert(tk.END, f"{nombre} - {apellido} - {fecha_nacimiento} - Nacionalidad: {nacionalidad} - Licencia: {licencia} - Años de experiencia: {anios_exp} - Sistema de juego: {sistema_juego}")

        entry_nombre_entrenador.delete(0, tk.END)
        entry_apellido_entrenador.delete(0, tk.END)
        entry_fecha_naci_entrenador.delete(0, tk.END)
        entry_nacionalidad_entrenador.delete(0, tk.END)
        entry_licencia_entrenador.delete(0, tk.END)
        entry_anios_exp_entrenador.delete(0, tk.END)
        entry_sistema_juego_entrenador.delete(0, tk.END)
    
    btn_registrar = tk.Button(ventana, text="Registrar Entrenador", command=registrar_entrenador)
    btn_registrar.pack(pady=10)
    
    tk.Label(ventana, text="Entrenadores registrados:").pack()
    listbox_entrenadores = tk.Listbox(ventana, width=50, height=8)
    listbox_entrenadores.pack(pady=5)
    
    btn_volver = tk.Button(ventana, text="Volver", 
                       command=lambda: mostrar_admin_entrenadores_jugadores(ventana, lista_entrenadores, lista_jugadores, lista_selecciones, mostrar_menu))
    btn_volver.pack(pady=10)
        
def mostrar_jugador(ventana, lista_entrenadores, lista_jugadores, lista_selecciones, mostrar_menu):
    """
    Muestra el formulario para registrar un jugador y el listado de selecciones registradas.
    #E: ventana (tk.Tk), lista_entrenadores (list), mostrar_menu (function), lista_jugadores (list), lista_seleccion(list)
    #S: No retorna nada, dibuja los widgets en la ventana
    #R: La ventana debe estar inicializada correctamente
    """
    limpiar_ventana(ventana)
    
    tk.Label(ventana, text="Registrar Jugador", font=("Arial", 16)).pack(pady=20) 
    
    tk.Label(ventana, text="Nombre:").pack()
    entry_nombre_jugador = tk.Entry(ventana)
    entry_nombre_jugador.pack()
    
    tk.Label(ventana, text="Apellido:").pack()
    entry_apellido_jugador = tk.Entry(ventana)
    entry_apellido_jugador.pack()
    
    tk.Label(ventana, text="Fecha nacimiento:").pack()
    entry_fecha_naci_jugador = tk.Entry(ventana)
    entry_fecha_naci_jugador.pack()
    
    tk.Label(ventana, text="Nacionalidad:").pack()
    entry_nacionalidad_jugador = tk.Entry(ventana)
    entry_nacionalidad_jugador.pack()
    
    tk.Label(ventana, text="Dorsal:").pack()
    entry_dorsal_jugador = tk.Entry(ventana)
    entry_dorsal_jugador.pack()
    
    tk.Label(ventana, text="Posicion:").pack()
    entry_posicion_jugador = tk.Entry(ventana)
    entry_posicion_jugador.pack()
    
    tk.Label(ventana, text="Puntaje individual:").pack()
    entry_puntaje_jugador = tk.Entry(ventana)
    entry_puntaje_jugador.pack()


    tk.Label(ventana, text="Selecciona una seleccion:").pack()
    
    listbox_seleccion = tk.Listbox(ventana, width=50, height=6)
    
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
        
        nuevo_jugador = Futbolista(nombre, apellido, fecha_nacimiento, nacionalidad, dorsal_num, posicion, puntaje_num)
        if seleccion:
            seleccion_elegida = lista_selecciones[seleccion[0]]
            seleccion_elegida.agregar_jugador(nuevo_jugador)
            
        lista_jugadores.append(nuevo_jugador)
        messagebox.showinfo("Éxito", f"Jugador {nombre} registrado correctamente")
        listbox_jugadores.insert(tk.END, f"{nombre} - {apellido} - {fecha_nacimiento} - Nacionalidad: {nacionalidad} - Dorsal: {dorsal} - Posicion: {posicion} - Puntaje Individual: {puntaje}")

        entry_nombre_jugador.delete(0, tk.END)
        entry_apellido_jugador.delete(0, tk.END)
        entry_fecha_naci_jugador.delete(0, tk.END)
        entry_nacionalidad_jugador.delete(0, tk.END)
        entry_dorsal_jugador.delete(0, tk.END)
        entry_posicion_jugador.delete(0, tk.END)
        entry_puntaje_jugador.delete(0, tk.END)
    
    btn_registrar = tk.Button(ventana, text="Registrar Jugador", command=registrar_jugador)
    btn_registrar.pack(pady=10)
    
    tk.Label(ventana, text="Jugadores registrados:").pack()
    listbox_jugadores = tk.Listbox(ventana, width=50, height=8)
    listbox_jugadores.pack(pady=5)
    
    btn_volver = tk.Button(ventana, text="Volver", 
                       command=lambda: mostrar_admin_entrenadores_jugadores(ventana, lista_entrenadores, lista_jugadores, lista_selecciones, mostrar_menu))
    btn_volver.pack(pady=10)
