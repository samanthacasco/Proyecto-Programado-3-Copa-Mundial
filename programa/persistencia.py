from pais import Pais
from seleccion import Seleccion
from persona import Persona
from futbolista import Futbolista
from partido import Partido
from entrenador import Entrenador

def guardar_paises(lista_paises):
    """
    Guarda la lista de países en el archivo paises.txt.
    #E: lista_paises (list)
    #S: No retorna nada, escribe los datos en el archivo paises.txt
    #R: lista_paises debe contener objetos Pais válidos
    """
    if len(lista_paises) == 0: 
        return
    
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

def guardar_jugadores(lista_selecciones):
    """
    Guarda los jugadores en jugadores.txt con su selección asociada.
    #E: lista_jugadores (list), lista_selecciones (list)
    #S: No retorna nada, escribe los datos en jugadores.txt
    #R: lista_selecciones debe contener objetos Seleccion válidos con jugadores asignados
    """
    with open("jugadores.txt", "w", encoding="utf-8") as archivo:
        for seleccion in lista_selecciones:
            for jugador in seleccion.get_jugadores():
                archivo.write(f"{jugador.get_nombre()}|{jugador.get_apellido()}|{jugador.get_fecha_nacimiento()}|{jugador.get_nacionalidad()}|{jugador.get_dorsal()}|{jugador.get_posicion()}|{jugador.get_puntaje_individual()}|{jugador.get_goles()}|{jugador.get_asistencias()}|{jugador.get_total_tarjetas_amarillas()}|{jugador.get_total_tarjetas_rojas()}|{seleccion.get_codigo_equipo()}\n")
                
def cargar_jugadores(lista_selecciones):
    """
    Carga los jugadores y los re-asigna a sus selecciones.
    #E: lista_selecciones (list)
    #S: No retorna nada, asigna jugadores directamente a cada selección
    #R: El archivo jugadores.txt debe existir y tener el formato correcto
    """
    jugadores = []
    try:
        with open("jugadores.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
        for linea in lineas:
            datos = linea.strip().split("|")
            jugador = Futbolista(datos[0], datos[1], datos[2], datos[3], int(datos[4]), datos[5], int(datos[6]))
            codigo_seleccion = datos[11]
            for seleccion in lista_selecciones:
                if seleccion.get_codigo_equipo() == codigo_seleccion:
                    seleccion.agregar_jugador(jugador)
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

def guardar_ranking_goleadores(lista_jugadores):
    """
    Guarda el ranking de goleadores ordenado de mayor a menor en ranking_goleadores.txt
    #E: lista_jugadores (list)
    #S: No retorna nada, escribe el ranking en el archivo ranking_goleadores.txt
    #R: lista_jugadores debe contener objetos Futbolista válidos
    """
    copia = lista_jugadores[:]
    for i in range(len(copia)):
        for j in range(len(copia) - 1):
            actual = j
            siguiente = j+1
            if copia[actual].get_goles() < copia[siguiente].get_goles():
                copia[actual], copia[siguiente] = copia[siguiente], copia[actual]
    
    with open("ranking_goleadores.txt", "w", encoding="utf-8") as archivo:
        for jugador in copia:
            archivo.write(f"{jugador.get_nombre()}|{jugador.get_apellido()}|{jugador.get_goles()}\n")
            
def guardar_ranking_selecciones(mundial):
    """
    Guarda el ranking de selecciones ordenado por puntos en ranking_selecciones.txt
    #E: mundial (Mundial)
    #S: No retorna nada, escribe el ranking en el archivo ranking_selecciones.txt
    #R: El mundial debe tener grupos con partidos simulados
    """
    datos_selecciones = []
    
    for grupo in mundial.get_grupos():
        tabla = grupo.calcular_tabla()
        for fila in tabla:
            seleccion = fila[0]
            puntos = fila[1]
            goles_favor = fila[2]
            goles_contra = fila[3]
            datos_selecciones.append([seleccion, puntos, goles_favor, goles_contra])
    
    # ordenar por puntos de mayor a menor
    for i in range(len(datos_selecciones)):
        for j in range(len(datos_selecciones) - 1):
            equipo_actual = j
            equipo_siguiente = j+1 
            pos_puntos = 1
            if datos_selecciones[equipo_actual][pos_puntos] < datos_selecciones[equipo_siguiente][pos_puntos]:
                datos_selecciones[equipo_actual], datos_selecciones[equipo_siguiente] = datos_selecciones[equipo_siguiente], datos_selecciones[equipo_actual]
    
    with open("ranking_selecciones.txt", "w", encoding="utf-8") as archivo:
        for dato in datos_selecciones:
            nombre = dato[0].get_pais().get_nombre()
            archivo.write(f"{nombre}|{dato[1]}|{dato[2]}|{dato[3]}\n")

def guardar_entrenadores(lista_selecciones):
    """
    Guarda los entrenadores asociados a cada selección en entrenadores.txt
    #E: lista_selecciones (list)
    #S: No retorna nada, escribe los datos en entrenadores.txt
    #R: lista_selecciones debe contener objetos Seleccion válidos
    """
    with open("entrenadores.txt", "w", encoding="utf-8") as archivo:
        for seleccion in lista_selecciones:
            if seleccion.get_entrenador() is not None:
                e = seleccion.get_entrenador()
                archivo.write(f"{e.get_nombre()}|{e.get_apellido()}|{e.get_fecha_nacimiento()}|{e.get_nacionalidad()}|{e.get_licencia()}|{e.get_experiencia_anios()}|{e.get_sistema_juego()}|{seleccion.get_codigo_equipo()}\n")

def cargar_entrenadores(lista_selecciones):
    """
    Carga los entrenadores y los re-asigna a sus selecciones.
    #E: lista_selecciones (list)
    #S: No retorna nada, asigna entrenadores directamente a cada selección
    #R: El archivo entrenadores.txt debe existir y tener el formato correcto
    """
    entrenadores = []
    try:
        with open("entrenadores.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
        for linea in lineas:
            datos = linea.strip().split("|")
            entrenador = Entrenador(datos[0], datos[1], datos[2], datos[3], datos[4], int(datos[5]), datos[6])
            entrenadores.append(entrenador)  
            codigo_seleccion = datos[7]
            for seleccion in lista_selecciones:
                if seleccion.get_codigo_equipo() == codigo_seleccion:
                    seleccion.asignar_entrenador(entrenador)
    except FileNotFoundError:
        pass
    return entrenadores
