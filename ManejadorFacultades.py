from Carrera import Carrera
from Facultad import Facultad
import csv

class ManejadorFacultades:
    def __init__(self):
        self.__facultades = []

    def __str__(self):
        s = ""
        for facultad in self.__facultades:
            s += str(facultad) + '\n'
        return s

    def agregarFacultad(self, unaFacu):
        self.__facultades.append(unaFacu)

    def crearFacultad(self):
        archivo = open("Facultades.csv")
        reader = csv.reader(archivo,delimiter=',')
        listaCarreras = []
        cod = 0
        ban = False
        for fila in reader:
            if cod < int(fila[0]):
                if ban:
                    unaFacu.actualizarCarrera(listaCarreras)
                    listaCarreras = []
                    self.agregarFacultad(unaFacu)
                    print(unaFacu)
                cod = int(fila[0])
                unaFacu = Facultad(int(fila[0]), fila[1], fila[2], fila[3], fila[4])
                ban = True
            elif cod == int(fila[0]):
                unaCarrera = Carrera(int(fila[1]), fila[2], fila[3], fila[4], fila[5])
                listaCarreras.append(unaCarrera)
        unaFacu.actualizarCarrera(listaCarreras)
        listaCarreras = []
        self.agregarFacultad(unaFacu)
        print(unaFacu)
        archivo.close()