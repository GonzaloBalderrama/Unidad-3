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

    def leerArchivo(self):
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
                cod = int(fila[0])
                unaFacu = Facultad(int(fila[0]), fila[1], fila[2], fila[3], fila[4])
                ban = True
            elif cod == int(fila[0]):
                unaCarrera = Carrera(int(fila[1]), fila[2], fila[3], fila[4], fila[5])
                listaCarreras.append(unaCarrera)
        unaFacu.actualizarCarrera(listaCarreras)
        listaCarreras = []
        self.agregarFacultad(unaFacu)
        archivo.close()

    def buscarFacultad(self):
        cod = int(input("Ingrese el codigo de la facultad --> "))
        i = 0
        ban = False
        while i<len(self.__facultades) and not ban:
            if cod == self.__facultades[i].getCodigo():
                ban = True
            else:
                i += 1
        print("*********************************** INFORME ***********************************")
        print(f"✹FACULTAD: {self.__facultades[i].getNombre()}                  ✹CODIGO: {self.__facultades[i].getCodigo()}")
        print("\n✹CARRERAS:")
        carreras = self.__facultades[i].getCarreras()
        for fila in carreras:
            print(f"↦{fila.getNombre()},  {fila.getDuracion()}")
        print("*******************************************************************************")

    def buscarCarrera(self):
        nom = input("Ingrese el nombre de la carrera --> ")
        i = 0
        ban = False
        try:
            while i<len(self.__facultades) and not ban:
                carreras = self.__facultades[i].getCarreras()
                j = 0
                while j<len(carreras) and not ban:
                    if nom == carreras[j].getNombre():
                        ban = True
                    j += 1
                i += 1      
            print("\n*********************************** INFORME ***********************************")
            print(f"✹CODIGO: {self.__facultades[i].getCodigo()}.{carreras[j].getCodigo()}\n✹FACULTAD: {self.__facultades[i].getNombre()}                    ✹LOCALIDAD: {self.__facultades[i].getLocalidad()}")
            print("*******************************************************************************")
        except:
            print("¡Carrera no encontrada!")
            print("*******************************************************************************")