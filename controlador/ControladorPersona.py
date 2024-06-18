from vista.VistaPersona import VistaPersona
from modelo.Persona import Propietario, Veterinario

class ControladorPersona:
    def __init__(self):
        self.vista= VistaPersona()
        self.listaPersonas=[]
        self.listaPropietarios=[]
        self.listaVeterinarios=[]

    def cargarArchivoPersonas(self):
        with open("archivos/personas.txt", encoding="utf-8") as archivo:
            for linea in archivo.readlines():
                datos = linea.strip().split(",")
                if len(datos) == 4:
                    codigo, nombre, direccion, telefono = datos
                    veterinario= Veterinario(codigo, nombre, direccion, telefono)
                    self.listaVeterinarios.append(veterinario)
                    self.listaPersonas.append(veterinario)
                elif len(datos) == 5:
                    codigo, nombre, direccion, telefono, numMascota= datos
                    propietario= Propietario(codigo, nombre, direccion, telefono, numMascota)
                    self.listaPropietarios.append(propietario)
                    self.listaPersonas.append(propietario)

    # función que permite guardar los datos en el archivo .txt.
    def agregarPersonas(self):
        opcion= self.vista.opcionPersona()
        codigo, nombre, direccion, telefono = self.vista.obtenerDatosPersona()
        with open('archivos/personas.txt', 'a', encoding="utf-8") as file:
            if opcion == "1":
                veterinario = Veterinario(codigo, nombre, direccion, telefono)
                file.write(f"{veterinario.getCodigo()},{veterinario.getNombre()},{veterinario.getDireccion()},{veterinario.getTelefono()}\n")
                self.listaVeterinarios.append(veterinario)
                self.listaPersonas.append(veterinario)
            elif opcion == "2":
                mascota = self.vista.pedirMascota()
                propietario= Propietario(codigo, nombre, direccion, telefono, mascota)
                file.write(f"{propietario.getCodigo()},{propietario.getNombre()},{propietario.getDireccion()},{propietario.getTelefono()},{propietario.getMascota()}\n")
                self.listaPropietarios.append(propietario)
                self.listaPersonas.append(propietario)
        self.vista.mostrarMensaje("Persona agregada con éxito.")

    def modificarPersona(self):
        self.listadoPersonas()
        persona_actual, nueva_persona= self.vista.modificarPersona()
        persona_modificar= self.buscarObjeto(persona_actual)
        if persona_modificar:
            persona_modificar.setNombre(nueva_persona)
            self.vista.mostrarMensaje("la persona fue modificada con exito")
            with open('archivos/personas.txt', 'w', encoding="utf-8") as file:
                for persona in self.listaPersonas:
                    file.write(f"{persona.getCodigo()},{persona.getNombre()}\n")

    def eliminarPersona(self):
        self.vista.mostrarLista(self.listaPersonas)
        codigo = self.vista.seleccionarPersona()
        personaEncontrada= True
        for i in self.listaPersonas:
            if i.getCodigo() == codigo:
                self.listaPersonas.remove(i)
                with open("archivos/personas.txt") as file:
                    lineas= file.readlines()
                with open ("archivos/personas.txt", "w") as file:
                    for linea in lineas:
                        if linea.startswith(codigo):
                            pass
                        else:
                            file.write(linea)
                self.vista.mostrarMensaje("persona eliminada")
                break
        if not personaEncontrada:
            self.vista.mostrarMensaje("persona no encontrada")

    def buscarObjeto(self,persona):
        for i in self.listaPersonas:
            if i.getCodigo() == persona:
                return i

    def buscarObjetoPropietario(self,propietario):
        for i in self.listaPropietarios:
            if i.getCodigo() == propietario:
                return i

    def buscarObjetoVeterinario(self,veterinario):
        for i in self.listaVeterinarios:
            if i.getCodigo() == veterinario:
                return i

    def listadoPersonas(self):
        self.vista.mostrarMensaje("Listado veterinarios:")
        self.vista.mostrarLista(self.listaVeterinarios)
        self.vista.mostrarMensaje("Listado Propietarios")
        self.vista.mostrarLista(self.listaPropietarios)

    def ejecutarMenuPersonas(self):
        opcion = self.vista.mostrarMenuPersona()
        while True:
            if opcion == "1":  # 1- Ver lista personas
                self.vista.mostrarLista(self.listaPersonas)
            elif opcion == "2":  # 2- ver lista veterinarios
                self.vista.mostrarLista(self.listaVeterinarios)
            elif opcion == "3":  # 3- ver lista propietarios
                self.vista.mostrarLista(self.listaPropietarios)
            elif opcion == "4":  # 4- agregar persona
                self.agregarPersonas()
            elif opcion == "5":  # 5- Modificar datos de una persona
                self.modificarPersona()
            elif opcion == "6":  # 6- Volver
                print("Volviendo")
                break
            else:
                print("Opción inválida. Por favor, intente nuevamente.\n")