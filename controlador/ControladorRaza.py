from vista.VistaGeneral import VistaGeneral
from modelo.Raza import Raza


class ControladorRaza:
    def __init__(self):
        self.vista= VistaGeneral()
        self.listaRazas=[]

    def cargarArchivoRazas(self):
        with open("archivos/razas.txt") as archivo:
            for linea in archivo.readlines():
                codigo, nombre= linea.strip().split(",")
                self.listaRazas.append(Raza(codigo, nombre))

    def buscarObjeto(self,raza):
        for i in self.listaRazas:
            if i.getCodigo() == raza:
                return i

    def listadoRazas(self):
        self.vista.mostrarLista(self.listaRazas)