class VistaRaza:
    def mostrarMenuPersona(self):
        print("\nMenú de Gestión de Razas\n"
            "1- Ver lista razas\n"
            "2- Agregar una nueva raza\n"
            "3- Modificar raza registrada\n"
            "4- Eliminar una raza\n"
            "5- Volver al menu principal\n")
        return input("Seleccione una opción: ")

    def modificarRaza(self):
        vieja_raza= input("ingrese el codigo de la raza actual que desea modificar")
        nueva_raza= input("ingrese el nombre del nombre modificado de la raza")
        return vieja_raza, nueva_raza

    def mostrarMensaje(self, dato):
        print (dato)

    def mostrarLista(self, lista):
        for i in lista:
            print(i)

    def obtenerRaza(self):
        return input("ingrese el nombre de la raza")

    def eliminarRaza(self):
        return input("ingrese el codigo de la raza a eliminar")