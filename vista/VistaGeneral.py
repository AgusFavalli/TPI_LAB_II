import os

class VistaGeneral:
    def bienvenida(self):
        print("-----BIENVENIDOS-----"
              "\n1 - Menu gestion de razas"
              "\n2 - Menu gestion de Personas"
              "\n3 - Menu gestion de diagnosticos"
              "\n4 - Menu gestion de tratamientos"
              "\n5 - Menu gestion de vacunas"
              "\n- - -"
              "\n8 - Menu de fichas médicas"                            
              )

    def menu(self):
        return input("Ingrese una opcion: ")

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


    def obtenerTratamiento(self):
        print("ingrese el nombre y descripcion de un nuevo tratamiento")
        nombre = input("ingrese el nombre: ")
        descripcion = input("ingrese la descripcion: ")
        return nombre, descripcion

    def eliminarTratamiento(self):
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

#funciones Extras
#Dependiendo del SO, cls limpia la pantalla en windows
    def limpiarPantalla(self):
      os.system("cls" if os.name == "nt" else "clear")  

#La funcion getch() del modulo msvcrt espera el ingreso de una tecla sin retornarla. En linux se configura la terminal en modo RAW y leer un caracter con la funcion sys.stdin.read(1)
def waitKey():
    if os.name == "nt": #Para Windows
        import msvcrt
        msvcrt.getch()