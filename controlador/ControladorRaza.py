from pathlib import Path
from vista.VistaRaza import VistaRaza
from modelo.Raza import Raza

class ControladorRaza:
    def __init__(self):
        self.vista= VistaRaza()
        self.listaRazas=[]

        base_dir = Path(__file__).resolve().parent.parent
        self.ruta_raza = base_dir / "archivos" / "razas.txt"

    def cargarArchivoRazas(self):   #carga el archivo en una lista, se instancia la clase
        with open(self.ruta_raza) as archivo:
            for linea in archivo.readlines():
                codigo, nombre= linea.strip().split(",")
                self.listaRazas.append(Raza(codigo, nombre))

    def actualizarArchivoRazas(self):
        with open(self.ruta_raza, "w", encoding="utf-8") as archivo:
            for raza in self.listaRazas:
                archivo.write(f"{raza.getCodigo()},{raza.getNombre()}\n")

    def buscarObjeto(self,raza):   #compara un str ingresado con un codigo de un objeto, si lo encuentra devuelve el objeto
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
        with open(self.ruta_raza, 'a', encoding="utf-8") as file:   #al agregar una nueva raza agrega dos variables en una linea
            file.write(f"{codigo}, {nombre}\n")
        self.vista.mostrarMensaje("Raza agregada con éxito.")
        self.actualizarArchivoRazas()

    def modificarRaza(self):   #al modificar el nombre de una raza reescribe los datos en el archivo
        self.listadoRazas()
        raza_actual, nueva_raza= self.vista.modificarRaza()
        raza_modificar= self.buscarObjeto(raza_actual)
        if raza_modificar:
            raza_modificar.setNombre(nueva_raza)
            self.vista.mostrarMensaje("la raza fue modificada con exito")
            self.actualizarArchivoRazas()
        else:
            self.vista.mostrarMensaje("raza no encontrada")

    def eliminarRaza(self):
        self.vista.mostrarLista(self.listaRazas)
        codigo = self.vista.eliminarRaza()
        razaEncontrada = False
        for i in self.listaRazas:
            if str(i.getCodigo()) == codigo:
                self.listaRazas.remove(i)
                self.actualizarArchivoRazas()
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