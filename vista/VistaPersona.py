class VistaPersona:
    def mostrarMenuPersona(self):
        print("\nMenú de Gestión de Personas\n"
              "1- Ver lista personas\n"
              "2- ver lista de veterinarios\n"
              "3- ver lista de propietarios\n"
              "4- Agregar persona\n"
              "5- Modificar datos de una persona\n"
              "6- Eliminar una persona\n"
              "7- Volver al menu principal\n")
        return input("Seleccione una opción: ")

    def opcionPersona(self):
        return input("para veterinario digite 1, para propietario digite 2")

    def obtenerDatosPersona(self):
        nombre = input("Ingrese el nombre: ")
        direccion = input("Ingrese la dirección: ")
        telefono = input("Ingrese el teléfono: ")
        return nombre, direccion, telefono

    def pedirMascota(self):
        return input("ingrese el numero de mascota")

    def mostrarMensaje(self,dato):
        print(dato)

    def mostrarLista(self,lista):
        for i in lista:
            print (i)

    def seleccionarPersona(self):
        return input("ingrese el codigo de la persona a eliminar")

    def modificarPersona(self):
        persona_actual= input("ingrese el codigo de la persona actual que desea modificar")
        nueva_persona= input("ingrese el nombre de la persona nueva")
        return persona_actual,nueva_persona