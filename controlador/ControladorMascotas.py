from Prueba_repositorio.vista.VistaMascotas import VistaMascotas
from Prueba_repositorio.modelo.Mascotas import Mascota
from Prueba_repositorio.modelo.Razas import Raza

class ControladorMascotas:
    def __init__(self):
        self.vista= VistaMascotas()
        self.modelo= Mascota()
        self.listaMascotas=[]
        self.razas = []

    def menu(self):
        self.vista.bienvenida()
        opcion= self.vista.menu()
        while True:
            if opcion == "1":
                self.listadoMascotasActivas()
            elif opcion == "2":
                pass
            elif opcion == "3":
                pass
            elif opcion == "4":
                pass
            else:
                self.vista.getMensaje("La opcion indicada no es valida")

    def cargarArchivoMascotas(self):
        with open("mascotas.txt") as file:
            renglones= file.readlines()
            for line in renglones:
                nombre, edad, fechaNac, estado= line.strip(",")
                self.listaMascotas = Mascota(nombre, edad, fechaNac,estado)

    def listadoMascotasActivas(self):  #muestra las mascotas activas (estado=1) y las imprime
        lista=[]
        for mascota in self.listaMascotas:
            if mascota.isActivas():
                lista.append(mascota)
            self.vista.mostrarLista(lista)


    def registrarRaza(self):
