from controlador.ControladorMascotas import ControladorMascotas
from controlador.ControladorPersona import ControladorPersona
from controlador.ControladorRaza import ControladorRaza
from controlador.ControladorVacuna import ControladorVacuna
from controlador.ControladorDiagnostico import ControladorDiagnostico
from controlador.ControladorTratamiento import ControladorTratamiento
from vista.VistaGeneral import VistaGeneral

class ControladorGeneral:
    def __init__(self):
        self.vista= VistaGeneral()
        self.controladorPersonas= ControladorPersona()
        self.controladorRaza= ControladorRaza()
        self.controladorVacuna= ControladorVacuna()
        self.controladorTratamiento= ControladorTratamiento()
        self.controladorMascotas = ControladorMascotas(self.controladorRaza, self.controladorPersonas)
        self.controladorDiagnostico= ControladorDiagnostico(self.controladorTratamiento, self.controladorVacuna)

    def cargarArchivos(self):       #carga los archivos txt a las listas de cada clase
        self.controladorPersonas.cargarArchivoPersonas()
        self.controladorRaza.cargarArchivoRazas()
        self.controladorVacuna.cargarArchivoVacunas()
        self.controladorTratamiento.cargarArchivoTratamientos()
        self.controladorMascotas.cargarArchivoMascotas()
        self.controladorDiagnostico.cargarArchivoDiagnosticos()


    def menu(self):
        self.cargarArchivos()
        self.vista.bienvenida()
        opcion= self.vista.menu()
        while opcion != "0":
            if opcion == "1":  #muestra la lista mascotas activas
                self.controladorMascotas.listadoMascotasActivas()
            elif opcion == "2": #muestra la lista de razas
                self.controladorRaza.listadoRazas()
            elif opcion == "3": #muestra la lista de vacunas
                self.vista.getMensaje("--- Vacuna / Descripcion ---")
                self.controladorVacuna.listadoVacunas()
            elif opcion == "4": #muestra la lista de tratamientos
                self.vista.getMensaje("--- Tratamiento / Descripcion ---")
                self.controladorTratamiento.listadoTratamientos()
            elif opcion == "5":
                self.controladorDiagnostico.listadoDiagnosticos()
            elif opcion == "6":
                self.controladorPersonas.listadoPersonas()
            elif opcion == "7":
                self.controladorDiagnostico.eliminarDiagnostico()
            else:
                self.vista.getMensaje("La opcion indicada no es valida")
            opcion= self.vista.menu()
