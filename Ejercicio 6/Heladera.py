from Aparato import Aparato

class Heladera(Aparato):
        __capacidad = None
        __freezer = None
        __ciclica = None

        def __init__(self, mar, mod, col, pais, precio, capa, free, cicl):
                super().__init__(mar, mod, col, pais, precio)
                self.__capacidad = capa
                self.__freezer = free
                self.__ciclica = cicl

        def __str__(self):
                return f"HELADERA: {self.getMarca()} - {self.getPais()} - ${self.getPrecio()}"

        def importeHeladera(self):
                total = self.__actual.getDatos().getPrecioBase()
                freezer = self.__actual.getDatos.getFreezer()
                ciclica = self.__actual.getDatos().getCiclica()
                if  freezer:
                        imp = total + (total * 5 / 100)
                else:
                        imp = total + (total / 100)
                if ciclica:
                        imp += total + (total * 10 / 100)
                return imp

        def toJSON(self):
                d = dict(
                        __class__=self.__class__.__name__,__atributos__=dict(
                        mar= self.getMarca(), 
                        mod= self.getModelo(), 
                        col= self.getColor(), 
                        pais= self.getPais(), 
                        precio = self.getPrecio(),
                        capa=self.__capacidad,
                        free=self.__freezer,
                        cicl=self.__ciclica
                        )
                )
                return d