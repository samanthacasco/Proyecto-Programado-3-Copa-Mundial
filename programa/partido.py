import random 

class Partido:
    def __init__(self, id_partido, equipo_1, equipo_2, fase, fecha):
        """
        Constructor que inicializa los atributos de la clase Partido
        #E: id_partido (int), equipo_1 (Seleccion), equipo_2 (Seleccion), fase(str), fecha(str)
        #S: No retorna nada
        #R: equipo_1 y equipo_2 deben ser selecciones
        """
        self.__id_partido = id_partido 
        self.__equipo_1 = equipo_1
        self.__equipo_2 = equipo_2
        self.__goles_equipo1 = 0
        self.__goles_equipo2 = 0
        self.__fase = fase
        self.__fecha = fecha

    def simular(self):
        """
        Simula el resultado del partido según la fuerza de cada equipo.
        #E: No recibe parámetros
        #S: No retorna nada, actualiza los goles del partido
        #R: Los equipos deben tener calculada su fuerza_equipo
        """
        fuerza_equipo1 = self.__equipo_1.get_fuerza_equipo()
        fuerza_equipo2 = self.__equipo_2.get_fuerza_equipo()

        diferencia = abs(fuerza_equipo1 - fuerza_equipo2)

        # Caso 1: equipos parejos
        if diferencia <= 15:
            self.__goles_equipo1 = random.randint(0, 4)
            self.__goles_equipo2 = random.randint(0, 4)
        
        # Caso 2: diferencia moderada
        elif diferencia > 15 and diferencia <= 30:
            if fuerza_equipo1 > fuerza_equipo2:
                self.__goles_equipo1 =  random.randint(1, 5)
                self.__goles_equipo2 =  random.randint(0, 4)
            else: 
                self.__goles_equipo1 =  random.randint(0, 4)
                self.__goles_equipo2 =  random.randint(1, 5)

        # Caso 3: diferencia grande     
        else:
            if fuerza_equipo1 > fuerza_equipo2:
                self.__goles_equipo1 =  random.randint(2, 6)
                self.__goles_equipo2 =  random.randint(0, 3)
            else: 
                self.__goles_equipo1 =  random.randint(0, 3)
                self.__goles_equipo2 =  random.randint(2, 6)
        
        # Registrar resultados de las estadisticas de cada seccion 
        self.__equipo_1.registrar_resultado(self.__goles_equipo1, self.__goles_equipo2, 0, 0)
        self.__equipo_2.registrar_resultado(self.__goles_equipo2, self.__goles_equipo1, 0, 0)


    def generar_ganador(self):
        """
        Determina el ganador del partido según la cantidad de goles anotados.
        #E: No recibe parámetros
        #S: Retorna el objeto Seleccion ganador o None en caso de empate
        #R: Los goles del partido deben haber sido simulados previamente
        """
        if self.__goles_equipo1 > self.__goles_equipo2:
            return self.__equipo_1
        elif self.__goles_equipo2 > self.__goles_equipo1:
            return self.__equipo_2
        else:
            return None
        
    def mostrar_resultado(self):
        """
        Muestra el resultado del partido en un formato legible.
        #E: No recibe parámetros
        #S: Retorna un str con el resultado del partido
        #R: Los equipos y los goles del partido deben estar correctamente inicializados
        """
        nombre_equipo1 = self.__equipo_1.get_pais().get_nombre()
        nombre_equipo2 = self.__equipo_2.get_pais().get_nombre()
        return f"{nombre_equipo1} {self.__goles_equipo1} - {self.__goles_equipo2} {nombre_equipo2}"
    
    def get_id_partido(self):
        """
        Retorna el identificador del partido.
        #E: No recibe parámetros
        #S: Retorna un int con el id del partido
        #R: El atributo __id_partido debe estar inicializado
        """
        return self.__id_partido
    
    def get_equipo_1(self):
        """
        Retorna el primer equipo del partido.
        #E: No recibe parámetros
        #S: Retorna un objeto Seleccion
        #R: El atributo __equipo_1 debe estar inicializado
        """
        return self.__equipo_1
    
    def get_equipo_2(self):
        """
        Retorna el segundo equipo del partido.
        #E: No recibe parámetros
        #S: Retorna un objeto Seleccion
        #R: El atributo __equipo_2 debe estar inicializado
        """
        return self.__equipo_2
    
    def get_goles_equipo1(self):
        """
        Retorna la cantidad de goles del equipo 1.
        #E: No recibe parámetros
        #S: Retorna un int con los goles del equipo 1
        #R: El atributo __goles_equipo1 debe estar inicializado
        """
        return self.__goles_equipo1
    
    def get_goles_equipo2(self):
        """
        Retorna la cantidad de goles del equipo 2.
        #E: No recibe parámetros
        #S: Retorna un int con los goles del equipo 2
        #R: El atributo __goles_equipo2 debe estar inicializado
        """
        return self.__goles_equipo2
    
    def get_fase(self):
        """
        Retorna la fase a la que pertenece el partido.
        #E: No recibe parámetros
        #S: Retorna un str con el nombre de la fase
        #R: El atributo __fase debe estar inicializado
        """
        return self.__fase

    def get_fecha(self):
        """
        Retorna la fecha del partido.
        #E: No recibe parámetros
        #S: Retorna un str con la fecha del partido
        #R: El atributo __fecha debe estar inicializado
        """
        return self.__fecha
