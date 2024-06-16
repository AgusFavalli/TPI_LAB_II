
class VistaPersona:
    def mostrar(self,lista):
        print(lista)
        for i in lista:
            print(i)

# esta función trae el menu que corresponde a la gestion de personas
    def mostrarMenuPersona(self):
        print("1- Ver lista personas")
        print("2- Consultar persona")
        print("3- Agregar una persona")
        print("4- Eliminar una persona")
        print("5- Modificar datos de una persona")
        print("6- Volver")
        return input("Seleccione una opción: ")

    def obtenerTipoPersona(self):
        tipo = input("Ingrese el tipo de persona (Veterinario/Propietario): ")
        return tipo.capitalize()



# esta función lista las personas
    def mostrarListaPersonas(self, personas):
        for persona in personas:
            print(f"codigo: {persona.cogigo}, Nombre: {persona.nombre}, Dirección: {persona.direccion}, Teléfono: {persona.telefono}")

# esta función muestra una persona en particular
    def mostrarPersona(self, persona):
        print(f"codigo: {persona.codigo}, Nombre: {persona.nombre}, Dirección: {persona.direccion}, Teléfono: {persona.telefono}")

# esta permite buscar los datos de una persona en particular mediante la interacción
    def obtenerDatosPersona(self):
        codigo = input("Ingrese el codigo: ")
        nombre = input("Ingrese el nombre: ")
        direccion = input("Ingrese la dirección: ")
        telefono = input("Ingrese el teléfono: ")
        return codigo, nombre, direccion, telefono

# esta función selecciona una personas
    def seleccionarPersona(self):
        codigo = input("Ingrese el codigo de la persona a seleccionar: ")
        return codigo

    def mostrarMensaje(self, mensaje):
        print(mensaje)


