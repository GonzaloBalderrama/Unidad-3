from Manejador import Manejador
from Aparato import Aparato
from Televisor import Televisor
from ObjectEncoder import ObjectEncoder

if __name__=="__main__":
    jsonF= ObjectEncoder()
    manejador = Manejador()
    diccionario = jsonF.leerJSONArchivo('aparatoselectronicos.json')
    manejador = jsonF.decodificarDiccionario(diccionario)

    for aparato in manejador:
        print(f"*{aparato}")
