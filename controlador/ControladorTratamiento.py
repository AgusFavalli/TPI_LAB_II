from vista.VistaTratamiento import VistaTratamiento
from modelo.Tratamiento import Tratamiento

class ControladorTratamiento:
    def __init__(self):
        self.vista = VistaTratamiento()
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
        self.vista.mostrarMensaje("Tratamiento agregado con éxito.")

    def modificarTratamiento(self):
        self.listadoTratamientos()
        tratamiento_actual, nueva_tratamiento= self.vista.modificarTratamiento()
        tratamiento_modificar= self.buscarObjeto(tratamiento_actual)
        if tratamiento_modificar:
            tratamiento_modificar.setNombre(tratamiento_actual)
            self.vista.mostrarMensaje("El tratamiento fue modificado con exito")
            with open('archivos/tratamientos.txt', 'w', encoding="utf-8") as file:
                for tratamiento in self.listaTratamientos:
                    file.write(f"{tratamiento.getCodigo()},{tratamiento.getNombre()},{tratamiento.getDescripcion()}\n")

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
                self.vista.mostrarMensaje("tratamiento eliminado")
                break
        if not tratamientoEncontrado:
            self.vista.mostrarMensaje("vacuna no encontrada")

    def buscarObjeto(self,tratamiento):
        for i in self.listaTratamientos:
            if i.getCodigo() == tratamiento:
                return i

    def ejecutarMenuTratamientos(self):
        opcion = self.vista.mostrarMenuTratamiento()
        while True:
            if opcion == "1":  # 1- mostrar listado de tratamientos
                self.listadoTratamientos()
            elif opcion == "2":  # 2- agregar tratamiento
                self.agregarTratamiento()
            elif opcion == "3":  # 3- modificar tratamientos registradas
                self.modificarTratamiento()
            elif opcion == "4":  # 4- eliminar tratamientos
                self.eliminarTratamiento()
            elif opcion == "5":  # 5- salir
                self.vista.mostrarMensaje("Volviendo al menu principal...")
                break
            else:
                print("Opción inválida. Por favor, intente nuevamente.\n")
            opcion = self.vista.mostrarMenuTratamiento()