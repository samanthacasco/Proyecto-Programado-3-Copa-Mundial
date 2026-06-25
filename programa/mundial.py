from grupo import Grupo
from fase import Fase

class Mundial:
    def __init__(self, nombre, anio):
        """
        Constructor que inicializa los atributos de la clase Mundial
        #E: nombre (str), anio (int)
        #S: No retorna nada
        #R: El nombre debe ser un str no vacío y el año debe ser int
        """
        self.__nombre = nombre
        self.__anio = anio
        self.__paises = []
        self.__selecciones = []
        self.__grupos = []
        self.__fases = []
        self.__campeon = None

    def registrar_pais(self, pais):
        """
        Registra un país en el mundial
        #E: pais (Pais)
        #S: No retorna nada, agrega el país a la lista de países
        #R: El parámetro debe ser un objeto Pais válido
        """
        self.__paises.append(pais)

    def registrar_seleccion(self, seleccion):
        """
        Registra una selección en el mundial
        #E: seleccion (Seleccion)
        #S: No retorna nada, agrega la selección a la lista de selecciones
        #R: El parámetro debe ser un objeto Seleccion válido
        """
        self.__selecciones.append(seleccion)

    def crear_grupos(self, cantidad_grupos):
        if cantidad_grupos < 2:
            return False
    
        cantidad_selecciones = len(self.__selecciones)
        if cantidad_selecciones != cantidad_grupos * 4:
            return False
        
        self.__grupos = [ ]
        letras = ["A", "B", "C", "D", "E", "F", "G", "H","I", "J", "K", "L", "M", "N", "O", "P"]
        for i in range(cantidad_grupos):
            nombre_grupo = "Grupo " + letras[i]
            grupo = Grupo(nombre_grupo)
            self.__grupos.append(grupo)

        indice_seleccion = 0
        for grupo in self.__grupos:
            for i in range(4):
                seleccion = self.__selecciones[indice_seleccion]
                grupo.agregar_equipo(seleccion)
                indice_seleccion += 1
            
        return True
    
    def jugar_fase_grupos(self):
        """
        Simula todos los partidos de la fase de grupos
        #E: No recibe parámetros
        #S: No retorna nada, simula los partidos de todos los grupos
        #R: Los grupos deben haber sido creados previamente
        """
        for grupo in self.__grupos:
            grupo.jugar_partidos()
    
    def armar_fase_eliminatoria(self, nombre_fase, clasificados):
        """
        Crea una fase eliminatoria a partir de una lista de selecciones clasificadas
        #E: nombre_fase (str), clasificados (lista)
        #S: Retorna un objeto Fase con los partidos registrados
        #R: La lista de clasificados debe tener selecciones válidas
        """
        fase = Fase(nombre_fase)
        i = 0
        while i < len(clasificados):
            equipo1 = clasificados[i]
            equipo2 = clasificados[i + 1]

            fase.registrar_juego(equipo1, equipo2)
            i += 2 # Avanza a la siguiente pareja de equipos
        self.__fases.append(fase)

        return fase
    
    def jugar_fase_eliminatoria(self, fase):
        """
        Simula una fase eliminatoria y retorna sus clasificados
        #E: fase (Fase)
        #S: Retorna una lista con las selecciones clasificadas a la siguiente ronda
        #R: La fase debe tener partidos registrados previamente
        """
        fase.jugar_fase()
        return fase.obtener_clasificados()
    
    def obtener_clasificados_grupos(self):
        """
        Obtiene los equipos clasificados desde la fase de grupos
        #E: No recibe parámetros
        #S: Retorna una lista con las selecciones clasificadas de todos los grupos
        #R: Los grupos deben haber jugado sus partidos previamente
        """
        clasificados = []

        for grupo in self.__grupos:
            clasificados_grupo = grupo.obtener_clasificados()

            for seleccion in clasificados_grupo:
                clasificados.append(seleccion)

        return clasificados
    
    def determinar_campeon(self):
        """
        Ejecuta las fases eliminatorias hasta determinar la selección campeona
        #E: No recibe parámetros
        #S: Retorna la selección campeona del mundial
        #R: La fase de grupos debe haberse jugado previamente
        """
        clasificados = self.obtener_clasificados_grupos()

        if len(clasificados) == 32:
            fase = self.armar_fase_eliminatoria("Dieciseisavos de final", clasificados)
            clasificados = self.jugar_fase_eliminatoria(fase)

        if len(clasificados) == 16:
            fase = self.armar_fase_eliminatoria("Octavos de final", clasificados)
            clasificados = self.jugar_fase_eliminatoria(fase)

        if len(clasificados) == 8:
            fase = self.armar_fase_eliminatoria("Cuartos de final", clasificados)
            clasificados = self.jugar_fase_eliminatoria(fase)

        if len(clasificados) == 4:
            fase = self.armar_fase_eliminatoria("Semifinales", clasificados)
            clasificados = self.jugar_fase_eliminatoria(fase)

        if len(clasificados) == 2:
            fase = self.armar_fase_eliminatoria("Final", clasificados)
            clasificados = self.jugar_fase_eliminatoria(fase)

        self.__campeon = clasificados[0]

        return self.__campeon
    
    def mostrar_tabla_general(self):
        """
        Muestra las tablas de posiciones de todos los grupos del mundial
        #E: No recibe parámetros
        #S: Retorna un str con las tablas de todos los grupos
        #R: Los grupos deben haber sido creados y sus partidos simulados previamente
        """
        resultado = ""

        for grupo in self.__grupos:
            resultado += grupo.mostrar_tabla()
            resultado += "\n"

        return resultado
    
    def obtener_todos_los_partidos(self):
        """
        Obtiene todos los partidos jugados en el mundial
        #E: No recibe parámetros
        #S: Retorna una lista con todos los partidos de grupos y fases eliminatorias
        #R: Los grupos y fases deben haberse creado previamente
        """
        partidos = []

        for grupo in self.__grupos:
            partidos_grupo = grupo.get_partidos()

            for partido in partidos_grupo:
                partidos.append(partido)

        for fase in self.__fases:
            partidos_fase = fase.get_partidos()

            for partido in partidos_fase:
                partidos.append(partido)

        return partidos

    def generar_reporte(self):
        """
        Genera los archivos de texto principales del mundial
        #E: No recibe parámetros
        #S: No retorna nada, guarda la información del mundial en archivos txt
        #R: El mundial debe tener información registrada previamente
        """
        from persistencia import guardar_paises, guardar_selecciones, guardar_partidos, guardar_ranking_goleadores

        partidos = self.obtener_todos_los_partidos()

        jugadores = [ ]
        for seleccion in self.__selecciones:
            for jugador in seleccion.get_jugadores():
                jugadores.apppend(jugador)

        guardar_paises(self.__paises)
        guardar_selecciones(self.__selecciones)
        guardar_partidos(partidos)
        guardar_ranking_goleadores(jugadores)
    
    def get_nombre(self):
        """
        Retorna el nombre del mundial
        #E: No recibe parámetros
        #S: Retorna un str con el nombre del mundial
        #R: El atributo __nombre debe estar inicializado
        """
        return self.__nombre


    def get_anio(self):
        """
        Retorna el año del mundial
        #E: No recibe parámetros
        #S: Retorna un int con el año del mundial
        #R: El atributo __anio debe estar inicializado
        """
        return self.__anio


    def get_paises(self):
        """
        Retorna la lista de países registrados
        #E: No recibe parámetros
        #S: Retorna una lista de objetos Pais
        #R: El atributo __paises debe estar inicializado
        """
        return self.__paises


    def get_selecciones(self):
        """
        Retorna la lista de selecciones registradas
        #E: No recibe parámetros
        #S: Retorna una lista de objetos Seleccion
        #R: El atributo __selecciones debe estar inicializado
        """
        return self.__selecciones


    def get_grupos(self):
        """
        Retorna la lista de grupos del mundial
        #E: No recibe parámetros
        #S: Retorna una lista de objetos Grupo
        #R: El atributo __grupos debe estar inicializado
        """
        return self.__grupos


    def get_fases(self):
        """
        Retorna la lista de fases eliminatorias del mundial
        #E: No recibe parámetros
        #S: Retorna una lista de objetos Fase
        #R: El atributo __fases debe estar inicializado
        """
        return self.__fases


    def get_campeon(self):
        """
        Retorna la selección campeona del mundial
        #E: No recibe parámetros
        #S: Retorna un objeto Seleccion con la selección campeona
        #R: El mundial debe haberse jugado previamente para tener campeón
        """
        return self.__campeon
            