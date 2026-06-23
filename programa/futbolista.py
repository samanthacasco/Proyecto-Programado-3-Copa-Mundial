from persona import Persona

class Futbolista(Persona):
    def __init__(self,  nombre, apellido, fecha_nacimiento, nacionalidad, dorsal, posicion, puntaje_individual):
        """
        Constructor que inicializa los atributos de la clase Futbolista.
        #E: nombre (str), apellido (str), fecha_nacimiento (str), nacionalidad (str), dorsal (int), posicion (str), puntaje_individual (int)
        #S: No retorna nada
        #R: Todos los parámetros deben ser str no vacíos
        """
        super().__init__(nombre, apellido, fecha_nacimiento, nacionalidad)

        self.__dorsal = dorsal
        self.__posicion = posicion
        self.__puntaje_individual = puntaje_individual
        self.__goles = 0
        self.__asistencias = 0
        self.__total_tarjetas_amarillas = 0
        self.__total_tarjetas_rojas = 0
    
    def mostrar_datos(self):
        """
        Muestra la información básica del futbolista.
        #E: No recibe parámetros
        #S: Retorna un str con la información del futbolista
        #R: El objeto debe estar correctamente inicializado
        """
        datos_persona = super().mostrar_datos()
        estadisticas = f"Goles: {self.__goles}, Asistencias: {self.__asistencias}, Total tarjetas amarillas: {self.__total_tarjetas_amarillas}, Total tarjetas rojas: {self.__total_tarjetas_rojas}"
        
        return f"{datos_persona}\nDorsal: {self.__dorsal}, Posicion:{self.__posicion}\n {estadisticas}\nPuntaje Individual: {self.__puntaje_individual}"
    
    def actualizar_datos(self, dorsal, posicion, puntaje_individual):
        """
        Actualiza los atributos del futbolista.
        #E: dorsal (int), posicion (str), puntaje_individual (int)
        #S: No retorna nada, actualiza los atributos del futbolista
        #R: El objeto debe estar correctamente inicializado
        """
        self.__dorsal = dorsal
        self.__posicion = posicion
        self.__puntaje_individual = puntaje_individual
    
    def registrar_gol(self):
        """
        Incrementa el contador de goles anotados.
        #E: No recibe parámetros
        #S:  Suma 1 al contador de goles del jugador
        #R: El objeto debe estar correctamente inicializado  
        """
        self.__goles += 1
    
    def registrar_asistencia(self):
        """
        Incrementa el contador de asistencias.
        #E: No recibe parámetros
        #S: Suma 1 al contador de asistencias del jugador
        #R: El objeto debe estar correctamente inicializado 
        """
        self.__asistencias += 1
    
    def registrar_tarjeta(self, tipo):
        """
        Incrementa el contador de tarjetas amarillas o rojas segun el tipo.
        #E: tipo (str)        
        #S: Suma 1 al contador de tarjetas amarillas o rojas según el tipo  
        #R: El objeto debe estar correctamente inicializado 
        """
        if tipo == "amarilla":
            self.__total_tarjetas_amarillas += 1
        else:
            self.__total_tarjetas_rojas += 1
    
    def get_dorsal(self):
        """
        Retorna el dorsal del futbolista.
        #E: No recibe parámetros
        #S: Retorna un int con dorsal del futbolista 
        #R: El atributo __dorsal debe estar inicializado
        """
        return self.__dorsal
    
    def get_posicion(self):
        """
        Retorna la posicion del futbolista.
        #E: No recibe parámetros
        #S: Retorna un str con la posicion del futbolista 
        #R: El atributo __posicion debe estar inicializado
        """
        return self.__posicion
    
    def get_puntaje_individual(self):
        """
        Retorna el puntaje del futbolista.
        #E: No recibe parámetros
        #S: Retorna un int con puntaje
        #R: El atributo __puntaje_individual debe estar inicializado
        """
        return self.__puntaje_individual
    
    def get_goles(self):
        """
        Retorna la cantidad de goles del futbolista.
        #E: No recibe parámetros
        #S: Retorna un int con la cantidad de goles
        #R: El atributo __goles debe estar inicializado
        """
        return self.__goles
  
    def get_asistencias(self):
        """
        Retorna la cantidad de asistencias del futbolista.
        #E: No recibe parámetros
        #S: Retorna un int la cantidad de asistencias
        #R: El atributo __asistencias debe estar inicializado
        """
        return self.__asistencias
    
    def get_total_tarjetas_amarillas(self):
        """
        Retorna el total de tarjetas amarillas.
        #E: No recibe parámetros
        #S: Retorna un int con el total de tarjetas amarillas
        #R: El atributo __total_tarjetas_amarillas debe estar inicializado
        """
        return self.__total_tarjetas_amarillas
    
    def get_total_tarjetas_rojas(self):
        """
        Retorna el total de tarjetas rojas.
        #E: No recibe parámetros
        #S: Retorna un int con el total de tarjetas rojas
        #R: El atributo __total_tarjetas_rojas debe estar inicializado
        """
        return self.__total_tarjetas_rojas
