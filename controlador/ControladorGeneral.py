from controlador.ControladorMascotas import ControladorMascotas
from controlador.ControladorPropietario import ControladorPropietario
from controlador.ControladorRaza import ControladorRaza
from vista.VistaGeneral import VistaGeneral

class ControladorGeneral:
    def __init__(self):
        self.vista= VistaGeneral()
        self.controladorPropietarios= ControladorPropietario()
        self.controladorRaza= ControladorRaza()
        self.controladorMascotas = ControladorMascotas(self.controladorRaza, self.controladorPropietarios)


    def cargarArchivos(self):       #carga los archivos txt a las listas de cada clase
        self.controladorPropietarios.cargarArchivoPropietarios()
        self.controladorRaza.cargarArchivoRazas()
        self.controladorMascotas.cargarArchivoMascotas()


    def menu(self):
        self.cargarArchivos()
        self.vista.bienvenida()
        opcion= self.vista.menu()
        while opcion != "0":
            if opcion == "1":  #muestra la lista mascotas activas
                self.controladorMascotas.listadoMascotasActivas()
            elif opcion == "2":
                pass
            elif opcion == "3":
                pass
            elif opcion == "4":
                pass
            else:
                self.vista.getMensaje("La opcion indicada no es valida")
            opcion= self.vista.menu()
