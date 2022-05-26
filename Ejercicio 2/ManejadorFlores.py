from Flor import Flor
import numpy as np 
import csv

class ManejadorFlores:
    __indice = 0
    __cantidad = 0

    def __init__(self):
        self.__Flores = np.empty(12, dtype=Flor)

    def __str__(self):
        s = ""
        i=0
        for flor in self.__Flores:
            if i<self.__cantidad:
                s += str(flor) + '\n'
                i += 1
        return s

    def agregarFlor(self, unaFlor):
        self.__Flores[self.__indice] = unaFlor
        self.__cantidad += 1

    def crearFlor(self):
        archivo = open("flores.csv")
        reader = csv.reader(archivo,delimiter=';')
        for fila in reader:
            unaFlor = Flor(int(fila[0]), fila[1], fila[2], fila[3])
            self.agregarFlor(unaFlor)
            self.__indice += 1
        archivo.close()

    def getFlores(self):
        return self.__Flores

    def getCantidad(self):
        return self.__cantidad