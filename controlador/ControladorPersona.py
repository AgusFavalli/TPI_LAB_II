from vista.VistaGeneral import VistaGeneral
from modelo.Persona import Propietario, Veterinario

class ControladorPersona:
    def __init__(self):
        self.vista= VistaGeneral()
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

    # función que permite guardar los datos en el carchivo .txt.
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
        self.vista.getMensaje("Persona agregada con éxito.")

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
                self.vista.getMensaje("persona eliminada")
                break
        if not personaEncontrada:
            self.vista.getMensaje("persona no encontrada")

    def buscarObjetoPropietario(self,propietario):
        for i in self.listaPropietarios:
            if i.getCodigo() == propietario:
                return i

    def buscarObjetoVeterinario(self,veterinario):
        for i in self.listaVeterinarios:
            if i.getCodigo() == veterinario:
                return i

    def listadoPersonas(self):
        self.vista.getMensaje("Listado veterinarios:")
        self.vista.mostrarLista(self.listaVeterinarios)
        self.vista.getMensaje("Listado Propietarios")
        self.vista.mostrarLista(self.listaPropietarios)