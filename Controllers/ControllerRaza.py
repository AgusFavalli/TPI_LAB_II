from Models.Raza import Raza
from Views.VistaRaza import VistaRaza

class selfRaza:
    def __init__(self, vista = VistaRaza()):
      self.vista = vista
      self.listaRazas = []
      self.cargarArchivos()

    def cargarArchivos(self):
        try:
            with open("Scripts/razas.txt", "r") as file:
                lineas = file.readlines()
            for linea in lineas:
                codigo, nombre = linea.strip().split(";")
                self.listaRazas.append(Raza(codigo, nombre))
        except FileNotFoundError:
            with open("Scripts/razas.txt", "w") as file:
                pass

    def guardarArchivos(self):
        with open("Scripts/razas.txt", "w") as file:
            for raza in self.listaRazas:
                file.write(f"{raza}\n")

    def darAltaRaza(self, codigo, nombre):
        nuevaRaza = Raza(codigo, nombre)
        self.listaRazas.append(nuevaRaza)
        self.guardarArchivos()

    def modificarRaza(self, codigo, nuevoNombre):
        for raza in self.listaRazas:
            if raza.codigo == codigo:
                raza.nombre = nuevoNombre
                self.guardarArchivos()
                return True
        return False

    def eliminarRaza(self, codigo):
        for raza in self.listaRazas:
            if raza.codigo == codigo:
                self.listaRazas.remove(raza)
                self.guardarArchivos()
                return True
        return False

    def listarRazas(self):
        return self.listaRazas


    def ejecutarMenuRaza(self, opcion):
        opcion = self.vista.menuRaza()
        while True:
            if opcion == "1":
                  codigo = input("Ingrese el código de la nueva raza: ")
                  nombre = input("Ingrese el nombre de la nueva raza: ")
                  self.darAltaRaza(codigo, nombre)
                  print("Raza agregada exitosamente.\n")
            
            elif opcion == "2":
                  codigo = input("Ingrese el código de la raza a modificar: ")
                  nuevoNombre = input("Ingrese el nuevo nombre de la raza: ")
                  if self.modificarRaza(codigo, nuevoNombre):
                     print("Raza modificada exitosamente.\n")
                  else:
                     print("Raza no encontrada.\n")
            
            elif opcion == "3":
                  codigo = input("Ingrese el código de la raza a eliminar: ")
                  if self.eliminarRaza(codigo):
                     print("Raza eliminada exitosamente.\n")
                  else:
                     print("Raza no encontrada o no se puede eliminar.\n")
            
            elif opcion == "4":
                  razas = self.listarRazas()
                  print("Listado de Razas:")
                  for raza in razas:
                     print(f"Código: {raza.codigo}, Nombre: {raza.nombre}")
                  print()
            
            elif opcion == "5":
                  print("Volviendo")
                  break
            
            else:
                  print("Opción inválida. Por favor, intente nuevamente.\n")     
   