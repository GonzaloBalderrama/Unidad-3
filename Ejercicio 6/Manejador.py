from Heladera import Heladera
from Lavarropa import Lavarropa
from Nodo import Nodo
from Televisor import Televisor

class Manejador:
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0

    def __init__(self):
        self.__comienzo=None
        self.__actual=None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato

    def agregarAparato(self, aparato):
        nodo = Nodo(aparato)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1

    def toJSON(self):
        d = dict(
        __class__=self.__class__.__name__,
        aparatos=[aparato.toJSON() for aparato in self]
        )
        return d

    def nuevoAparato(self):
        bandera = False
        while not bandera:
            print("Escriba el tipo de aparato que desea agregar")
            tipo=input("->")
            if tipo == "Televisor":
                mar = input("Marca-> ")
                mod = input("Modelo-> ")
                col = input("Color-> ")
                pais = input("Pais de fabricacion-> ")
                precio = int(input("Precio-> "))
                tdepant = input("Tipo de pantalla-> ")
                pulg = int(input("Pulgadas-> "))
                defi = input("Definicion-> ")
                conexion = int(input("Conexion a internet 1(si) o 2(no)->"))
                if conexion == 1:
                    conex = True
                else:
                    conex = False
                aparato = Televisor(mar, mod, col, pais, precio, tdepant, pulg, defi, conex)
                bandera = True

            elif tipo == "Heladera":
                mar = input("Marca-> ")
                mod = input("Modelo-> ")
                col = input("Color-> ")
                pais = input("Pais de fabricacion-> ")
                precio = int(input("Precio-> "))
                capa = input("Capacidad-> ")
                free = bool(input("Freezer 1(si) o 0(no)-> "))
                cicl = bool(input("Ciclica 1(si) o 0(no)-> "))
                aparato = Heladera(mar, mod, col, pais, precio, capa, free, cicl)
                bandera = True

            elif tipo == "Lavarropa":
                mar = input("Marca-> ")
                mod = input("Modelo-> ")
                col = input("Color-> ")
                pais = input("Pais de fabricacion-> ")
                precio = int(input("Precio-> "))
                capa = input("Capacidad-> ")
                vel = ("Velocidad de centrifugado-> ")
                prog = input("CAntidad de programas-> ")
                carga = ("Tipo de carga-> ")
                aparato = Lavarropa(mar, mod, col, pais, precio, capa, vel, prog, carga)
                bandera = True
            else:
                print("¡Opcion invalida!")

        return aparato

    def buscarPosicion(self):
        bandera = False
        while not bandera:
            posicion = int(input("Posicion en la que deseaagregar el nuevo aparato-> "))
            if posicion < self.__tope:
                bandera = True
            else:
                print("Posicion invalida, intente nuevamente")
        aparato = self.nuevoAparato()
        i=0
        for nodo in self:
            if i == posicion:
                nuevo_nodo = Nodo(aparato)
                nodo.setSiguiente(nuevo_nodo)
                nuevo_nodo.setSiguiente(nodo.getSiguiente())
                self.__tope+=1
            i+=1
