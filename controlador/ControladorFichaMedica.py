from modelo.FichaMedica import FichaMedica
from vista.VistaFichaMedica import VistaFichaMedica
from controlador.ControladorMascotas import ControladorMascotas
from controlador.ControladorPersona import ControladorPersona
from controlador.ControladorRaza import ControladorRaza
from controlador.ControladorVacuna import ControladorVacuna
from controlador.ControladorDiagnostico import ControladorDiagnostico
from controlador.ControladorTratamiento import ControladorTratamiento
import os
import shutil #este modulo permite el manejo de archivos (copiar, mover, etc.)

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
        self.rutaFichasEliminadas = "./archivosFichasMedicas/fichasMedicasEliminadas"  # Carpeta para las fichas eliminadas        


                                      
    def modificarFichaMedica(self):
        nombreMascota = self.vista.solicitarNombreMascota()
        fichaMedica = self.cargarFichaMedica(nombreMascota)
        if fichaMedica:
            nuevosDatos = self.vista.solicitarDatosFichaMedica()
            self.guardarFichaMedica(nombreMascota, nuevosDatos)
            self.vista.mostrarMensaje("Ficha médica actualizada con éxito.")
        else:
            self.vista.mostrarMensaje("No se encontró la ficha médica para modificar.")

    def guardarFichaMedica(self, nombreMascota, datos):
        rutaArchivo = os.path.join(self.rutaArchivosFichasMedicas, f"{nombreMascota}.txt")
        with open(rutaArchivo, "a+", encoding="utf-8") as file:
            linea = f"{datos['fecha']},{datos['tratamiento']},{datos['veterinario']},{datos['diagnosticos']},{datos['vacunas']}\n"
            file.write(linea)
        self.vista.mostrarMensajeVariable("Datos guardados en", rutaArchivo)

    def crearFichaMedica(self):
        self.vista.mostrarMensaje("Iniciando creación de ficha médica...")
        if not os.path.exists(self.rutaArchivosFichasMedicas):
            os.makedirs(self.rutaArchivosFichasMedicas)
            self.vista.mostrarMensajeVariable("Carpeta creada en", self.rutaArchivosFichasMedicas)
        nombreMascota = self.vista.solicitarNombreMascota()
        rutaArchivo = os.path.join(self.rutaArchivosFichasMedicas, f"{nombreMascota}.txt")
        if not os.path.exists(rutaArchivo):
            datosFicha = self.vista.solicitarDatosFichaMedica()
            self.guardarFichaMedica(nombreMascota, datosFicha)
            self.vista.mostrarMensaje("Ficha médica creada con éxito.")
        else:
            self.vista.mostrarMensaje("Ya existe una ficha médica para esta mascota.")

    def cargarFichaMedica(self, nombreMascota):
        rutaArchivo = os.path.join(self.rutaArchivosFichasMedicas, f"{nombreMascota}.txt")
        try:
            with open(rutaArchivo, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            return None

    def listarFichasMedicas(self):
        archivos = os.listdir(self.rutaArchivosFichasMedicas)
        fichas = [archivo for archivo in archivos if archivo.endswith('.txt')]
        if fichas:
            self.vista.mostrarMensaje("Lista de fichas médicas:")
            for ficha in fichas:
                self.vista.mostrarMensaje(ficha)
        else:
            self.vista.mostrarMensaje("No hay fichas médicas disponibles.")

    def consultarFichaMedica(self):
        nombreMascota = self.vista.solicitarNombreMascota()
        rutaArchivo = os.path.join(self.rutaArchivosFichasMedicas, f"{nombreMascota}.txt")
        if os.path.exists(rutaArchivo):
            self.vista.mostrarMensajeVariable("Ficha médica de", nombreMascota)
            self.mostrarContenidoFicha(rutaArchivo)
        else:
            self.vista.mostrarMensajeVariable("No existe una ficha médica para la mascota llamada", nombreMascota)

    def mostrarContenidoFicha(self, rutaArchivo):
        if rutaArchivo and os.path.exists(rutaArchivo):
            nombreMascota = os.path.basename(rutaArchivo).replace('.txt', '')
            self.vista.mostrarMensajeVariable("Contenido de la ficha médica de", nombreMascota)
            self.vista.mostrarMensaje("Fecha, Tratamiento, Veterinario, Diagnósticos, Vacunas")
            with open(rutaArchivo, "r", encoding="utf-8") as file:
                self.vista.mostrarMensaje(file.read())
        else:
            self.vista.mostrarMensaje("No se puede mostrar el contenido, el archivo no existe.")

    def eliminarFichaMedica(self):
        self.listarFichasMedicas()
        nombreMascota = self.vista.pedir("Ingrese el nombre de la mascota cuya ficha desea eliminar: ")
        rutaArchivo = os.path.join(self.rutaArchivosFichasMedicas, f"{nombreMascota}.txt")
        if os.path.exists(rutaArchivo):
            if not os.path.exists(self.rutaFichasEliminadas):
                os.makedirs(self.rutaFichasEliminadas)
            rutaEliminada = os.path.join(self.rutaFichasEliminadas, f"{nombreMascota}.txt")
            shutil.move(rutaArchivo, rutaEliminada)
            self.vista.mostrarMensajeVariable("La ficha médica fue eliminada y movida a", self.rutaFichasEliminadas)
        else:
            self.vista.mostrarMensajeVariable("No existe una ficha médica para la mascota llamada", nombreMascota)

    def ejecutarMenuFichaMedica(self):
        while True:
            opcion = self.vista.mostrarMenuFichaMedica()
            if opcion == '1':
                self.vista.limpiarPantalla()
                self.listarFichasMedicas()
                self.consultarFichaMedica()
            elif opcion == '2':
                self.vista.limpiarPantalla()
                self.modificarFichaMedica()
            elif opcion == '3':
                self.vista.limpiarPantalla()
                self.crearFichaMedica()
            elif opcion == '4':
                self.vista.limpiarPantalla()
                self.eliminarFichaMedica()
            elif opcion == '5':
                break
            else:
                self.vista.mostrarMensaje("Opción no válida, por favor seleccione de nuevo.")
