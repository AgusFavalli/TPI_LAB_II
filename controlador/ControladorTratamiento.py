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

    def agregarTratamiento(self):
        codigo = len(self.listaTratamientos) + 1
        nombre, descripcion = self.vista.obtenerTratamiento()
        with open('archivos/tratamientos.txt', 'a', encoding="utf-8") as file:
            file.write(f"{codigo},{nombre},{descripcion}\n")
            self.listaTratamientos.append(f"{codigo},{nombre},{descripcion}\n")
        self.vista.getMensaje("Tratamiento agregado con éxito.")

    def eliminarTratamiento(self):
        self.vista.mostrarLista(self.listaTratamientos)
        codigo = self.vista.eliminarTratamiento()
        tratamientoEncontrado = True
        for i in self.listaTratamientos:
            if i.getCodigo() == codigo:
                self.listaTratamientos.remove(i)
                with open("archivos/tratamientos.txt") as file:
                    lineas = file.readlines()
                with open("archivos/tratamientos.txt", "w") as file:
                    for linea in lineas:
                        if linea.startswith(codigo):
                            pass
                        else:
                            file.write(linea)
                self.vista.getMensaje("tratamiento eliminado")
                break
        if not tratamientoEncontrado:
            self.vista.getMensaje("vacuna no encontrada")