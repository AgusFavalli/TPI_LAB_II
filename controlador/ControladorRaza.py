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
            if str(i.getCodigo()) == raza:
                return i

    def listadoRazas(self):
        self.vista.mostrarLista(self.listaRazas)

    def agregarRaza(self):
        codigo = len(self.listaRazas) + 1
        nombre= self.vista.obtenerRaza()
        nuevaRaza= Raza(codigo, nombre)
        self.listaRazas.append(nuevaRaza)
        with open('archivos/razas.txt', 'a', encoding="utf-8") as file:
            file.write(f"{codigo}, {nombre}\n")
        self.vista.mostrarMensaje("Raza agregada con éxito.")

    def modificarRaza(self):
        self.listadoRazas()
        raza_actual, nueva_raza= self.vista.modificarRaza()
        raza_modificar= self.buscarObjeto(raza_actual)
        if raza_modificar:
            raza_modificar.setNombre(nueva_raza)
            self.vista.mostrarMensaje("la raza fue modificada con exito")
            with open('archivos/razas.txt', 'w', encoding="utf-8") as file:
                for raza in self.listaRazas:
                    file.write(f"{raza.getCodigo()},{raza.getNombre()}\n")

    def eliminarRaza(self):
        self.vista.mostrarLista(self.listaRazas)
        codigo = self.vista.eliminarRaza()
        razaEncontrada = False
        for i in self.listaRazas:
            if str(i.getCodigo()) == codigo:
                self.listaRazas.remove(i)
                with open("archivos/razas.txt", "w+") as file:
                    for linea in self.listaRazas:
                        file.write(f"{linea.getCodigo()},{linea.getNombre()}\n")
                self.vista.mostrarMensaje("Raza eliminada")
                razaEncontrada=True
                break
            else:
                self.vista.mostrarMensaje("Raza no encontrada")

    def ejecutarMenuRazas(self):
        opcion = self.vista.mostrarMenuPersona()
        while True:
            if opcion == "1":  # 1- mostrar listado de razas
                self.listadoRazas()
            elif opcion == "2":  # 2- agregar raza
                self.agregarRaza()
            elif opcion == "3":  # 3- modificar razas registradas
                self.modificarRaza()
            elif opcion == "4":  # 4- eliminar razas
                self.eliminarRaza()
            elif opcion == "5":  # 5- salir
                self.vista.mostrarMensaje("Volviendo al menu principal...")
                return
            else:
                print("Opción inválida. Por favor, intente nuevamente.")
            opcion = self.vista.mostrarMenuPersona()