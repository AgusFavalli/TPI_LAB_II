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

    def seleccionarPersona(self):
        return input("ingrese el codigo de la persona a eliminar")

    def obtenerTipoPersona(self):
        tipo = input("Ingrese el tipo de persona (Veterinario/Propietario): ")
        return tipo.capitalize()

    def obtenerDatosPersona(self):
        codigo = input("Ingrese el codigo: ")
        nombre = input("Ingrese el nombre: ")
        direccion = input("Ingrese la dirección: ")
        telefono = input("Ingrese el teléfono: ")
        return codigo, nombre, direccion, telefono

    def pedirMascota(self):
        return input("ingrese el numero de mascota")


    def opcionPersona(self):
        return input("desea agregar veterinario digite 1, si desea agregar propietario digite 2")

    def obtenerDiagnostico(self):
        print("ingrese la descripcion de un nuevo diagnostico, su tratamiento y una vacuna")
        descripcion= input("ingrese la descripcion: ")
        tratamiento = input("ingrese el tratamiento: ")
        vacuna= input("ingrese la vacuna: ")
        return descripcion, tratamiento, vacuna

    def eliminarDiagnostico(self):
        return input("ingrese el codigo del diagnostico a eliminar")

    def obtenerVacuna(self):
        print("ingrese el nombre y descripcion de una nueva vacuna")
        nombre = input("ingrese el nombre: ")
        descripcion = input("ingrese la descripcion: ")
        return nombre, descripcion

    def eliminarVacuna(self):
        return input("ingrese el codigo de la vacuna a eliminar")

    def obtenerRaza(self):
        return input("ingrese el nombre de la raza")

    def eliminarRaza(self):
        return input("ingrese el codigo de la raza a eliminar")

    def obtenerTratamiento(self):
        print("ingrese el nombre y descripcion de un nuevo tratamiento")
        nombre = input("ingrese el nombre: ")
        descripcion = input("ingrese la descripcion: ")
        return nombre, descripcion

    def eliminarTratamiento
        return input("ingrese el codigo del tratamiento a eliminar")

    def obtenerMascota(self):
        print("ingrese el nombre, la especie, la raza de la mascota y el nombre del propietario")
        nombre = input("ingrese el nombre: ")
        especie = input("ingrese la especie: ")
        raza = input("ingrese la raza: ")
        propietario = input("ingrese el propietario")
        return nombre, especie, raza, propietario

    def eliminarMascota(self):
        return input("ingrese el codigo de la mascota a eliminar")