class VistaTratamiento:
    def mostrarMenuTratamiento(self):
        print("\nMenú de Gestión de Tratamientos\n"
              "1- Ver lista tratamientos\n"
              "2- Agregar un nuevo tratamiento\n"
              "3- Modificar tratamiento registrado\n"
              "4- Eliminar un tratamiento\n"
              "5- Volver\n")
        return input("Seleccione una opción: ")

    def mostrarMensaje(self, dato):
        print (dato)

    def mostrarLista(self, lista):
        for i in lista:
            print(i)

    def obtenerTratamiento(self):
        print("ingrese el nombre y descripcion de un nuevo tratamiento")
        nombre = input("ingrese el nombre: ")
        descripcion = input("ingrese la descripcion: ")
        return nombre, descripcion

    def eliminarTratamiento(self):
        return input("ingrese el codigo del tratamiento a eliminar")

    def modificarTratamiento(self):
        viejo_tratamiento= input("ingrese el codigo del tratamiento actual que desea modificar")
        nuevo_tratamiento= input("ingrese el nuevo nombre del tratamiento")
        return viejo_tratamiento, nuevo_tratamiento