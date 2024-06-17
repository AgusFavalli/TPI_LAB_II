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

    def agregarRaza(self):
        codigo = len(self.listaRazas) + 1
        nombre= self.vista.obtenerRaza()
        with open('archivos/razas.txt', 'a', encoding="utf-8") as file:
            file.write(f"{codigo},{nombre}\n")
            self.listaRazas.append(f"{codigo},{nombre}\n")
        self.vista.getMensaje("Raza agregada con éxito.")

    def eliminarRaza(self):
        self.vista.mostrarLista(self.listaRazas)
        codigo = self.vista.eliminarRaza()
        razaEncontrada = True
        for i in self.listaRazas:
            if i.getCodigo() == codigo:
                self.listaRazas.remove(i)
                with open("archivos/razas.txt") as file:
                    lineas = file.readlines()
                with open("archivos/razas.txt", "w") as file:
                    for linea in lineas:
                        if linea.startswith(codigo):
                            pass
                        else:
                            file.write(linea)
                self.vista.getMensaje("Raza eliminada")
                break
        if not razaEncontrada:
            self.vista.getMensaje("raza no encontrada")