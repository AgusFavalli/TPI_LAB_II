from Models.Vacuna import Vacuna
from Views.VistaVacuna import VistaVacuna

class ControllerVacuna:
    def __init__(self, vista = VistaVacuna()):
        self.vista = VistaVacuna
        self.listaVacunas = []
        self.cargarArchivos()

    def cargarArchivos(self):
        # Cargar los datos de vacunas desde el archivo vacunas.txt
        with open("Scripts/vacunas.txt") as file:
            lineas = file.readlines()
        for l in lineas:
            codigo, nombre, fabricante, observaciones = l.strip().split(";")
            self.listaVacunas.append(Vacuna(codigo, nombre, fabricante, observaciones))

    def guardarArchivos(self):
        # Guardar los datos de vacunas en el archivo vacunas.txt
        with open("Scripts/vacunas.txt", "w") as file:
            for vacuna in self.listaVacunas:
                file.write(str(vacuna) + "\n")

    def darAltaNuevaVacuna(self, codigo, nombre, fabricante, observaciones):
        # Agregar una nueva vacuna a la lista y guardar en archivo
        nuevaVacuna = Vacuna(codigo, nombre, fabricante, observaciones)
        self.listaVacunas.append(nuevaVacuna)
        self.guardarArchivos()

    def modificarVacuna(self, codigo, nuevoNombre, nuevoFabricante, nuevasObservaciones):
        # Modificar una vacuna existente
        for vacuna in self.listaVacunas:
            if vacuna.codigoVacuna == codigo:
                vacuna.nombre = nuevoNombre
                vacuna.fabricante = nuevoFabricante
                vacuna.observaciones = nuevasObservaciones
                self.guardarArchivos()
                return True
        return False

    def eliminarVacuna(self, codigo):
        # Eliminar una vacuna de la lista y guardar en archivo
        self.listaVacunas = [vacuna for vacuna in self.listaVacunas if vacuna.codigoVacuna != codigo]
        self.guardarArchivos()

    def ejecutarMenuVacuna(self):
        while True:
            VistaVacuna.mostrarMenuVacuna()
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                codigo = input("Ingrese el código de la vacuna: ")
                nombre = input("Ingrese el nombre de la vacuna: ")
                fabricante = input("Ingrese el fabricante de la vacuna: ")
                observaciones = input("Ingrese observaciones: ")
                self.darAltaNuevaVacuna(codigo, nombre, fabricante, observaciones)
            elif opcion == "2":
                codigo = input("Ingrese el código de la vacuna a modificar: ")
                nuevoNombre = input("Ingrese el nuevo nombre: ")
                nuevoFabricante = input("Ingrese el nuevo fabricante: ")
                nuevasObservaciones = input("Ingrese las nuevas observaciones: ")
                if not self.modificarVacuna(codigo, nuevoNombre, nuevoFabricante, nuevasObservaciones):
                    print("Vacuna no encontrada.")
            elif opcion == "3":
                codigo = input("Ingrese el código de la vacuna a eliminar: ")
                self.eliminarVacuna(codigo)
            elif opcion == "4":
                break
            else:
                print("Opción no válida. Intente de nuevo.")

