class FLor:
    __numero = 0 
    __nombre = "" 
    __color = "" 
    __descripcion = ""

    def __init__(self, num, nom, color, desc):
        self.__numero = num
        self.__nombre = nom
        self.__color = color
        self.__descripcion = desc

    def __str__(self):
        return f"{self.__numero} - {self.__nombre}, {self.__color}"
