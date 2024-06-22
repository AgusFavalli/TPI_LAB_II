from vista.VistaMascotas import VistaMascotas
from modelo.Mascota import Mascota
from controlador.ControladorRaza import ControladorRaza


class ControladorMascotas:
    def __init__(self,controladorRaza, controladorPersonas):
        self.vista= VistaMascotas()
        self.listaMascotas=[]
        self.controladorRaza= controladorRaza
        self.controladorPersonas= controladorPersonas

    def cargarArchivoMascotas(self):
        with open("archivos/mascotas.txt") as archivo:
            for linea in archivo.readlines():
                codigo, nombre, especie, raza, propietario= linea.strip().split(",")
                objRaza= self.controladorRaza.buscarObjeto(raza)
                objPropietario = self.controladorPersonas.buscarObjetoPropietario(propietario)
                self.listaMascotas.append(Mascota(codigo, nombre, especie, objRaza, objPropietario))

    def listadoMascotas(self):
        self.vista.mostrarLista(self.listaMascotas)

    def listadoMascotasActivas(self):  #muestra las mascotas activas (estado=1) y las imprime
        lista=[]
        for i in self.listaMascotas:
            if i.isActivas():
                lista.append(i)
            else:
                pass
        self.vista.mostrarLista(lista)

    def buscarObjeto(self,mascota):
        for i in self.listaMascotas:
            if i.getCodigo() == mascota:
                return i

    def agregarMascota(self):
        codigo = len(self.listaMascotas) + 1
        nombre, especie, raza, propietario = self.vista.obtenerMascota()
        with open('archivos/mascotas.txt', 'a', encoding="utf-8") as file:
            file.write(f"{codigo},{nombre},{especie},{raza},{propietario}\n")
            self.listaMascotas.append(f"{codigo},{nombre},{especie},{raza},{propietario}\n")
        self.vista.mostrarMensaje("Mascota agregada con éxito.")

    def modificarMascota(self):
        self.listadoMascotas()
        mascota_actual, nueva_mascota= self.vista.modificarMascota()
        mascota_modificar= self.buscarObjeto(mascota_actual)
        if mascota_modificar:
            mascota_modificar.setNombre(mascota_actual)
            self.vista.mostrarMensaje("La mascota fue modificada con exito")
            with open('archivos/mascota.txt', 'w', encoding="utf-8") as file:
                for mascota in self.listaMascotas:
                    file.write(f"{mascota.getCodigo()},{mascota.getNombre()},{mascota.getEspecie()},{mascota.getRaza()},{mascota.getPropietario()}\n")

    def eliminarMascota(self):
        self.vista.mostrarLista(self.listaMascotas)
        codigo = self.vista.eliminarMascota()
        mascotaEncontrada = True
        for i in self.listaMascotas:
            if i.getCodigo() == codigo:
                self.listaMascotas.remove(i)
                with open("archivos/mascotas.txt") as file:
                    lineas = file.readlines()
                with open("archivos/mascotas.txt", "w") as file:
                    for linea in lineas:
                        if linea.startswith(codigo):
                            pass
                        else:
                            file.write(linea)
                self.vista.mostrarMensaje("mascota eliminada")
                break
        if not mascotaEncontrada:
            self.vista.mostrarMensaje("mascota no encontrada")

    def ejecutarMenuMascotas(self):
        opcion = self.vista.mostrarMenuMascotas()
        while True:
            if opcion == "1":  # 1- Ver lista mascotas
                self.vista.mostrarLista(self.listaMascotas)
            elif opcion == "2":  # 2- agregar mascota
                self.agregarMascota()
            elif opcion == "3":  # 3- modificar mascota registrada
                self.modificarMascota()
            elif opcion == "4":  # 4- eliminar mascota
                self.eliminarMascota()
            elif opcion == "5":  # 5- salir
                self.vista.mostrarMensaje("Volviendo al menu principal...")
                break
            else:
                print("Opción inválida. Por favor, intente nuevamente.\n")
            opcion = self.vista.mostrarMenuMascotas()

