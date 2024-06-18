from modelo.FichaMedica import FichaMedica
from vista.VistaFichaMedica import VistaFichaMedica
from controlador.ControladorMascotas import ControladorMascotas
from controlador.ControladorPersona import ControladorPersona
from controlador.ControladorRaza import ControladorRaza
from controlador.ControladorVacuna import ControladorVacuna
from controlador.ControladorDiagnostico import ControladorDiagnostico
from controlador.ControladorTratamiento import ControladorTratamiento
import os

class ControladorFichaMedica:
    def __init__(self):
        self.vista= VistaFichaMedica()
        self.controladorPersonas= ControladorPersona()
        self.controladorRaza= ControladorRaza()
        self.controladorVacuna= ControladorVacuna()
        self.controladorTratamiento= ControladorTratamiento()
        self.controladorMascotas = ControladorMascotas(self.controladorRaza, self.controladorPersonas)
        self.controladorDiagnostico= ControladorDiagnostico(self.controladorTratamiento, self.controladorVacuna)
        self.listaFichasMedicas = []
        self.rutaArchivosFichasMedicas = "./archivosFichasMedicas" #carpeta donde se desea almacenar las fichas individuales

   # metodo para consultar una ficha medica en particular
    def consultarFichaMedica(self):
        nombreMascota = self.vista.solicitarNombreMascota()
        fichaMedica = self.cargarFichaMedica(nombreMascota)
        self.vista.mostrarFichaMedica(fichaMedica)
                                      
      # metodo para modificar una ficha medica en particular
    
    
    
    def modificarFichaMedica(self):
         nombreMascota = self.vista.solicitarNombreMascota()
         fichaMedica = self.cargarFichaMedica(nombreMascota)
         if fichaMedica:
               nuevosDatos = self.vista.solicitarDatosFichaMedica()
               self.guardarFichaMedica(nombreMascota, nuevosDatos)
               self.vista.mostrarMensaje("Ficha médica actualizada con éxito.")
         else:
               self.vista.mostrarMensaje("No se encontró la ficha médica para modificar.")


#crea la ficha medica, en una carpeta en especifico
    def crearFichaMedica(self):
         #nombreMascota = self.vista.solicitarNombreMascota()
         if not os.path.exists(self.rutaArchivosFichasMedicas):
            os.makedirs(self.rutaArchivosFichasMedicas)
         nombreMascota = self.vista.solicitarNombreMascota()
         rutaArchivo = os.path.join(self.rutaArchivosFichasMedicas, f"{nombreMascota}.txt")
         if not os.path.exists(rutaArchivo):
            datosFicha = self.vista.solicitarDatosFichaMedica()
            self.guardarFichaMedica(rutaArchivo, datosFicha)
            self.vista.mostrarMensaje("Ficha médica creada con éxito.")
         else:
            self.vista.mostrarMensaje("Ya existe una ficha médica para esta mascota.")

    def cargarFichaMedica(self, nombremascota):
        try:
            with open(f"{nombremascota}.txt", "r") as file:
                datos = file.readlines()
                return {
                    'fecha': datos[0].strip(),
                    'tratamiento': datos[1].strip(),
                    'veterinario': datos[2].strip(),
                    'diagnosticos': datos[3].strip(),
                    'vacunas': datos[4].strip()
                }
        except FileNotFoundError:
            return None

    def guardarFichaMedica(self, nombreMascota, datos):
      with open(f"{nombreMascota}.txt", "a+") as file:
         # Formatear los datos en una sola línea, separados por ";"
         linea = f"{datos['fecha']},{datos['tratamiento']},{datos['veterinario']},{datos['diagnosticos']},{datos['vacunas']}\n"
         # Escribir la línea en el archivo
         file.write(linea)


 #metodos para obtener informacion desde los archivos   
    def obtenerTratamientos(self):
      with open("archivos/tratamientos.txt", "r") as file:
         tratamientos = file.readlines()
      return [tratamiento.strip() for tratamiento in tratamientos]

    def obtenerVeterinarios(self):
      with open("archivos/veterinarios.txt", "r") as file:
         veterinarios = file.readlines()
      return [veterinario.strip() for veterinario in veterinarios]

    def obtenerDiagnosticos(self):
      with open("archivos/tratamientos.txt", "r") as file:
         tratamientos = file.readlines()
      return [tratamiento.strip() for tratamiento in tratamientos]    

 #.-.-.-.-.-.-..-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    def obtenerVacunas(self):
      with open("archivos/vacunas.txt", "r") as file:
         vacunas = file.readlines()
      return [vacuna.strip() for vacuna in vacunas] 
    
    def ejecutarMenuFichaMedica(self):
         while True:
            self.vista.limpiarPantalla()   
            opcion = self.vista.mostrarMenuFinchaMedica()
            if opcion == '1':
                self.consultarFichaMedica()
            elif opcion == '2':
                self.modificarFichaMedica()
            elif opcion == '3':
                self.crearFichaMedica()
            elif opcion == '4':
                break
            else:
                self.vista.mostrarMensaje("Opción no válida, por favor seleccione de nuevo.")
