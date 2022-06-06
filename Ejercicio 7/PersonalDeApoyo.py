from Personal import Personal

class PersonalDeApoyo(Personal):
    __categoria = None

    def __init__(self, cuil, apellido, nombre, sueldob, antiguedad, categoria):
        super.__init__(self, cuil, apellido, nombre, sueldob, antiguedad)
        self.__categoria = categoria