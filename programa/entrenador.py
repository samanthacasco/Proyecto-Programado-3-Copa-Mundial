from persona import Persona

class Entrenador(Persona):
    
    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad, licencia, experiencia_anios, sistema_juego):
        """
        Constructor que inicializa los atributos de la clase Entrenador.
        #E: nombre (str), apellido (str), fecha_nacimiento (str), nacionalidad (str), licencia (str), experiencia_anios (int), sistema_juego (str)
        #S: No retorna nada
        #R: Todos los parámetros deben ser str no vacíos
        """
        super().__init__(nombre, apellido, fecha_nacimiento, nacionalidad)
        
        self.__licencia = licencia
        self.__experiencia_anios = experiencia_anios
        self.__sistema_juego = sistema_juego
    
    def mostrar_datos(self):
        """
        Muestra la información básica del entrenador.
        #E: No recibe parámetros
        #S: No retorna nada, imprime en consola
        #R: El objeto debe estar correctamente inicializado
        """
        datos_persona = super().mostrar_datos()
        return f"{datos_persona}\nLicencia: {self.__licencia}, Años de Experiencia: {self.__experiencia_anios}, Sistema de juego: {self.__sistema_juego}"
    
    def actualizar_datos(self, licencia, experiencia_anios, sistema_juego):
        """
        Actualiza los atributos del entrenador.
        #E: licencia (str), experiencia_anios (int), sistema_juego (str)
        #S: No retorna nada, actualiza los atributos del entrenador
        #R: El objeto debe estar correctamente inicializado
        """
        self.__licencia = licencia
        self.__experiencia_anios = experiencia_anios
        self.__sistema_juego = sistema_juego
    
    def get_licencia(self):
        """
        Retorna la licencia del entrenador 
        #E: No recibe parámetros
        #S: Retorna un str con la licencia
        #R: El atributo __licencia debe estar inicializado
        """
        return self.__licencia
    
    def get_experiencia_anios(self):
        """
        Retorna los años de experiencia del entrenador.
        #E: No recibe parámetros
        #S: Retorna un int con los años de experiencia
        #R: El atributo __experiencia_anios debe estar inicializado
        """
        return self.__experiencia_anios
    
    def get_sistema_juego(self):
        """
        Retorna el sistema de juego del entrenador.
        #E: No recibe parámetros
        #S: Retorna un str con el sistema de juego
        #R: El atributo __sistema_juego debe estar inicializado
        """
        return self.__sistema_juego
