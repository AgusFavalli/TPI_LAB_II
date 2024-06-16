from Models.Tratamiento import Tratamiento
from Views.VistaTratamiento import VistaTratamiento

class ControllerTratamiento:
   def __init__(self, vista = VistaTratamiento()):
      self.vista = vista
      self.listaTratamientos = []
      self.cargarArchivos()

   def cargarArchivos(self):
        with open("Scripts/tratamientos.txt") as file:
            lineas = file.readlines()
        for l in lineas:
            codigo, nombre, observaciones = l.strip().split(";")
            self.listaTratamientos.append(Tratamiento(codigo, nombre, observaciones))

   def darAltaTratamiento(self, codigo, nombre, observaciones):
        # Agregar nuevo tratamiento
        nuevo_tratamiento = Tratamiento(codigo, nombre, observaciones)
        self.listaTratamientos.append(nuevo_tratamiento)
        self.guardarArchivos()

   def modificarTratamiento(self, codigo, nombre, observaciones):
        # Modificar tratamiento existente
        for tratamiento in self.listaTratamientos:
            if tratamiento.codigo == codigo:
                tratamiento.nombre = nombre
                tratamiento.observaciones = observaciones
                self.guardarArchivos()
                return
        print("Tratamiento no encontrado")

   def listarTratamientos(self):
        # Listar todos los tratamientos
        for tratamiento in self.listaTratamientos:
            print(f"Código: {tratamiento.codigo}, Nombre: {tratamiento.nombre}, Observaciones: {tratamiento.observaciones}")

   def guardarArchivos(self):
        # Guardar los cambios en el archivo
        with open("Scripts/tratamientos.txt", "w") as file:
            for tratamiento in self.listaTratamientos:
                file.write(f"{tratamiento.codigo};{tratamiento.nombre};{tratamiento.observaciones}\n")

   def ejecutarMenuTratamiento(self):
         opcion = self.mostrarMenuTratamiento() 
         while True:
            if opcion == '1':
                  codigo = input("Ingrese el código del tratamiento: ")
                  nombre = input("Ingrese el nombre del tratamiento: ")
                  observaciones = input("Ingrese las observaciones del tratamiento: ")
                  self.darAltaTratamiento(codigo, nombre, observaciones)
            elif opcion == '2':
                  codigo = input("Ingrese el código del tratamiento a modificar: ")
                  nombre = input("Ingrese el nuevo nombre del tratamiento: ")
                  observaciones = input("Ingrese las nuevas observaciones del tratamiento: ")
                  self.modificarTratamiento(codigo, nombre, observaciones)
            elif opcion == '3':
                  self.listarTratamientos()
            elif opcion == '4':
                  break
            else:
                  print("Opción no válida, intente nuevamente.")