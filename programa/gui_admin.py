import tkinter as tk
from tkinter import messagebox
from utilidades import centrar_ventana, limpiar_ventana
from pais import Pais
    
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
    
    btn_selecciones = tk.Button(ventana, text="Registrar Selección")
    btn_selecciones.pack(pady=10)
    
    btn_volver = tk.Button(ventana, text="Volver al Menú", command=mostrar_menu)
    btn_volver.pack(pady=10)
