"""Clase general de la cual heredan Entrenador y Futbolista"""
class Persona:
    """
    Constructor que inicializa los atributos de la clase Persona.
    #E: nombre (str), apellido (str), fecha_nacimiento (str), nacionalidad (str)
    #S: No retorna nada
    #R: Todos los parámetros deben ser str no vacíos
    """
    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_nacimiento = fecha_nacimiento
        self.__nacionalidad = nacionalidad
    
    def mostrar_datos(self):
        """
        Muestra la información básica de la persona.
        #E: No recibe parámetros
        #S: Retorna un str con la información de la persona
        #R: El objeto debe estar correctamente inicializado
        """
        return f"Nombre: {self.__nombre}, Apellido: {self.__apellido}, Fecha de Nacimiento: {self.__fecha_nacimiento}, Nacionalidad: {self.__nacionalidad}"    
    
    def get_nombre(self):
        """
        Retorna el nombre de la persona.
        #E: No recibe parámetros
        #S: Retorna un str con el nombre
        #R: El atributo __nombre debe estar inicializado
        """
        return self.__nombre

    def get_apellido(self):
        """
        Retorna el apellido de la persona.
        #E: No recibe parámetros
        #S: Retorna un str con el apellido
        #R: El atributo __apellido debe estar inicializado
        """
        return self.__apellido

    def get_fecha_nacimiento(self):
        """
        Retorna la fecha de nacimiento de la persona.
        #E: No recibe parámetros
        #S: Retorna un str con la fecha de nacimiento 
        #R: El atributo __fecha_nacimiento debe estar inicializado
        """
        return self.__fecha_nacimiento

    def get_nacionalidad(self):
        """
        Retorna la nacionalidad de la persona.
        #E: No recibe parámetros
        #S: Retorna un str con la nacionalidad
        #R: El atributo __nacionalidad debe estar inicializado
        """
        return self.__nacionalidad
