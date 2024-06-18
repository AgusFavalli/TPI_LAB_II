from vista.VistaVacunas import VistaVacunas
from modelo.Vacuna import Vacuna

class ControladorVacuna:
    def __init__(self):
        self.vista = VistaVacunas()
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

    def buscarObjeto(self,vacuna):
        for i in self.listaVacunas:
            if i.getCodigo() == vacuna:
                return i

    def agregarVacuna(self):
        codigo = len(self.listaVacunas) + 1
        nombre, descripcion = self.vista.obtenerVacuna()
        with open('archivos/vacunas.txt', 'a', encoding="utf-8") as file:
            file.write(f"{codigo},{nombre},{descripcion}\n")
            self.listaVacunas.append(f"{codigo},{nombre},{descripcion}\n")
        self.vista.mostrarMensaje("Vacuna agregada con éxito.")

    def modificarVacuna(self):
        self.listadoVacunas()
        vacuna_actual, nueva_vacuna= self.vista.modificarVacuna()
        vacuna_modificar= self.buscarObjeto(vacuna_actual)
        if vacuna_modificar:
            vacuna_modificar.setNombre(vacuna_actual)
            self.vista.mostrarMensaje("La vacuna fue modificada con exito")
            with open('archivos/vacunas.txt', 'w', encoding="utf-8") as file:
                for vacuna in self.listaVacunas:
                    file.write(f"{vacuna.getCodigo()},{vacuna.getNombre()},{vacuna.getDescripcion()}\n")

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
                self.vista.mostrarMensaje("vacuna eliminada")
                break
        if not vacunaEncontrada:
            self.vista.mostrarMensaje("vacuna no encontrada")

    def ejecutarMenuVacunas(self):
        opcion = self.vista.mostrarMenuVacunas()
        while True:
            if opcion == "1":  # 1- mostrar listado de vacunas
                self.listadoVacunas()
            elif opcion == "2":  # 2- agregar vacuna
                self.agregarVacuna()
            elif opcion == "3":  # 3- modificar vacuna registradas
                self.modificarVacuna()
            elif opcion == "4":  # 4- eliminar vacuna
                self.eliminarVacuna()
            elif opcion == "5":  # 5- salir
                self.vista.mostrarMensaje("Volviendo al menu principal...")
                break
            else:
                print("Opción inválida. Por favor, intente nuevamente.\n")
            opcion = self.vista.mostrarMenuVacunas()