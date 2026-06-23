class Pais:
    def __init__(self, codigo_fifa, nombre, continente, ranking_fifa):
        """
        Constructor que inicializa los atributos de la clase Pais.
        #E: codigo_fifa (str), nombre (str), continente (str), ranking_fifa (int)
        #S: No retorna nada
        #R: Todos los parámetros deben ser str no vacíos
        """
        self.__codigo_fifa = codigo_fifa
        self.__nombre = nombre
        self.__continente = continente
        self.__ranking_fifa = ranking_fifa
    
    def mostrar_datos(self):
        """
        Muestra la información básica del pais.
        #E: No recibe parámetros
        #S: Retorna un str con la información del pais
        #R: El objeto debe estar correctamente inicializado
        """
        return f"Codigo fifa: {self.__codigo_fifa}, Nombre: {self.__nombre}, Continente: {self.__continente}, Ranking fifa: {self.__ranking_fifa}"
    
    def actualizar_datos(self, codigo_fifa, nombre, continente, ranking_fifa):
        """
        Actualiza los atributos del pais.
        #E: codigo_fifa (str), nombre (str), continente (str), ranking_fifa (int)
        #S: No retorna nada, actualiza los atributos del pais
        #R: El objeto debe estar correctamente inicializado
        """
        self.__codigo_fifa = codigo_fifa
        self.__nombre = nombre
        self.__continente = continente
        self.__ranking_fifa = ranking_fifa
    
    def get_codigo_fifa(self):
        """
        Retorna el codigo fifa del pais.
        #E: No recibe parámetros
        #S: Retorna un str con el codigo fifa
        #R: El atributo __codigo_fifa debe estar inicializado
        """
        return self.__codigo_fifa
    
    def get_nombre(self):
        """
        Retorna el nombre del pais.
        #E: No recibe parámetros
        #S: Retorna un str con el nombre del pais
        #R: El atributo __nombre debe estar inicializado
        """
        return self.__nombre
    
    def get_continente(self):
        """
        Retorna el continente del pais.
        #E: No recibe parámetros
        #S: Retorna un str con el continente del pais
        #R: El atributo __continente debe estar inicializado
        """
        return self.__continente
    
    def get_ranking_fifa(self):
        """
        Retorna el ranking fifa del pais.
        #E: No recibe parámetros
        #S: Retorna un int con el ranking fifa
        #R: El atributo __ranking_fifa debe estar inicializado
        """
        return self.__ranking_fifa
