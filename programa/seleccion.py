from futbolista import Futbolista
from entrenador import Entrenador
from pais import Pais

class Seleccion:
    def __init__(self, codigo_equipo, pais, entrenador):
        """
        Constructor que inicializa los atributos de la clase Seleccion.
        #E: codigo_equipo (str), pais (Pais), entrenador (Entrenador)
        #S: No retorna nada
        #R: Todos los parámetros deben ser str o int, no vacíos
        """
        self.__codigo_equipo = codigo_equipo
        self.__pais = pais         
        self.__entrenador = entrenador  
        self.__jugadores = []
        self.__total_goles_favor = 0
        self.__total_goles_contra = 0
        self.__total_tarjetas_amarillas = 0
        self.__total_tarjetas_rojas = 0
        self.__fuerza_equipo = 0
        self.__fase_alcanzada = "Fase de grupos"
    
    def mostrar_datos(self):
        """
        Muestra la información de la selección, incluyendo país, entrenador y plantilla
        #E: No recibe parámetros
        #S: Retorna un str con la información de la selección
        #R: El objeto debe estar correctamente inicializado
        """
        info_pais = self.__pais.mostrar_datos()
        if self.__entrenador is not None:
            info_entrenador = self.__entrenador.mostrar_datos()
        else:
            info_entrenador = "Sin entrenador asignado"
            
        info_jugadores = ""
        
        for jugador in self.__jugadores:
            info_jugadores += f"\n  {jugador.mostrar_datos()}"
        
        return f"Código equipo: {self.__codigo_equipo}\n{info_pais}\n{info_entrenador}\nJugadores:{info_jugadores}"
    
    def agregar_jugador(self, futbolista):
        """
        Agrega un futbolista a la lista de jugadores
        #E: futbolista (Futbolista)
        #S: Retorna True si se guarda el jugador o false en caso contrario
        #R: El objeto debe estar correctamente inicializado
        """
        cantidad = len(self.__jugadores)
        if cantidad >= 23:
            return False
        else:
            self.__jugadores.append(futbolista)
            return True
        
    def eliminar_jugador(self, dorsal):
        """
        Elimina un futbolista a la lista segun su dorsal
        #E: dorsal (int)
        #S: Retorna True si se elimina el jugador o false en caso contrario
        #R: El objeto debe estar correctamente inicializado
        """
        for jugador in self.__jugadores:
            if jugador.get_dorsal() == dorsal:
                self.__jugadores.remove(jugador)
                return True
        return False
    
    def asignar_entrenador(self, entrenador):
        """
        Asigna o reemplaza el entrenador de la selección
        #E: entrenador (Entrenador)
        #S: No retorna nada, actualiza el atributo __entrenador
        #R: El objeto debe estar correctamente inicializado
        """
        self.__entrenador = entrenador
    
    def registrar_resultado(self, goles_favor, goles_contra, tarjetas_am, tarjetas_roj):
        """
        Actualiza los totales del equipo tras un partido. 
        #E: goles_favor (int), goles_contra (int), tarjetas_am (int), tarjetas_roj (int)
        #S: Suma los valores a cada atributo
        #R: El objeto debe estar correctamente inicializado
        """
        self.__total_goles_favor += goles_favor
        self.__total_goles_contra += goles_contra
        self.__total_tarjetas_amarillas += tarjetas_am
        self.__total_tarjetas_rojas += tarjetas_roj
    
    def calcular_fuerza_equipo(self):
        """
        Calcula y actualiza el atributo fuerza_equipo 
        #E: No recibe parametros
        #S: No retorna nada, actualiza el atributo __fuerza_equipo
        #R: El objeto debe estar correctamente inicializado
        """
        copia = self.__jugadores[:]
      
        for i in range(len(copia)):
            for j in range(len(copia) - 1):
                primero = j
                siguiente = j+1
                if copia[primero].get_puntaje_individual() < copia[siguiente].get_puntaje_individual():
                    copia[primero], copia[siguiente] = copia[siguiente], copia[primero] #intercambia las posiciones
        titulares = copia[:11]

        suma = 0
        for jugador in titulares:
            suma += jugador.get_puntaje_individual()
        promedio_jugadores = suma / 11
        
        factor_entrenador = self.__entrenador.get_experiencia_anios() * 4
        if factor_entrenador > 100:
            factor_entrenador = 100
            
        factor_ranking = 100 - self.__pais.get_ranking_fifa()
        
        self.__fuerza_equipo = (promedio_jugadores * 0.6) + (factor_entrenador * 0.25) + (factor_ranking * 0.15)
    
    def get_codigo_equipo(self):
        """
        Retorna el código del equipo.
        #E: No recibe parámetros
        #S: Retorna un str con el código del equipo
        #R: El atributo __codigo_equipo debe estar inicializado
        """
        return self.__codigo_equipo
    
    def get_pais(self):
        """
        Retorna el pais del equipo.
        #E: No recibe parámetros
        #S: Retorna un objeto Pais
        #R: El atributo __pais debe estar inicializado
        """
        return self.__pais
    
    def get_entrenador(self):
        """
        Retorna el entrenador del equipo.
        #E: No recibe parámetros
        #S: Retorna un objeto Entrenador
        #R: El atributo __entrenador debe estar inicializado
        """
        return self.__entrenador
    
    def get_jugadores(self):
        """
        Retorna los jugadores del equipo.
        #E: No recibe parámetros
        #S: Retorna una list con los jugadores
        #R: El atributo __jugadores debe estar inicializado
        """
        return self.__jugadores
        
    def get_fuerza_equipo(self):
        """
        Retorna la fuerza del equipo.
        #E: No recibe parámetros
        #S: Retorna un float con la fuerza
        #R: El atributo __fuerza_equipo debe estar inicializado
        """
        return self.__fuerza_equipo
    
    def get_total_goles_favor(self):
        """
        Retorna el total de goles a favor del equipo.
        #E: No recibe parámetros
        #S: Retorna un int con los goles a favor
        #R: El atributo __total_goles_favor debe estar inicializado
        """
        return self.__total_goles_favor
        
    def get_total_goles_contra(self):
        """
        Retorna el total de goles en contra del equipo.
        #E: No recibe parámetros
        #S: Retorna un int con los goles en contra
        #R: El atributo __total_goles_contra debe estar inicializado
        """
        return self.__total_goles_contra
    
    def get_total_tarjetas_amarillas(self):
        """
        Retorna el total de tarjetas amarillas del equipo.
        #E: No recibe parámetros
        #S: Retorna un int con las tarjetas amarillas
        #R: El atributo __total_tarjetas_amarillas debe estar inicializado
        """
        return self.__total_tarjetas_amarillas
    
    def get_total_tarjetas_rojas(self):
        """
        Retorna el total de tarjetas rojas del equipo.
        #E: No recibe parámetros
        #S: Retorna un int con las tarjetas rojas
        #R: El atributo __total_tarjetas_rojas debe estar inicializado
        """
        return self.__total_tarjetas_rojas
    
    def actualizar_fase_alcanzada(self, fase):
        """
        Actualiza la fase alcanzada por la selección.
        #E: fase (str)
        #S: No retorna nada, cambia la fase alcanzada
        #R: fase debe ser un texto válido
        """
        self.__fase_alcanzada = fase


    def get_fase_alcanzada(self):
        """
        Retorna la fase alcanzada por la selección.
        #E: No recibe parámetros
        #S: Retorna un str con la fase alcanzada
        #R: El atributo __fase_alcanzada debe estar inicializado
        """
        return self.__fase_alcanzada
