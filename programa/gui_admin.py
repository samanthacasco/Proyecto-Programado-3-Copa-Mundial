import tkinter as tk
from tkinter import messagebox
from utilidades import centrar_ventana, limpiar_ventana
from pais import Pais
from seleccion import Seleccion
    
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
