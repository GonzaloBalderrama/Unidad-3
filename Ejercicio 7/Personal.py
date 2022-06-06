class Personal:
    __cuil = None
    __apellido = None
    __nombre = None
    __sueldobasico = None
    __antiguedad = None

    def __init__(self, cuil, apellido, nombre, sueldob, antiguedad):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldobasico = sueldob
        self.__antiguedad = antiguedad
