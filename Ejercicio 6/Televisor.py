from Aparato import Aparato

class Televisor(Aparato):
        __tdepantalla = None
        __pulgadas = None
        __definicion = None
        __conexion = None
        def __init__(self, mar, mod, col, pais, precio, tdepant, pulg, defi, conex):
                super().__init__(mar, mod, col, pais, precio)
                self.__tdepantalla = tdepant
                self.__pulgadas = pulg
                self.__definicion = defi
                self.__conexion = conex

        def __str__(self):
                return f"TELEVISOR: {self.getMarca()} - {self.getPais()} - ${self.getPrecio()}"

        def importeTelevisor(self):
                total = self.__actual.getDatos().getPrecioBase()
                definicion = self.__actual.getDatos().getTipoDefinicion()
                internet = self.__actual.getDatos().getInternet()
                if definicion == 'SD':
                        imp = total + (total / 100)
                elif definicion == 'HD':
                        imp = total + (total * 2 / 100)
                elif definicion == 'FULL HD':
                        imp = total + (total * 3 / 100)
                if internet == True:
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
                        tdepant=self.__tdepantalla,
                        pulg=self.__pulgadas,
                        defi=self.__definicion,
                        conex=self.__conexion
                        )
                )
                return d