import tkinter as tk

def centrar_ventana(ventana, ancho, alto):
    """
    Centra una ventana de tkinter en la pantalla del usuario, independientemente del tamaño del monitor. Calcula la 
            posición usando las dimensiones de la pantalla.
    #E: ventana (tk.Tk): la ventana de tkinter a centrar.
        ancho (int): ancho deseado de la ventana en pixeles.
        alto (int): alto deseado de la ventana en pixeles. 
    #S: Ninguna. Modifica la geometría de la ventana (tamaño y posición).
    #R: ventana debe ser una instancia válida de tk.Tk o Toplevel.
                   ancho y alto deben ser enteros positivos.
    """
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    
    pos_x = (ancho_pantalla - ancho) // 2
    pos_y = (alto_pantalla - alto) // 2
    
    ventana.geometry(f"{ancho}x{alto}+{pos_x}+{pos_y}")
    
def limpiar_ventana(ventana):
    """Elimina todos los widgets que haya en la ventana recibida.
    #E: Recibe la ventana a limpiar.
    #S: No devuelve nada; se usa para borrar la pantalla anterior antes de dibujar otra.
    #R: La ventana debe ser una instancia válida de tk.Tk
    """
    for widget in ventana.winfo_children():
        widget.destroy()  
        
def validar_fecha(fecha):
    """Valida el formato de la fecha de nacimiento.
    #E: Recibe la fecha ingresada.
    #S: Retorna True si la fecha tiene el formato correcto, en caso contrario retorna False
    #R: La fecha debe ser un str en formato DD/MM/AAAA
    """
    if len(fecha) != 10:
        return False
    
    if fecha[2] != "/" or fecha[5] != "/":
        return False
    
    dia = fecha[0:2]
    mes = fecha[3:5]
    anio = fecha[6:10]
    
    if not dia.isdigit() or not mes.isdigit() or not anio.isdigit():
        return False
    
    dia_num = int(dia)
    mes_num = int(mes)
    
    if dia_num < 1 or dia_num > 31:
        return False
    if mes_num < 1 or mes_num > 12:
        return False
    
    return True
