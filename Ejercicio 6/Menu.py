class Menu():
    def mostrarMenu(self):
        print("----------------------------------------------------------------------------------------------------------------------")
        print("1- Insertar un aparato en la colección en una posición determinada")
        print("2- Agregar un aparato a la colección")
        print("3- Mostrar por pantalla qué tipo de objeto se encuentra almacenado en una posición")
        print("4- Mostrar la cantidad de heladeras, lavarropas y televisores cuya marca sea phillips")
        print("5- Mostrar la marca de todos los lavarropas que tienen carga superior")
        print("6- Mostrar para todos los aparatos que la empresa tiene a la venta, marca, país de fabricación e importe de venta")
        print("7- Almacenar los objetos de la colección Lista en el archivo “aparatoselectronicos.json”")
        print("8- Salir")
        print("----------------------------------------------------------------------------------------------------------------------")
        opcion = int(input("-> "))
        return opcion
        

