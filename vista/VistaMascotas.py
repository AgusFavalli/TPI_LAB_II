class VistaMascotas:
    def mostrarMenuMascotas(self):
        print("Menú de Gestión de Mascotas\n"
              "1- Ver lista mascotas\n"
              "2- Agregar una nueva mascota\n"
              "3- Modificar mascota registrada\n"
              "4- Eliminar una mascota\n"
              "5- Volver\n")
        return input("Seleccione una opción: ")

    def mostrarMensaje(self, dato):
        print (dato)

    def mostrarLista(self, lista):
        for i in lista:
            print(i)

    def obtenerMascota(self):
        print("ingrese el nombre, la especie, la raza de la mascota y el nombre del propietario")
        nombre = input("ingrese el nombre: ")
        especie = input("ingrese la especie: ")
        raza = input("ingrese la raza: ")
        propietario = input("ingrese el propietario")
        return nombre, especie, raza, propietario

    def eliminarMascota(self):
        return input("ingrese el codigo de la mascota a eliminar")

    def modificarMascota(self):
        vieja_mascota= input("ingrese el codigo de la mascota actual que desea modificar")
        nueva_mascota= input("ingrese el nombre nuevo de la mascota")
        return vieja_mascota,nueva_mascota
