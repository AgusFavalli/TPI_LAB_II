from pathlib import Path
from vista.VistaPersona import VistaPersona
from modelo.Persona import Propietario, Veterinario

class ControladorPersona:
    def __init__(self):
        self.vista= VistaPersona()
        self.listaPersonas=[]
        self.listaPropietarios=[]
        self.listaVeterinarios=[]

        base_dir = Path(__file__).resolve().parent.parent
        self.ruta_personas = base_dir / "archivos" / "personas.txt"

    def cargarArchivoPersonas(self):
        try:
            with open(self.ruta_personas, encoding="utf-8") as archivo:
                for linea in archivo:
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
        except FileNotFoundError:
            print(f"⚠️ No se encontró el archivo {self.ruta_personas}. Se creará vacío.")
            self.ruta_personas.parent.mkdir(parents=True, exist_ok=True)
            self.ruta_personas.touch()

    # función que permite guardar los datos en el archivo .txt.
    def agregarPersonas(self):
        opcion= self.vista.opcionPersona()
        codigo = len(self.listaPersonas) + 1
        nombre, direccion, telefono = self.vista.obtenerDatosPersona()

        with open(self.ruta_personas, 'a', encoding="utf-8") as file:
            if opcion == "1":
                veterinario = Veterinario(codigo, nombre, direccion, telefono)
                file.write(f"{codigo},{nombre},{direccion},{telefono}\n")
                self.listaVeterinarios.append(veterinario)
                self.listaPersonas.append(veterinario)
            elif opcion == "2":
                mascota = self.vista.pedirMascota()
                propietario= Propietario(codigo, nombre, direccion, telefono, mascota)
                file.write(f"{codigo},{nombre},{direccion},{telefono},{mascota}\n")
                self.listaPropietarios.append(propietario)
                self.listaPersonas.append(propietario)
        self.vista.mostrarMensaje("Persona agregada con éxito.")

    def modificarPersona(self):
        self.listadoPersonas()
        opcion= self.vista.opcionPersona()
        persona_actual, nueva_persona= self.vista.modificarPersona()
        if opcion == "1":
            veterinario_modificar= self.buscarObjetoVeterinario(persona_actual)
            veterinario_modificar.setNombre(nueva_persona)
            with open(self.ruta_personas, 'w', encoding="utf-8") as file:
                for veterinario in self.listaPersonas:
                    file.write(f"{veterinario.getCodigo()},{veterinario.getNombre()},{veterinario.getDireccion()}, {veterinario.getTelefono()}\n")
        elif opcion =="2":
            persona_modificar= self.buscarObjetoPropietario(persona_actual)
            persona_modificar.setNombre(nueva_persona)
            with open(self.ruta_personas, 'w', encoding="utf-8") as file:
                for propietario in self.listaPersonas:
                    file.write(f"{propietario.getCodigo()},{propietario.getNombre()},{propietario.getDireccion()}, {propietario.getTelefono()}, {propietario.getMascota()}\n")
        self.vista.mostrarMensaje("la persona fue modificada con exito")

    def eliminarPersona(self):
        self.vista.mostrarLista(self.listaPersonas)
        codigo = self.vista.seleccionarPersona()
        personaEncontrada= False
        for i in self.listaPersonas:
            if str(i.getCodigo()) == codigo:
                self.listaPersonas.remove(i)
                if codigo == "1": #veterinario
                    self.listaVeterinarios.remove(i)
                elif codigo == "2": #propietario
                    self.listaPropietarios.remove(i)

                with open (self.ruta_personas, "w+") as file:
                    for linea in self.listaPersonas:
                        if codigo == "1":
                            file.write(f"{linea.getCodigo()}, {linea.getNombre()}, {linea.getDireccion()}, {linea.getTelefono()}")
                        elif codigo == "2":
                            file.write(f"{linea.getCodigo()}, {linea.getNombre()}, {linea.getDireccion()}, {linea.getTelefono()}, {linea.getMascota()}")
                self.vista.mostrarMensaje("persona eliminada")
                personaEncontrada= True
                break
            else:
                self.vista.mostrarMensaje("persona no encontrada")

    def buscarObjeto(self,persona):
        for i in self.listaPersonas:
            if str(i.getCodigo()) == persona:
                return i

    def buscarObjetoPropietario(self,propietario):
        for i in self.listaPropietarios:
            if str(i.getCodigo()) == propietario:
                return i

    def buscarObjetoVeterinario(self,veterinario):
        for i in self.listaVeterinarios:
            if str(i.getCodigo()) == veterinario:
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
            elif opcion == "6": # 6- Eliminar persona
                self.eliminarPersona()
            elif opcion == "7":  # 7- Volver
                print("Volviendo al menu principal...")
                return
            else:
                print("Opción inválida. Por favor, intente nuevamente.\n")
            opcion = self.vista.mostrarMenuPersona()