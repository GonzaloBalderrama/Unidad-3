class Contrato:
    __fechai = ""
    __fechaf = ""
    __pagom = 0
    __jugador = None
    __equipo = None

    def __init__(self, fi, ff, pm, ju, eq):
        self.__fechai = fi
        self.__fechaf = ff
        self.__pagom = pm
        self.__jugador = ju
        self.__equipo = eq

    def __str__(self):
        return f"{self.__jugador}: {self.__equipo}"

