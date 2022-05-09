class Carrera:
    __codigo = 0
    __nombre = ""
    __fechainicio = ""
    __duracion = ""
    __titulo = ""

    def __init__(self, cod, nom, fini, dur, tit):
        self.__codigo = cod
        self.__nombre = nom
        self.__fechainicio = fini
        self.__duracion = dur
        self.__titulo = tit

    def __str__(self):
        return f"Carrera: {self.__nombre}    Codigo: {self.__codigo}   Duracion: {self.__duracion}    Titulo: {self.__titulo}"