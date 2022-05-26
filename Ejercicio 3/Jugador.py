class Jugador:
    __nombre = ""
    __dni = 0
    __ciudadn = ""
    __pais = ""
    __fechan = ""

    def __init__(self, nom, dni, ciu, pais, fn):
        self.__nombre = nom
        self.__dni = dni
        self.__ciudadn = ciu
        self.__pais = pais
        self.__fechan = fn

    def __Str__(self):
        return f"{self.__nombre} - {self.__dni} - {self.__pais}"