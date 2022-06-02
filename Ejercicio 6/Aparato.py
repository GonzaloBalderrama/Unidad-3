class Aparato:
    __marca = None
    __modelo = None
    __color = None
    __paisf = None
    __preciob = None

    def __init__(self, mar="N/I", mod="N/I", col="N/I", pais="N/I", precio=0):
        self.__marca = mar
        self.__modelo = mod
        self.__color = col
        self.__paisf = pais
        self.__preciob = precio

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo
        
    def getColor(self):
        return self.__color

    def getPais(self):
        return self.__paisf

    def getPrecio(self):
        return self.__preciob
    