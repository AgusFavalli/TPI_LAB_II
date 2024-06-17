class VistaRaza:
    def mostrarMenuPersona(self):
        print("Menú de Gestión de Personas\n"
            "1- Ver lista personas\n"
            "2- Consultar persona\n"
            "3- Agregar una persona\n"
            "4- Eliminar una persona\n"
            "5- Modificar datos de una persona\n"
            "6- Volver\n")
        return input("Seleccione una opción: ")

    def modificarRaza(self):
        vieja_raza= input("ingrese el nombre de la raza actual que desea modificar")
        return input("ingrese el nombre modificado de la raza")

    def mostrarMensaje(self, dato):
        print (dato)

    def mostrarLista(self, lista):
        for i in lista:
            print(i)

    def obtenerRaza(self):
        return input("ingrese el nombre de la raza")

    def eliminarRaza(self):
        return input("ingrese el codigo de la raza a eliminar")