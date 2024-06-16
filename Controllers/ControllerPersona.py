from Models.Persona import *
from Views.VistaPersona import VistaPersona
import os



class ControllerPersona:
    def __init__(self, vista = VistaPersona()):
      self.vista = vista
      self.personas = []

# función que permite la carga desde el archivo personas.txt
    def cargarDatos(self):
        if os.path.exists('Scripts/personas.txt'):
            with open('Scripts/personas.txt', 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    if data[0] == 'Veterinario':
                        self.personas.append(Veterinario(*data[1:]))
                    elif data[0] == 'Propietario':
                        self.personas.append(Propietario(*data[1:]))

# función que permite guardar los datos en el carchivo .txt.
    def guardarDatos(self):
        with open('Scripts/personas.txt', 'a') as file:
            for persona in self.personas:
                tipo = 'Veterinario' if isinstance(persona, Veterinario) else 'Propietario'
                file.write(f"{tipo},{persona.codigo},{persona.nombre},{persona.direccion},{persona.telefono}\n")

# función que permite agregar personas
    def agregarPersona(self, tipo):
        codigo, nombre, direccion, telefono = self.vista.obtenerDatosPersona()
        if tipo == 'Veterinario':
            self.personas.append(Veterinario(codigo, nombre, direccion, telefono))
        elif tipo == 'Propietario':
            self.personas.append(Propietario(codigo, nombre, direccion, telefono))
        self.guardarDatos()
        self.vista.mostrarMensaje("Persona agregada con éxito.")

# función que permite eliminar personas
    def eliminarPersona(self):
        codigo = self.vista.seleccionarPersona()
        persona = next((p for p in self.personas if p.codigo == codigo), None)
        if persona:
            self.personas.remove(persona)
            self.guardarDatos()
            self.vista.mostrarMensaje("Persona eliminada con éxito.")
        else:
            self.vista.mostrarMensaje("Persona no encontrada.")

# función que permite modificar datos
    def modificarPersona(self):
        codigo = self.vista.seleccionarPersona()
        persona = next((p for p in self.personas if p.codigo == codigo), None)
        if persona:
            _, nombre, direccion, telefono = self.vista.obtenerDatosPersona()
            persona.nombre = nombre
            persona.direccion = direccion
            persona.telefono = telefono
            self.guardarDatos()
            self.vista.mostrarMensaje("Persona modificada con éxito.")
        else:
            self.vista.mostrarMensaje("Persona no encontrada.")

    def listarPersonas(self):
        self.vista.mostrarListaPersonas(self.personas)

#funcion alternativa para buscar personas
    def buscar_persona(lista, termino_busqueda):
      resultados = []
      for persona in lista:
         nombre_completo = persona[2]
         nombre_pila, apellido = nombre_completo.split()
         if termino_busqueda.lower() in nombre_pila.lower() or termino_busqueda.lower() in apellido.lower():
               resultados.append(persona)
      return resultados

# función que permite consultar personas.
    def consultarPersona(self):
        codigo = self.vista.seleccionarPersona()
        persona = next((p for p in self.personas if p.codigo == codigo), None)
        if persona:
            self.vista.mostrarPersona(persona)
        else:
            self.vista.mostrarMensaje("Persona no encontrada.")

