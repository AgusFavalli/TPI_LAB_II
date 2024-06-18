class VistaDiagnostico:
    def mostrarMenuDiagnosticos(self):
        print("Menú de Gestión de Diagnosticos\n"
              "1- Ver lista diagnosticos\n"
              "2- Agregar un nuevo diagnostico\n"
              "3- Modificar diagnostico\n"
              "4- Eliminar un diagnostico\n"
              "5- Volver\n")
        return input("Seleccione una opción: ")

    def mostrarLista(self, lista):
        for i in lista:
            print(i)

    def obtenerDiagnostico(self):
        print("ingrese la descripcion de un nuevo diagnostico, su tratamiento y una vacuna")
        descripcion= input("ingrese la descripcion: ")
        tratamiento = input("ingrese el tratamiento: ")
        vacuna= input("ingrese la vacuna: ")
        return descripcion, tratamiento, vacuna

    def mostrarMensaje(self, dato):
        print (dato)

    def eliminarDiagnostico(self):
        return input("ingrese el codigo del diagnostico a eliminar")

    def modificarDiagnostico(self):
        viejo_diagnostico= input("ingrese el codigo del diagnostico actual que desea modificar")
        nuevo_diagnostico= input("ingrese el nombre del nombre modificado del diagnostico")
        return viejo_diagnostico, nuevo_diagnostico