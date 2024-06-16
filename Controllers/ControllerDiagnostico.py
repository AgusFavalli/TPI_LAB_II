from Views.VistaDiagnostico import VistaDiagnostico
from Models.Diagnostico import Diagnostico

class ControllerDiagnostico:
    def __init__(self, vista = VistaDiagnostico()):
        self.vista = vista
        self.listaDiagnosticos = []
        self.mascotas = {}
        self.cargarMascotas()
        self.cargarArchivos()

    def cargarMascotas(self):
        """Carga las mascotas desde el archivo mascotas.txt"""
        with open("Scripts/mascotas.txt") as file:
            lineas = file.readlines()
        for l in lineas:
            codigo, nombre, especie, raza, propietario = l.strip().split(";")
            self.mascotas[codigo] = {"nombre": nombre, "especie": especie, "raza": raza, "propietario": propietario}

    def cargarArchivos(self):
        """Carga los diagnósticos desde el archivo diagnosticos.txt"""
        with open("Scripts/diagnosticos.txt", "r+") as file:
            lineas = file.readlines()
        for l in lineas:
            codigo, nombre, observaciones, mascota = l.strip().split(";")
            mascota = self.mascotas.get(mascota, None)
            if mascota:
                self.listaDiagnosticos.append(Diagnostico(codigo, nombre, observaciones, mascota))

    def darAltaDiagnostico(self, codigo, nombre, observaciones, mascota):
        """Agrega un nuevo diagnóstico a la lista y al archivo"""
        mascota = self.mascotas.get(mascota, None)
        if mascota:
            nuevoDiagnostico = Diagnostico(codigo, nombre, observaciones, mascota)
            self.listaDiagnosticos.append(nuevoDiagnostico)
            with open("Scripts/diagnosticos.txt", "a") as file:
                file.write(f"{codigo};{nombre};{observaciones};{mascota}\n")
            print("Diagnóstico agregado correctamente.")
        else:
            print("Código de mascota no encontrado.")

    def modificarDiagnostico(self, codigo, nombre=None, observaciones=None):
        """Modifica un diagnóstico existente en la lista y en el archivo"""
        for diag in self.listaDiagnosticos:
            if diag.codigo == codigo:
                if nombre:
                    diag.nombre = nombre
                if observaciones:
                    diag.observaciones = observaciones
                self.guardarDiagnosticos()
                print("Diagnóstico modificado correctamente.")
                return
        print("Diagnóstico no encontrado.")

    def eliminarDiagnostico(self, codigo):
        """Elimina un diagnóstico de la lista y del archivo"""
        self.listaDiagnosticos = [diag for diag in self.listaDiagnosticos if diag.codigo != codigo]
        self.guardarDiagnosticos()
        print("Diagnóstico eliminado correctamente.")

    def guardarDiagnosticos(self):
        """Guarda los diagnósticos actuales en el archivo diagnosticos.txt"""
        with open("Scripts/diagnosticos.txt", "w") as file:
            for diag in self.listaDiagnosticos:
                file.write(f"{diag.codigo};{diag.nombre};{diag.observaciones};{diag.mascota['codigo']}\n")

#ejecutar submenu de Diagnosticos
    def ejecutarMenuDiagnostico(self):
         #valor = VistaDiagnostico.mostrarMenu()
      while True:
            VistaDiagnostico.mostrarMenu()
            opcion = input("Ingrese una opción: ")
            
            if opcion == "1":
                  codigo = input("Ingrese el código del diagnóstico: ")
                  nombre = input("Ingrese el nombre del diagnóstico: ")
                  observaciones = input("Ingrese las observaciones del diagnóstico: ")
                  mascota = input("Ingrese el código de la mascota: ")
                  self.darAltaDiagnostico(codigo, nombre, observaciones, mascota)
            
            elif opcion == "2":
                  codigo = input("Ingrese el código del diagnóstico a modificar: ")
                  nombre = input("Ingrese el nuevo nombre del diagnóstico (dejar en blanco para no modificar): ")
                  observaciones = input("Ingrese las nuevas observaciones del diagnóstico (dejar en blanco para no modificar): ")
                  self.modificarDiagnostico(codigo, nombre if nombre else None, observaciones if observaciones else None)
            
            elif opcion == "3":
                  codigo = input("Ingrese el código del diagnóstico a eliminar: ")
                  self.eliminarDiagnostico(codigo)
            
            elif opcion == "4":
                  break
            
            else:
                  print("Opción no válida. Intente nuevamente.")