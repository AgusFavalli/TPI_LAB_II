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

    def actualizarArchivoVacunas(self):
        with open("archivos/vacunas.txt", "w", encoding="utf-8") as archivo:
            for vacuna in self.listaVacunas:
                archivo.write(f"{vacuna.getCodigo()},{vacuna.getNombre()},{vacuna.getDescripcion()}\n")

    def listadoVacunas(self):
        self.vista.mostrarLista(self.listaVacunas)

    def buscarObjeto(self,vacuna):
        for i in self.listaVacunas:
            if str(i.getCodigo()) == vacuna:
                return i.getDatosVacunas()
        return None

    def buscarNombreVacuna(self,nombre):
        for i in self.listaVacunas:
            if str(i.getNombre) == nombre:
                return i.getCodigo
        return None

    def agregarVacuna(self):
        codigo = len(self.listaVacunas) + 1
        nombre, descripcion = self.vista.obtenerVacuna()
        nuevaVacuna= Vacuna(codigo,nombre,descripcion)
        self.listaVacunas.append(nuevaVacuna)
        with open('archivos/vacunas.txt', 'a', encoding="utf-8") as file:
            file.write(f"{codigo}, {nombre}, {descripcion}\n")
        self.vista.mostrarMensaje("Vacuna agregada con éxito.")
        self.actualizarArchivoVacunas()

    def modificarVacuna(self):
        self.listadoVacunas()
        vacuna_actual, nueva_vacuna= self.vista.modificarVacuna()
        vacuna_modificar= self.buscarObjeto(vacuna_actual)
        if vacuna_modificar:
            vacuna_modificar.setNombre(nueva_vacuna)
            self.vista.mostrarMensaje("La vacuna fue modificada con exito")
            self.actualizarArchivoVacunas()
        else:
            self.vista.mostrarMensaje("vacuna no encontrada")

    def eliminarVacuna(self):
        self.vista.mostrarLista(self.listaVacunas)
        codigo = self.vista.eliminarVacuna()
        vacunaEncontrada = False
        for i in self.listaVacunas:
            if str(i.getCodigo()) == codigo:
                self.listaVacunas.remove(i)
                self.actualizarArchivoVacunas()
                self.vista.mostrarMensaje("vacuna eliminada")
                vacunaEncontrada= True
                break
        else:
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
                return
            else:
                print("Opción inválida. Por favor, intente nuevamente.")
            opcion = self.vista.mostrarMenuVacunas()