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

    def actualizarArchivoTratamientos(self):
        with open("archivos/tratamientos.txt", "w", encoding="utf-8") as archivo:
            for tratamiento in self.listaTratamientos:
                archivo.write(f"{tratamiento.getCodigo()}, {tratamiento.getNombre()}, {tratamiento.getDescripcion()}\n")

    def buscarObjetoTratamiento(self,tratamiento):
        for i in self.listaTratamientos:
            if str(i.getCodigo()) == tratamiento:
                return i.getDatosTratamiento()

    def buscarNombreTratamiento(self,nombre):
        for i in self.listaTratamientos:
            if str(i.getNombre) == nombre:
                return i.getCodigo()
        return None

    def listadoTratamientos(self):
        self.vista.mostrarLista(self.listaTratamientos)

    def agregarTratamiento(self):
        codigo = len(self.listaTratamientos) + 1
        nombre, descripcion = self.vista.obtenerTratamiento()
        nuevoTratamiento= Tratamiento(codigo, nombre, descripcion)
        self.listaTratamientos.append(nuevoTratamiento)
        with open('archivos/tratamientos.txt', 'a', encoding="utf-8") as file:
            file.write(f"\n{codigo}, {nombre}, {descripcion}")
        self.vista.mostrarMensaje("Tratamiento agregado con éxito.")
        self.actualizarArchivoTratamientos()

    def modificarTratamiento(self):
        self.listadoTratamientos()
        tratamiento_actual, nueva_tratamiento= self.vista.modificarTratamiento()
        tratamiento_modificar= self.buscarObjeto(tratamiento_actual)
        if tratamiento_modificar:
            tratamiento_modificar.setNombre(nueva_tratamiento)
            self.vista.mostrarMensaje("El tratamiento fue modificado con exito")
            self.actualizarArchivoTratamientos()
        else:
            self.vista.mostrarMensaje("tratamiento no encontrado")

    def eliminarTratamiento(self):
        self.vista.mostrarLista(self.listaTratamientos)
        codigo = self.vista.eliminarTratamiento()
        tratamientoEncontrado = False
        for i in self.listaTratamientos:
            if str(i.getCodigo()) == codigo:
                self.listaTratamientos.remove(i)
                self.actualizarArchivoTratamientos()
                self.vista.mostrarMensaje("tratamiento eliminado")
                tratamientoEncontrado= True
                break
        else:
            self.vista.mostrarMensaje("tratamiento no encontrado")


    def buscarObjeto(self,tratamiento):
        for i in self.listaTratamientos:
            if str(i.getCodigo()) == tratamiento:
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
            elif opcion == "5":  # 5- cantidad de tratamientos
                self.cantidadTratamientos()
            elif opcion == "6":  # 6- salir
                self.vista.mostrarMensaje("Volviendo al menu principal...")
                return
            else:
                print("Opción inválida. Por favor, intente nuevamente.\n")
            opcion = self.vista.mostrarMenuTratamiento()

    def cantidadTratamientos(self): #CANTIDAD TRATAMIENTOS
        cantidad = len(self.listaTratamientos)
        self.vista.mostrarMensaje(f"La cantidad de tratamientos aplicados es: {cantidad}")