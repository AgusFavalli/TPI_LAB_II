from vista.VistaGeneral import VistaGeneral
from modelo.Vacuna import Vacuna

class ControladorVacuna:
    def __init__(self):
        self.vista = VistaGeneral()
        self.listaVacunas = []

    def cargarArchivoVacunas(self):
        with open("archivos/vacunas.txt") as archivo:
            for linea in archivo.readlines():
                codigo, nombre, descripcion= linea.strip().split(",")
                self.listaVacunas.append(Vacuna(codigo, nombre, descripcion))


    def buscarObjetoVacuna(self,vacuna):
        for i in self.listaVacunas:
            if i.getCodigo() == vacuna:
                return i.getNombre()

    def listadoVacunas(self):
        self.vista.mostrarLista(self.listaVacunas)