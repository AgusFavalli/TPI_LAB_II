from vista.VistaGeneral import VistaGeneral
from modelo.Tratamiento import Tratamiento

class ControladorTratamiento:
    def __init__(self):
        self.vista = VistaGeneral()
        self.listaTratamientos = []

    def cargarArchivoTratamientos(self):
        with open("archivos/tratamientos.txt", encoding="utf-8") as archivo:
            for linea in archivo.readlines():
                codigo, nombre, descripcion= linea.strip().split(",")
                self.listaTratamientos.append(Tratamiento(codigo, nombre, descripcion))


    def buscarObjetoTratamiento(self,tratamiento):
        for i in self.listaTratamientos:
            if i.getCodigo() == tratamiento:
                return i.getDatosTratamiento()

    def listadoTratamientos(self):
        self.vista.mostrarLista(self.listaTratamientos)
