from re import S


class Flor:
    __numero = 0 
    __nombre = "" 
    __color = "" 
    __descripcion = ""
    __cantvendida = 0

    def __init__(self, num, nom, color, desc, cant=0):
        self.__numero = num
        self.__nombre = nom
        self.__color = color
        self.__descripcion = desc
        self.__cantvendida= cant

    def __str__(self):
        s = f"{self.__numero} - {self.__nombre} (Color: {self.__color}, Vendidas: {self.__cantvendida})"
        return s

    def getNumero(self):
        return self.__numero

    def getNombre(self):
        return self.__nombre

    def sumarVendida(self, cant):
        self.__cantvendida += cant

    def getCantidad(self):
        return self.__cantvendida

    def __gt__(self,otraFlor):
        ban = True
        if self.__cantvendida<otraFlor.getCantidad():
            ban = False
        return ban