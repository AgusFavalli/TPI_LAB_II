class VistaGeneral:
    def bienvenida(self):
        print("-----BIENVENIDOS-----"
              "\n1 - Menu gestion de razas"
              "\n2 - Menu gestion de Personas"
              "\n3 - Menu gestion de diagnosticos"
              "\n4 - Menu gestion de tratamientos"
              "\n5 - Menu gestion de vacunas"
              )

    def menu(self):
        return input("Ingrese una opcion")

    def getMensaje(self, dato):
        print (dato)

    def mostrarLista(self,lista):
        for i in lista:
            print (i)

    # esta función trae el menu que corresponde a la gestion de personas
    def mostrarMenuPersona(self):
        print("\nMenú de Gestión de Personas")
        print("1- Ver lista personas")
        print("2- Consultar persona")
        print("3- Agregar una persona")
        print("4- Eliminar una persona")
        print("5- Modificar datos de una persona")
        print("6- Volver")
        return input("Seleccione una opción: ")


    def obtenerTipoPersona(self):
        tipo = input("Ingrese el tipo de persona (Veterinario/Propietario): ")
        return tipo.capitalize()




