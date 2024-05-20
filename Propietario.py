from Persona import Persona

class Propietario(Persona):
    def __init__(self, nombre, apellido, telefono):
        super().__init__(nombre, apellido, telefono, "Propietario")

    def __str__(self):
        return f"{super().__str__()}"