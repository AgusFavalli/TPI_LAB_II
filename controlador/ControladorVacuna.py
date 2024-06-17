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

    def agregarVacuna(self):
        codigo = len(self.listaVacunas) + 1
        nombre, descripcion = self.vista.obtenerVacuna()
        with open('archivos/vacunas.txt', 'a', encoding="utf-8") as file:
            file.write(f"{codigo},{nombre},{descripcion}\n")
            self.listaVacunas.append(f"{codigo},{nombre},{descripcion}\n")
        self.vista.getMensaje("Vacuna agregada con éxito.")

    def eliminarVacuna(self):
        self.vista.mostrarLista(self.listaVacunas)
        codigo = self.vista.eliminarVacuna()
        vacunaEncontrada = True
        for i in self.listaVacunas:
            if i.getCodigo() == codigo:
                self.listaVacunas.remove(i)
                with open("archivos/vacunas.txt") as file:
                    lineas = file.readlines()
                with open("archivos/vacunas.txt", "w") as file:
                    for linea in lineas:
                        if linea.startswith(codigo):
                            pass
                        else:
                            file.write(linea)
                self.vista.getMensaje("vacuna eliminada")
                break
        if not vacunaEncontrada:
            self.vista.getMensaje("vacuna no encontrada")