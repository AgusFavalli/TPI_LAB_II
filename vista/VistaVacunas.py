class VistaVacunas:
    def mostrarMenuVacunas(self):
        print("Menú de Gestión de Vacunas\n"
            "1- Ver lista Vacunas\n"
            "2- Agregar una nueva vacuna\n"
            "3- Modificar vacuna registrada\n"
            "4- Eliminar una vacuna\n"
            "5- Volver\n")
        return input("Seleccione una opción: ")

    def mostrarMensaje(self, dato):
        print (dato)

    def mostrarLista(self, lista):
        for i in lista:
            print(i)

    def obtenerVacuna(self):
        print("ingrese el nombre y descripcion de una nueva vacuna")
        nombre = input("ingrese el nombre: ")
        descripcion = input("ingrese la descripcion: ")
        return nombre, descripcion

    def modificarVacuna(self):
        vieja_vacuna= input("ingrese el codigo de la vacuna actual que desea modificar")
        nueva_vacuna= input("ingrese el nombre nuevo de la vacuna")
        return vieja_vacuna, nueva_vacuna

    def eliminarVacuna(self):
        return input("ingrese el codigo de la vacuna a eliminar")