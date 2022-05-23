from ManejadorFlores import ManejadorFlores
from Menu import Menu
from ManejadorRamos import ManejadorRamos
from ManejadorFlores import ManejadorFlores

if __name__=="__main__":
    menu = Menu()
    ban = True
    flores = ManejadorFlores()
    flores.crearFlor()
    ramos = ManejadorRamos()
    while ban:
        ban = menu.mostrarMenu(flores,ramos)
