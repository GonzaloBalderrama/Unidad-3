from Ramo import Ramo
from ManejadorFlores import ManejadorFlores

class ManejadorRamos:

    def __init__(self):
        self.__listaRamos = []

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

    def masVendidas(self, flores,cant):
        flores.sort()
        i = 0
        cant -=1
        while i<5:
            print(flores[int(cant)-i])
            i +=1

    def floresVendidasPorRamo(self, tipo):
        for ramo in self.__listaRamos:
            if ramo.getTamano() == tipo:
                print("Ramo encontrado")
                i=0
                flores = ramo.getFlores()
                while i<len(flores):
                    print(flores[i].getNombre())
                    i += 1

    def mostrarListaRamos(self):
        for ramo in self.__listaRamos:
            print(ramo)
            i=0
            flores=ramo.getFlores()
            while i<len(flores):
                flores[i]
                i += 1
