from partido import Partido 
import random

class Fase:
    def __init__(self, nombre_fase):
        """
        Constructor que inicializa los atributos de la clase Fase
        #E: nombre_fase (str)
        #S: No retorna nada
        #R: El nombre de la fase debe ser un str no vacío
        """
        self.__nombre_fase = nombre_fase
        self.__partidos = [ ]
        self.__clasificados = [ ]
        self.__resultados_penales = [ ]
        self.__eliminados = [ ]

    def registrar_juego(self, equipo1, equipo2):
        """
        Registra un partido en la fase.
        #E: equipo1 (Seleccion), equipo2 (Seleccion)
        #S: No retorna nada, agrega un partido a la fase
        #R: Los equipos deben ser objetos Seleccion válidos
        """

        id_partido = len(self.__partidos) + 1
        partido = Partido(id_partido, equipo1, equipo2, self.__nombre_fase, "DD/MM/AAAA")
        self.__partidos.append(partido)

    def jugar_fase(self):
        """
        Simula todos los partidos de la fase eliminatoria.
        #E: No recibe parámetros
        #S: No retorna nada, guarda en __clasificados las selecciones ganadoras
        #R: Los partidos deben estar registrados previamente en la fase
        """
        self.__clasificados = []
        self.__eliminados = []
        self.__resultados_penales = []
        
        for partido in self.__partidos:
            partido.simular()

            ganador = partido.generar_ganador()

            # Si no hay ganador
            if ganador is None:
                penales_equipo1 = random.randint(2, 5)
                penales_equipo2 = random.randint(2, 5)
                while penales_equipo1 == penales_equipo2:
                    penales_equipo1 = random.randint(2, 5)
                    penales_equipo2 = random.randint(2, 5)
                    
                # Si gana equipo 1
                if penales_equipo1 > penales_equipo2:
                    self.__clasificados.append(partido.get_equipo_1())
                    self.__eliminados.append(partido.get_equipo_2())
                else:
                    self.__clasificados.append(partido.get_equipo_2())
                    self.__eliminados.append(partido.get_equipo_1())
                self.__resultados_penales.append([partido, penales_equipo1, penales_equipo2])
            else:
                self.__clasificados.append(ganador)
                if ganador == partido.get_equipo_1():
                    self.__eliminados.append(partido.get_equipo_2())
                else:
                    self.__eliminados.append(partido.get_equipo_1())

    def obtener_clasificados(self):
        """
        Obtiene las selecciones clasificadas a la siguiente fase.
        #E: No recibe parámetros
        #S: Retorna una lista con las selecciones ganadoras de la fase
        #R: La fase debe haberse jugado previamente
        """
        return self.__clasificados


    def mostrar_juegos(self):
        """
        Muestra los resultados de todos los partidos de la fase.
        #E: No recibe parámetros
        #S: Retorna un str con los resultados de los partidos de la fase
        #R: Los partidos deben haber sido registrados previamente
        """
        resultado = self.__nombre_fase + "\n\n"  

        for partido in self.__partidos:
            tuvo_penales = False

            for penal in self.__resultados_penales:
                if penal[0] == partido:
                    penal_equipo1 = penal[1]
                    penal_equipo2 = penal[2]

                    juego = f"{partido.mostrar_resultado()} (Penales: {penal_equipo1}-{penal_equipo2})"
                    resultado += juego + "\n"
                    tuvo_penales = True

            # Si no tuvo penales, se guarda resultado normal
            if tuvo_penales == False:
                juego = partido.mostrar_resultado()
                resultado += juego + "\n"
        return resultado

    def get_nombre_fase(self):
        """
        Retorna el nombre de la fase.
        #E: No recibe parámetros
        #S: Retorna un str con el nombre de la fase
        #R: El atributo __nombre_fase debe estar inicializado
        """
        return self.__nombre_fase
    
    def get_partidos(self):
        """
        Retorna la lista de partidos de la fase.
        #E: No recibe parámetros
        #S: Retorna una lista de objetos Partido
        #R: El atributo __partidos debe estar inicializado
        """
        return self.__partidos
    
    def get_clasificados(self):
        """
        Retorna las selecciones clasificadas de la fase.
        #E: No recibe parámetros
        #S: Retorna una lista de objetos Seleccion
        #R: La fase debe haberse jugado previamente para contener clasificados
        """
        return self.__clasificados
    
    def get_penales(self):
        """
        Retorna los resultados de las tandas de penales de la fase.
        #E: No recibe parámetros
        #S: Retorna una lista con los partidos que se definieron por penales y sus resultados
        #R: La fase debe haberse jugado previamente para contener resultados de penales
        """
        return self.__resultados_penales
    
    def get_eliminados(self):
        """
        Retorna las selecciones eliminadas de la fase.
        #E: No recibe parámetros
        #S: Retorna una lista con las selecciones eliminadas
        #R: La fase debe haberse jugado previamente para contener eliminados
        """
        return self.__eliminados
    

        