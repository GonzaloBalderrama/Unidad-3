from sunau import Au_read
from Personal import Personal

class Ivestigador(Personal):
    __area = None
    __tipo = None

    def __init__(self, cuil, apellido, nombre, sueldob, antiguedad, area, tipo):
        super.__init__(self, cuil, apellido, nombre, sueldob, antiguedad,)
        self.__area = area
        self.__tipo = tipo
