from vista.VistaGeneral import VistaGeneral
from modelo.Mascota import Mascota
from controlador.ControladorRaza import ControladorRaza


class ControladorMascotas:
    def __init__(self,controladorRaza, controladorPropietario):
        self.vista= VistaGeneral()
        self.listaMascotas=[]
        self.controladorRaza= controladorRaza
        self.controladorPropietario= controladorPropietario

    def cargarArchivoMascotas(self):
        with open("archivos/mascotas.txt") as archivo:
            for linea in archivo.readlines():
                codigo, nombre, especie, raza, propietario= linea.strip().split(",")
                objRaza= self.controladorRaza.buscarObjeto(raza)
                objPropietario = self.controladorPropietario.buscarObjeto(propietario)
                self.listaMascotas.append(Mascota(codigo, nombre, especie, objRaza, objPropietario))

    def listadoMascotasActivas(self):  #muestra las mascotas activas (estado=1) y las imprime
        lista=[]
        for i in self.listaMascotas:
            if i.isActivas():
                lista.append(i)
            else:
                pass
        self.vista.mostrarLista(lista)


