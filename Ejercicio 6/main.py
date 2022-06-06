from Manejador import Manejador
from Aparato import Aparato
from Televisor import Televisor
from ObjectEncoder import ObjectEncoder
from Menu import Menu

if __name__=="__main__":
    bandera = True
    menu = Menu()
    jsonF= ObjectEncoder()
    manejador = Manejador()
    diccionario = jsonF.leerJSONArchivo('aparatoselectronicos.json')
    manejador = jsonF.decodificarDiccionario(diccionario)

    while bandera:
        opcion= menu.mostrarMenu()
        if opcion == 1:
            manejador.buscarPosicion()
        elif opcion == 2:
            aparato = manejador.nuevoAparato()
            manejador.agregarAparato(aparato)
        elif opcion == 3:
            pass
        elif opcion == 4:
            for aparato in manejador:
                if aparato.getMarca() == "Phillips":
                    print(aparato)
        elif opcion == 5:
            for aparato in manejador:
                if aparato.__class__.__name__ == "Lavarropa":
                    if aparato.getTipoDeCarga() == "Superior":
                        print(aparato)
        elif opcion == 6:
            for aparato in manejador:
                print(f"*{aparato}")
        elif opcion == 7:
            d=manejador.toJSON()
            jsonF.guardarJSONArchivo(d,'aparatoselectronicos.json')
        elif opcion == 8:
            bandera = False

