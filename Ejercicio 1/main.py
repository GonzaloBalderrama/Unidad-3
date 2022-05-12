from ManejadorFacultades import ManejadorFacultades
from Menu import Menu

if __name__ == '__main__':
    listaFacultades = ManejadorFacultades()
    listaFacultades.leerArchivo()
    menu=Menu()
    salir = False
    band = 0
    while not salir:
        print('******************************** MENU ********************************')
        print('1.Ingrese codigo de una facultad y mostrar nombre y carreras')
        print('2.Ingrese nombre de una carrera y muestra codigo, nombre y localidad de la facultad')
        print('3.Salir')
        print('**********************************************************************')
        op = input('Opción-> ')
        menu.opcion(op,listaFacultades)
        salir = op == '3'