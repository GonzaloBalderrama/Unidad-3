from Flor import Flor
import numpy as np 
import csv

class ManejadorFlores:
    __indice = 0
    __cantidad = 0

    def __init__(self):
        self.__Flores = np.empty(30, dtype=Flor)

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
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                unaFlor = Flor(int(fila[0]), fila[1], bool(fila[2]), fila[3], fila[4], fila[5], fila[6], fila[7])
                self.agregarFlor(unaFlor)
                self.__indice += 1
        archivo.close()