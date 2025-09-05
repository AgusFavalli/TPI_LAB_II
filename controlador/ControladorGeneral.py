from controlador.ControladorMascotas import ControladorMascotas
from controlador.ControladorPersona import ControladorPersona
from controlador.ControladorRaza import ControladorRaza
from controlador.ControladorVacuna import ControladorVacuna
from controlador.ControladorDiagnostico import ControladorDiagnostico
from controlador.ControladorTratamiento import ControladorTratamiento
from controlador.ControladorFichaMedica import ControladorFichaMedica
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
        self.controladorFichaMedica= ControladorFichaMedica(self.controladorTratamiento, self.controladorPersonas, self.controladorDiagnostico, self.controladorVacuna)

    def cargarArchivos(self):       #carga los archivos txt a las listas de cada clase
        self.controladorPersonas.cargarArchivoPersonas()
        self.controladorRaza.cargarArchivoRazas()
        self.controladorVacuna.cargarArchivoVacunas()
        self.controladorTratamiento.cargarArchivoTratamientos()
        self.controladorMascotas.cargarArchivoMascotas()
        self.controladorDiagnostico.cargarArchivoDiagnosticos()


    def menu(self):
        self.cargarArchivos()   #carga todos los archivos a las listas
        while True:
            self.vista.bienvenida()
            opcion = self.vista.menu()
            if opcion == "1":  #gestion de razas
                self.controladorRaza.ejecutarMenuRazas()
            elif opcion == "2": #gestion de personas
                self.controladorPersonas.ejecutarMenuPersonas()
            elif opcion == "3": #gestion de diagnosticos
                self.controladorDiagnostico.ejecutarMenuDiagnosticos()
            elif opcion == "4": #gestion de tratamiento
                self.controladorTratamiento.ejecutarMenuTratamientos()
            elif opcion == "5": #gestion de vacunas
                self.controladorVacuna.ejecutarMenuVacunas()
            elif opcion == "6": #gestion de mascotas
                self.controladorMascotas.ejecutarMenuMascotas()
            elif opcion == "7": #gestion de ficha medica
                pass
            elif opcion == "8": #salir
                break
            else:
                self.vista.getMensaje("La opcion indicada no es valida")
