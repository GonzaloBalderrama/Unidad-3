from ManejadorRamos import ManejadorRamos
from ManejadorFlores import ManejadorFlores

class Menu:
    def mostrarMenu(self, flores, ramos):
        ban = True
        print("------------------ ❀ FRAGANCIAS NATURALES ❀ ------------------")
        print("1- Registrar ramo")
        print("2- Mostrar 5 flores mas pedidas")
        print("3- Buscar tipo de ramo y mostrar flores mas vendidas")
        print("4- Salir")
        print("--------------------------------------------------------------")
        opcion = input("-> ")
        if int(opcion) == 1:
            print(flores)
            ramos.crearRamo(flores.getFlores())
        elif int(opcion) == 2:
            ramos.masVendidas(flores.getFlores())
        elif int(opcion) == 3:
            pass
        elif int(opcion) == 4:
            ban = False
        return ban
