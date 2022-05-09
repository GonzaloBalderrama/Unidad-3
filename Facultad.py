from Carrera import Carrera

class Facultad:
    __codigo = 0
    __nombre = ""
    __direccion = ""
    __localidad = ""
    __telefono = ""
    __carreras = []

    def __init__(self, cod, nom, dir, loc, tel, carrera = []):
        self.__codigo = cod
        self.__nombre = nom
        self.__direccion = dir
        self.__localidad = loc
        self.__telefono = tel
        self.__carreras = carrera

    def __str__(self):
        s = ""
        for fila in self.__carreras:
            s = s+str(fila)+"\n"
        return f"FACULTAD: {self.__nombre}\n{s}"
    def actualizarCarrera(self, nueva):
        self.__carreras = nueva

    def mostrarCarreras(self):
        print(f"\n\FACULTAD: {self.__nombre}")
        for fila in self.__carreras:
            print(fila)