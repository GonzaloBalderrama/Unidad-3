from asyncio.proactor_events import _ProactorBaseWritePipeTransport


from Personal import Personal

class Docente(Personal):
    __carreras = None
    __cargo = None
    __catedra = None

    def __init__(self, cuil, apellido, nombre, sueldob, antiguedad, carreras, cargo, catedra):
        super.__init__(self, cuil, apellido, nombre, sueldob, antiguedad)
        self.__carreras = carreras
        self.__cargo = cargo
        self.__catedra = catedra