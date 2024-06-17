from vista.VistaRaza import VistaRaza
from modelo.Raza import Raza


class ControladorRaza:
    def __init__(self):
        self.vista= VistaRaza()
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
        self.vista.mostrarMensaje("Raza agregada con éxito.")

    def modificarRaza(self):

        nueva_raza= self.vista.modificarRaza()
        raza_modificar= self.buscarObjeto(raza)
        raza_modificar.setNombre(nueva_raza)
        self.vista.mostrarMensaje("la raza fue modificada con exito")

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
                self.vista.mostrarMensaje("Raza eliminada")
                break
        if not razaEncontrada:
            self.vista.mostrarMensaje("raza no encontrada")

    def ejecutarMenuRazas(self):
        opcion = self.vista.mostrarMenuPersona()
        while True:
            if opcion == "1":  # 1- Dar de alta nuevas razas
                self.agregarRaza()
            elif opcion == "2":  # 2- modificar razas registradas
                self.modificarRaza()
            elif opcion == "3":  # 3- eliminar razas
                self.eliminarRaza()
            elif opcion == "4":  # 4- mostrar listado de razas
                self.listadoRazas()
            elif opcion == "5":  # 5- salir
                break
            else:
                print("Opción inválida. Por favor, intente nuevamente.\n")