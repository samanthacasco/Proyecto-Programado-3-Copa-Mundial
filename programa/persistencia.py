from pais import Pais
from seleccion import Seleccion
from persona import Persona
from futbolista import Futbolista
from partido import Partido

def guardar_paises(lista_paises):
    """
    Guarda la lista de países en el archivo paises.txt.
    #E: lista_paises (list)
    #S: No retorna nada, escribe los datos en el archivo paises.txt
    #R: lista_paises debe contener objetos Pais válidos
    """
    with open("paises.txt", "w", encoding="utf-8") as archivo:
        for pais in lista_paises:
            archivo.write(f"{pais.get_codigo_fifa()}|{pais.get_nombre()}|{pais.get_continente()}|{pais.get_ranking_fifa()}\n")

def cargar_paises():
    """
    Carga la lista de países del archivo paises.txt.
    #E: No recibe parametros
    #S: Retorna la lista con los paises
    #R: El archivo paises.txt debe existir y tener el formato correcto
    """
    paises = []
    try:
        with open("paises.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            
        for linea in lineas:
            datos = linea.strip().split("|")
            pais = Pais(datos[0], datos[1], datos[2], int(datos[3]))
            paises.append(pais)
            
    except FileNotFoundError:
        pass
    return paises
        
def guardar_selecciones(lista_selecciones):
    """
    Guarda la lista de selecciones en el archivo selecciones.txt.
    #E: lista_selecciones (list)
    #S: No retorna nada, escribe los datos en el archivo selecciones.txt
    #R: lista_selecciones debe contener objetos Seleccion válidos
    """
    with open("selecciones.txt", "w", encoding="utf-8") as archivo:
        for seleccion in lista_selecciones:
            archivo.write(f"{seleccion.get_codigo_equipo()}|{seleccion.get_pais().get_codigo_fifa()}|{seleccion.get_fuerza_equipo()}\n")

def cargar_selecciones(lista_paises):
    """
    Carga la lista de selecciones del archivo selecciones.txt.
    #E: lista_paises (list) 
    #S: Retorna la lista con las selecciones
    #R: El archivo selecciones.txt debe existir y tener el formato correcto
    """
    selecciones = []
    try:
        with open("selecciones.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            
        for linea in lineas:
            datos = linea.strip().split("|")
            
            pais_encontrado = None
            for pais in lista_paises:
                if pais.get_codigo_fifa() == datos[1]:
                    pais_encontrado = pais
            seleccion = Seleccion(datos[0], pais_encontrado, None)
            selecciones.append(seleccion)
            
    except FileNotFoundError:
        pass
    return selecciones

def guardar_jugadores(lista_jugadores):
    """
    Guarda la lista de jugadores en el archivo jugadores.txt.
    #E: lista_jugadores (list)
    #S: No retorna nada, escribe los datos en el archivo jugadores.txt
    #R: lista_jugadores debe contener objetos Futbolista válidos
    """
    with open("jugadores.txt", "w", encoding="utf-8") as archivo:
        for jugador in lista_jugadores:
            archivo.write(f"{jugador.get_nombre()}|{jugador.get_apellido()}|{jugador.get_fecha_nacimiento()}|{jugador.get_nacionalidad()}|{jugador.get_dorsal()}|{jugador.get_posicion()}|{jugador.get_puntaje_individual()}|{jugador.get_goles()}|{jugador.get_asistencias()}|{jugador.get_total_tarjetas_amarillas()}|{jugador.get_total_tarjetas_rojas()} \n")

def cargar_jugadores():
    """
    Carga la lista de jugadores del archivo jugadores.txt.  
    #E: No recibe parametros
    #S: Retorna la lista con los jugadores
    #R: El archivo jugadores.txt debe existir y tener el formato correcto
    """
    jugadores = []
    try:
        with open("jugadores.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            
        for linea in lineas:
            datos = linea.strip().split("|")
            jugador = Futbolista(datos[0], datos[1], datos[2], datos[3], int(datos[4]), datos[5], int(datos[6]))
            jugadores.append(jugador)
            
    except FileNotFoundError:
        pass
    return jugadores

def guardar_partidos(lista_partidos):
    """
    Guarda la lista de partidos en el archivo partidos.txt.
    #E: lista_partidos (list)
    #S: No retorna nada, escribe los datos en el archivo partidos.txt
    #R: lista_partidos debe contener objetos Partido válidos
    """
    with open("partidos.txt", "w", encoding="utf-8") as archivo:
        for partido in lista_partidos:
            archivo.write(f"{partido.get_id_partido()}|{partido.get_equipo_1().get_pais().get_nombre()}|{partido.get_equipo_2().get_pais().get_nombre()}|{partido.get_goles_equipo1()}|{partido.get_goles_equipo2()}|{partido.get_fase()}|{partido.get_fecha()}\n")

def cargar_partidos():
    """
    Carga la lista de partidos del archivo partidos.txt.
    #E: No recibe parametros
    #S: Retorna la lista con los partidos
    #R: El archivo partidos.txt debe existir y tener el formato correcto
    """
    partidos = []
    try:
        with open("partidos.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
        for linea in lineas:
            datos = linea.strip().split("|")
            partidos.append(datos)  
    except FileNotFoundError:
        pass
    return partidos
