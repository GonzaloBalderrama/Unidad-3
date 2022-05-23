from Ramo import Ramo
from ManejadorFlores import ManejadorFlores

class ManejadorRamos:
    __listaRamos= []

    def __init__(self):
        __listaRamos = []

    def agregarRamo(self, unRamo):
        self.__listaRamos.append(unRamo)

    def crearRamo(self, flores):
        ban = True
        tam = input("Ingrese el tamaño del ramo (Chico, Mediano, Grande)-> ")
        ramo = Ramo(tam)
        while ban:
            codigo = int(input("Ingrese el codigo de flor que desea agregar (0 para dejar de agregar)-> "))
            if codigo == 0:
                ban = False
            else:
                cant = int(input("Ingrese la cantidad que desea agregar -> "))
            ban2 = False
            i=0
            while not ban2 and i<len(flores) and codigo!=0:
                if codigo == flores[i].getNumero():
                    ban2 = True
                    ramo.agregarFlor(flores[i], cant)
                    flores[i].sumarVendida(cant)
                i+=1
        self.agregarRamo(ramo)
        print(ramo)

    def masVendidas(self, flores):
        flores.sort(reverse=True)
        for i in flores:
            print(i)