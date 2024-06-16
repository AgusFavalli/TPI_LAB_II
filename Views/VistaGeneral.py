from extra.extraFunctions import *

class View:
    #Se solicitan al usuario los datos individuales de una fecha.
    def request_date(self, message, format):
        while True:
            clearScreen()
            data = input(f"Ingrese el {message} de la reserva en formato {format}: \n")
            if data.isnumeric() and int(data) > 0:
                return data
            else:
                print("El dato debe ser un entero positivo")
                self.print_message("Presione cualquier tecla para continuar...")
                waitKey()
                continue

    #Imprimir un mensaje.
    def print_message(self, message):
        print(message)

    #Imprimir menu y solicitar una opción.
    def request_menu_option(self):
        print("Veterinaria Sierras Chicas S.A.")
        print("1. GESTIÓN DE RAZAS")
        print("2. GESTIÓN DE PERSONAS")
        print("3. GESTIÓN DE DIAGNOSTICO")
        print("4. GESTIÓN DE TRATAMIENTOS")
        print("5. GESTIÓN DE VACUNAS")
        print("7. GESTIÓN DE DIAGNOSTICO")
        print("8. Salir")
        return input("Ingrese una opción: \n")
    

    
    #Se realiza una validacion general.
    def requestVerification(self, message):
        while True:
            clearScreen()
            self.print_message(message)
            verification = input("¿Es correcto? 1 = SI / 0 = NO\n")
            if verification == "1" or verification == "0":
                return verification
            else:
                self.print_message("Ingresa una opción correcta")
                self.print_message("Presione una tecla para continuar...")
                waitKey()

