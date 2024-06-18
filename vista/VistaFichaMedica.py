class VistaFichaMedica:

    def mostrarMenuFinchaMedica(self):
        print("Menú de Gestión de Razas\n"
            "1- Consultar una ficha medica\n"
            "2- Modificar una Ficha Medica\n"
            "5- Volver\n")
        return input("Seleccione una opción: ")
   

    def modificarFichaMedica(self):
        vieja_fichaMedica= input("ingrese el codigo de la raza actual que desea modificar")
        nueva_fichaMedica= input("ingrese el nombre del nombre modificado de la raza")
        return vieja_fichaMedica, nueva_fichaMedica


    def mostrarMensaje(self, dato):
        print (dato)

    def mostrarLista(self, lista):
        for i in lista:
            print(i)

    def obtenerFichaMedica(self):
        return input("ingrese el nombre de la ficha medica")

    def obtenerNombreMascota(self):
        return input("ingrese el nombre de la mascota")
    
    def mostrarSolicitudFicha(self, nombreMascota, ficha):
        if ficha:
            print("\nFicha Médica:")
            print(ficha)
        else:
            print(f"\nNo se encontró una ficha médica para {nombreMascota}.")

    def ingresarFecha(self):
        return input("Ingrese la fecha de la ficha médica: ")
    
    def ingresarInformacion(self):
        tratamiento = input("Ingrese el tratamiento: ")
        veterinario = input("Ingrese el nombre del veterinario: ")
        diagnostico = input("Ingrese el diagnóstico: ")
        vacunas = input("Ingrese las vacunas: ")
        return tratamiento, veterinario, diagnostico, vacunas  
    
    def mensajeModificacion(nombreMascota):
        print(f"\nFicha médica de {nombreMascota} actualizada correctamente.")