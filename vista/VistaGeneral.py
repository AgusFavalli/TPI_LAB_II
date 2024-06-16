class VistaGeneral:
    def bienvenida(self):
        print("-----BIENVENIDOS-----"
              "\n1 - Listado mascotas activas"
              "\n2 - Listado de razas"
              "\n3 - Listado de vacunas"
              "\n4 - ___"
              )

    def menu(self):
        return input("Ingrese una opcion")

    def getMensaje(self, dato):
        print (dato)

    def mostrarLista(self,lista):
        for i in lista:
            print(i)