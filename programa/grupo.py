from partido import Partido
from datetime import date

class Grupo:
    def __init__(self, nombre_grupo):
        """
        Constructor que inicializa los atributos de la clase Grupo.
        #E: nombre_grupo (str)
        #S: No retorna nada
        #R: El nombre del grupo debe ser un str no vacío
        """
        self.__nombre_grupo = nombre_grupo
        self.__equipos = []
        self.__partidos = []

    def agregar_equipo(self, seleccion):
        """
        Agrega una selección al grupo.
        #E: seleccion (Seleccion)
        #S: Retorna True si la selección se agrega correctamente, False en caso contrario
        #R: El grupo no puede tener más de 4 equipos
        """
        cantidad = len(self.__equipos)
        if cantidad < 4:
            self.__equipos.append(seleccion)
            return True
        return False
    
    def jugar_partidos(self):
        """
        Genera y simula todos los partidos de todos contra todos dentro del grupo.
        #E: No recibe parámetros
        #S: No retorna nada, agrega los partidos simulados a la lista de partidos
        #R: El grupo debe tener al menos 2 equipos agregados previamente
        """
        for i in range(len(self.__equipos)):
            for j in range(i+1, len(self.__equipos)):

                equipo_1 = self.__equipos[i]
                equipo_2 = self.__equipos[j]

                id_partido = len(self.__partidos) + 1

                partido = Partido(id_partido, equipo_1, equipo_2, "Fase de grupos", date.today().strftime("%d/%m/%Y"))
                partido.simular()

                self.__partidos.append(partido)

    def calcular_tabla(self):
        """
        Calcula la tabla de posiciones del grupo.
        #E: No recibe parámetros
        #S: Retorna una lista con la tabla de posiciones actualizada
        #R: Los partidos del grupo deben haber sido simulados previamente
        """

        # Crear la tabla inicial con todos los equipos en cero
        #[equipo, puntos, goles_favor, goles_contra, diferencia]
        tabla = [ ]
        for equipo in self.__equipos:
            tabla.append([equipo, 0, 0, 0, 0])

        # Recorrer todos los partidos de grupo
        for partido in self.__partidos:

            equipo1 = partido.get_equipo_1()
            equipo2 = partido.get_equipo_2()

            goles1 = partido.get_goles_equipo1()
            goles2 = partido.get_goles_equipo2()

            # Actualizar estadisticas de cada equipo en la tabla
            for fila in tabla:
                # Actualizar datos del equipo 1
                if fila[0] == equipo1:
                    fila[2] += goles1
                    fila[3] += goles2
                    # Victoria del equipo 1
                    if goles1 > goles2:
                        fila[1] += 3
                    # Empate
                    elif goles1 == goles2:
                        fila[1] += 1

                # Actualizar datos del equipo 2
                else:
                    if fila[0] == equipo2:
                        fila[2] += goles2
                        fila[3] += goles1
                        # Victoria del equipo 2
                        if goles2 > goles1:
                            fila[1] += 3
                          # Empate   
                        elif goles1 == goles2:
                            fila[1] += 1

        # Calcular la diferencia de goles de cada equipo
        for fila in tabla:
            fila[4] = fila[2] - fila[3]
        
        # Ordenar la tabla de mayor a menor según:
        # 1. Puntos
        # 2. Diferencia de goles 
        # 3. Goles favor
        
        for i in range(len(tabla)):
            for j in range(len(tabla) - 1):
                primero = j
                siguiente = j+1

                # Comparar puntos
                if tabla[primero][1] < tabla[siguiente][1]:
                    tabla[primero], tabla[siguiente] = tabla[siguiente], tabla[primero]
                    
                    # Si tienen los mismos puntos, comparar diferencia de goles
                elif tabla[primero][1] == tabla[siguiente][1]:
                    if tabla[primero][4] < tabla[siguiente][4]:
                        tabla[primero], tabla[siguiente] = tabla[siguiente], tabla[primero]

                    # Si también tienen la misma diferencia, comparar goles a favor
                    elif tabla[primero][4] == tabla[siguiente][4]:
                        if tabla[primero][2] < tabla[siguiente][2]:
                            tabla[primero], tabla[siguiente] = tabla[siguiente], tabla[primero]
        
        return tabla


    def obtener_clasificados(self):
        """
        Obtiene las dos selecciones clasificadas a la siguiente fase.
        #E: No recibe parámetros
        #S: Retorna una lista con las dos mejores selecciones
        #R: La tabla del grupo debe poder calcularse correctamente
        """

        tabla = self.calcular_tabla()
        clasificado1 = tabla[0][0]
        clasificado2 = tabla[1][0]
        return [clasificado1, clasificado2]

    def mostrar_tabla(self):
        """
        Muestra la tabla de posiciones del grupo.
        #E: No recibe parámetros
        #S: Retorna un str con la tabla de posiciones del grupo
        #R: Los partidos del grupo deben haber sido simulados previamente
        """
        tabla = self.calcular_tabla()
        resultado = self.__nombre_grupo + "\n\n"
        for fila in tabla:
            nombre = fila[0].get_pais().get_nombre()
            puntos = fila[1]
            goles_favor = fila[2]
            goles_contra = fila[3]
            dif_goles = fila[4]

            resultado += f"{nombre} | Pts: {puntos} | Goles a favor: {goles_favor} | Goles en contra: {goles_contra} | Diferencia goles: {dif_goles}\n"
        
        return  resultado
    
    def get_nombre_grupo(self):
        """
        Retorna el nombre del grupo.
        #E: No recibe parámetros
        #S: Retorna un str con el nombre del grupo
        #R: El atributo __nombre_grupo debe estar inicializado
        """
        return self.__nombre_grupo
    
    def get_equipos(self):
        """
        Retorna la lista de equipos del grupo.
        #E: No recibe parámetros
        #S: Retorna una lista de objetos Seleccion
        #R: El atributo __equipos debe estar inicializado
        """
        return self.__equipos
    
    def get_partidos(self):
        """
        Retorna la lista de partidos del grupo.
        #E: No recibe parámetros
        #S: Retorna una lista de objetos Partido
        #R: El atributo __partidos debe estar inicializado
        """
        return self.__partidos
    
