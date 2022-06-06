from Aparato import Aparato

class Lavarropa(Aparato):
    __capacidad = None
    __veldecent = None
    __cantprog = None
    __tipodecarga = None

    def __init__(self, mar, mod, col, pais, precio, capa, vel, prog, carga):
        super().__init__(mar, mod, col, pais, precio)
        self.__capacidad = capa
        self.__veldecent = vel
        self.__cantprog = prog
        self.__tipodecarga = carga

    def __str__(self):
        return f"LAVARROPA: {self.getMarca()} - {self.getPais()} - ${self.getPrecio()}"

    def importeLavarropa(self):
        total = self.__actual.getDatos().getPrecioBase()
        capacidad = self.__actual.getDatos().getCapacidadLavado()
        if  capacidad <= 5:
                imp = total + (total / 100)
        elif capacidad > 5:
                imp = total + (total * 3 / 100)
        return imp

    def getTipoDeCarga(self):
            return self.__tipodecarga

    def toJSON(self):
                d = dict(
                        __class__=self.__class__.__name__,__atributos__=dict(
                        mar= self.getMarca(), 
                        mod= self.getModelo(), 
                        col= self.getColor(), 
                        pais= self.getPais(), 
                        precio = self.getPrecio(),
                        capa=self.__capacidad,
                        vel=self.__veldecent,
                        prog=self.__cantprog,
                        carga=self.__tipodecarga
                        )
                )
                return d