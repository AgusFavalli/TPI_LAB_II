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

#.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    # guarda la ficha médica, en una carpeta en específico
    def guardarFichaMedica(self, rutaArchivo, datos):
        with open(rutaArchivo, "a+") as file:
            # Formatear los datos en una sola línea, separados por ","
            linea = f"{datos['fecha']},{datos['tratamiento']},{datos['veterinario']},{datos['diagnosticos']},{datos['vacunas']}\n"
            # Escribir la línea en el archivo
            file.write(linea)
            self.vista.mostrarMensajeVariable("Datos guardados en", rutaArchivo)


    # crea la ficha médica, en una carpeta en específico
    def crearFichaMedica(self):
        self.vista.mostrarMensaje("Iniciando creación de ficha médica...")  
        if not os.path.exists(self.rutaArchivosFichasMedicas):
            os.makedirs(self.rutaArchivosFichasMedicas)
            return self.vista.mostrarMensajeVariable("carpeta creada en ", self.rutaArchivosFichasMedicas)  
        nombreMascota = self.vista.solicitarNombreMascota()
        rutaArchivo = os.path.join(self.rutaArchivosFichasMedicas, f"{nombreMascota}.txt")
        if not os.path.exists(rutaArchivo):
            datosFicha = self.vista.solicitarDatosFichaMedica()
            self.guardarFichaMedica(rutaArchivo, datosFicha)
            return self.vista.mostrarMensaje("Ficha médica creada con éxito.")
        else:
            return self.vista.mostrarMensaje("Ya existe una ficha médica para esta mascota.")
#.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    def cargarFichaMedica(self, nombremascota):
         try:
            with open(f"{nombremascota}.txt", "r") as file:
                  for linea in file:
                     self.vista.mostrarMensaje(linea.strip())
         except FileNotFoundError:
             return self.vista.mostrarMensaje("No se encontro el archivo")

#.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    # Imprime una lista de todos los archivos .txt en la carpeta de archivosFichaMedica
    def listarFichasMedicas(self):
        archivos = os.listdir(self.rutaArchivosFichasMedicas)
        fichas = [archivo for archivo in archivos if archivo.endswith('.txt')]
        if fichas:
            self.vista.mostrarMensaje("Lista de fichas médicas:")
            for ficha in fichas:
                self.vista.mostrarMensaje(ficha)
        else:
            self.vista.mostrarMensaje("No hay fichas médicas disponibles.")

    # Consulta una ficha médica por nombre de mascota
    def consultarFichaMedica(self):
        nombreMascota = self.vista.solicitarNombreMascota
        rutaArchivo = os.path.join(self.rutaArchivosFichasMedicas, f"{nombreMascota}.txt")
        if os.path.exists(rutaArchivo):
            self.vista.mostrarMensajeVariable("Ficha médica de", nombreMascota)
            return rutaArchivo
        else:
            return self.vista.mostrarMensajeVariable("No existe una ficha médica para la mascota llamada", nombreMascota)
            

# Muestra el contenido de una ficha médica seleccionada
    def mostrarContenidoFicha(self, rutaArchivo):
        if rutaArchivo and os.path.exists(rutaArchivo):
            nombreMascota = os.path.basename(rutaArchivo).replace('.txt', '')
            self.vista.mostrarMensajeVariable("Contenido de la ficha médica de ", nombreMascota)
            self.vista.mostrarMensaje("Fecha, Tratamiento, Veterinario, Diagnósticos, Vacunas")
            with open(rutaArchivo, "r", encoding="utf-8") as file:
                self.vista.mostrarMensaje(file.read())
        else:
            self.vista.mostrarMensaje("No se puede mostrar el contenido, el archivo no existe.")


 # Instancia una nueva ficha médica con los datos proporcionados
    def instanciarFichaMedica(self, fecha, tratamiento, veterinario, diagnosticos, vacunas):
        return self.modelo.FichaMedica(fecha, tratamiento, veterinario, diagnosticos, vacunas)

    # Agrega información nueva a una ficha médica existente
    def agregarInformacionFichaMedica(self, rutaArchivo, datos):
        if os.path.exists(rutaArchivo):
            with open(rutaArchivo, "a+", encoding="utf-8") as file:
                linea = f"{datos['fecha']},{datos['tratamiento']},{datos['veterinario']},{datos['diagnosticos']},{datos['vacunas']}\n"
                file.write(linea)
            self.vista.mostrarMensaje("Información agregada con éxito.")
        else:
            self.vista.mostrarMensaje("El archivo no existe. No se puede agregar información.")

    # Selecciona y elimina una ficha médica moviéndola a otra carpeta
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
            opcion = self.vista.mostrarMenuFinchaMedica()
            if opcion == '1':
                self.vista.limpiarPantalla()
                self.listarFichasMedicas()
                self.consultarFichaMedica()
            elif opcion == '2':
                self.modificarFichaMedica()
            elif opcion == '3':
                self.vista.limpiarPantalla()

                self.crearFichaMedica()
                self.vista.limpiarPantalla()
            elif opcion == '4':
                break
            else:
                self.vista.mostrarMensaje("Opción no válida, por favor seleccione de nuevo.")
