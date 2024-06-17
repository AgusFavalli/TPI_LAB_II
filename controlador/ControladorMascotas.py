from vista.VistaGeneral import VistaGeneral
from modelo.Mascota import Mascota
from controlador.ControladorRaza import ControladorRaza


class ControladorMascotas:
    def __init__(self,controladorRaza, controladorPersonas):
        self.vista= VistaGeneral()
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

    def listadoMascotasActivas(self):  #muestra las mascotas activas (estado=1) y las imprime
        lista=[]
        for i in self.listaMascotas:
            if i.isActivas():
                lista.append(i)
            else:
                pass
        self.vista.mostrarLista(lista)

    def agregarMascota(self):
        codigo = len(self.listaMascotas) + 1
        nombre, especie, raza, propietario = self.vista.obtenerMascota()
        with open('archivos/mascotas.txt', 'a', encoding="utf-8") as file:
            file.write(f"{codigo},{nombre},{especie},{raza},{propietario}\n")
            self.listaMascotas.append(f"{codigo},{nombre},{especie},{raza},{propietario}\n")
        self.vista.getMensaje("Mascota agregada con éxito.")

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
                self.vista.getMensaje("mascota eliminada")
                break
        if not mascotaEncontrada:
            self.vista.getMensaje("mascota no encontrada")

