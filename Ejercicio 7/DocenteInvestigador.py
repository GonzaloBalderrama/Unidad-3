from Investigador import Investigador
from Docente import Docente

class DocenteInvestigador(Docente,Investigador):
    __categoria = None
    __importe_extra = None

    def __init__(self, cuil, apellido, nombre, sueldob, antiguedad, carreras, cargo, catedra, area, tipo, categoria, importee):
        super.__init__(self, cuil, apellido, nombre, sueldob, antiguedad, carreras, cargo, catedra, area, tipo, categoria, importee)
        self.__categoria = categoria
        self.__importe_extra = importee