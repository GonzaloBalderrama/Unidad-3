class Equipo:
    __nombre = ""
    __ciudad = ""
    __contratos = []

    def __init__(self, nom, ciu, cont = None):
        self.__nombre = nom
        self.__ciudad = ciu
        self.__contratos = []

    def __str__(self):
        s = f"{self.__nombre} - {self.__ciudad}\nContratos:"
        for contrato in self.__contratos:
            s += f"{contrato}"
        return s