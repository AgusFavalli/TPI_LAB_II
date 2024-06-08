class VistaMascotas:
    def bienvenida(self):
        print("-----BIENVENIDOS-----")
        print("1 - ___")
        print("2 - ___")
        print("3 - ___")
        print("4 - ___")

    def menu(self):
        return input("Ingrese una opcion")

    def getMensaje(self, dato):
        print (dato)

    def mostrarLista(self,lista):
        for i in lista:
            print(i)