class Ramo:
    __tamano = ""
    __flores = []
    
    def __init__(self, tam, flor = None):
        self.__tamano = tam
        if flor != None:
            self.agregarFlor(flor)

    def __str__(self):
        s = f"\n{self.__tamano}\n"
        for i in self.__flores:
            s += f"{i.getNombre()}\n"
        return s
    
    def agregarFlor(self, flor, cant):
        for i in range(cant):
            self.__flores.append(flor)

    def borrarFlores(self):
        self.__flores.clear()
    
    def getFlores(self):
        return self.__flores

    def getTamano(self):
        return self.__tamano
        
    
    
    
