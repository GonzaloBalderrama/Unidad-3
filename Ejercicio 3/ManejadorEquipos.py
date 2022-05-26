from Equipo import Equipo
import numpy as np
import csv

class ManejadorEquipos:
    __dimension = 5
    __cantidad = 0

    def __init__(self, dim):
        self.__Equipos = np.empty(dim, dtype=Equipo)

    def __str__(self):
        s = ""
        i = 0
        for equipo in self.__Equipos:
            if i<self.__cantidad:
                s += str(equipo)+"\n"
                i += 1
        return s

    