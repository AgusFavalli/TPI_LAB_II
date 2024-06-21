import os

class VistaFichaMedica:
    def mostrarMenuFichaMedica(self):
        print("Menú de Gestión de Fichas Médicas\n"
              "1- Consultar una ficha médica\n"
              "2- Agregar información a una ficha médica\n"
              "3- Crear una ficha médica\n"
              "4- Eliminar una ficha médica\n"
              "5- Volver\n")
        return input("Seleccione una opción: ")

    def pedir(self, mensaje):
        return input(mensaje)

    def mostrarMensajeVariable(self, mensaje, variable):
        print(f"{mensaje} {variable}")

    def mostrarMensaje(self, dato,):
        print(dato)

    def solicitarNombreMascota(self):
        return input("Ingrese el nombre de la mascota: \n").capitalize()

    def solicitarDatosFichaMedica(self):
        fecha = input("Ingrese la fecha: ")
        tratamiento = input("Ingrese el tratamiento: ")
        veterinario = input("Ingrese el nombre del veterinario: ")
        diagnosticos = input("Ingrese los diagnósticos: ")
        vacunas = input("Ingrese las vacunas: ")
        return {
            'fecha': fecha,
            'tratamiento': tratamiento,
            'veterinario': veterinario,
            'diagnosticos': diagnosticos,
            'vacunas': vacunas
        }

#funciones Extras
#Dependiendo del SO, cls limpia la pantalla en windows
    def limpiarPantalla(self):
       os.system("cls" if os.name == "nt" else "clear")  

#La funcion getch() del modulo msvcrt espera el ingreso de una tecla sin retornarla. En linux se configura la terminal en modo RAW y leer un caracter con la funcion sys.stdin.read(1)
    def esperarTecla(self):
         """Espera a que el usuario presione una tecla para continuar."""
         if os.name == 'nt':
            import msvcrt
            print("Presiona una tecla para continuar...")
            msvcrt.getch()