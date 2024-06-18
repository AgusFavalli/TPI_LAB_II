from modelo.FichaMedica import FichaMedica
from vista.VistaFichaMedica import VistaFichaMedica
from controlador.ControladorMascotas import ControladorMascotas
from controlador.ControladorPersona import ControladorPersona
from controlador.ControladorRaza import ControladorRaza
from controlador.ControladorVacuna import ControladorVacuna
from controlador.ControladorDiagnostico import ControladorDiagnostico
from controlador.ControladorTratamiento import ControladorTratamiento


class ControladorFichaMedica:
    def __init__(self,controladorRaza, controladorPersonas):
        self.vista= VistaFichaMedica()
        self.controladorPersonas= ControladorPersona()
        self.controladorRaza= ControladorRaza()
        self.controladorVacuna= ControladorVacuna()
        self.controladorTratamiento= ControladorTratamiento()
        self.controladorMascotas = ControladorMascotas(self.controladorRaza, self.controladorPersonas)
        self.controladorDiagnostico= ControladorDiagnostico(self.controladorTratamiento, self.controladorVacuna)
        self.listaFichasMedicas = []

   # metodo para consultar una ficha medica en particular
    def consultarFichaMedica(self):
        nombreMascota = self.vista.obtenerNombreMascota()
        ficha = self.consultar_ficha_medica(nombreMascota)
        self.vista.mostrarSolicitudFicha(nombreMascota, ficha)

   # metodo para modificar una ficha medica en particular
    def modificarFichaMedica(self):
        nombreMascota = self.vista.obtenerNombreMascota()
        fecha = self.vista.ingresarFecha()
        tratamiento, veterinario, diagnostico, vacunas = self.vista.ingresarInformacion()
        return nombreMascota, fecha, tratamiento, veterinario, diagnostico, vacunas
      
        #self.modificarFichaMedica(nombreMascota, fecha, tratamiento, veterinario, diagnostico, vacunas) 
        #self.vista.mensajeModificacion(nombreMascota)

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

    def obtenerVacunas(self):
      with open("archivos/vacunas.txt", "r") as file:
         vacunas = file.readlines()
      return [vacuna.strip() for vacuna in vacunas] 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def ejecutarMenuFichaMedica(self):
        opcion = self.vista.mostrarMenuFinchaMedica()
        while True:
            if opcion == "1":  # 1- Consultar una ficha medica
                pass
            elif opcion == "2":  # 2- Modificar una Ficha Medica
                pass
            elif opcion == "3":  # 5- salir
                self.vista.mostrarMensaje("Volviendo al menu principal...")
                break
            else:
                print("Opción inválida. Por favor, intente nuevamente.\n")
