from Persona import Persona

class Veterinario(Persona):
  def __init__(self, nombre, apellido, telefono):
    super().__init__(nombre, apellido, telefono, "Veterinario")

  def __str__(self):
    return f"{super().__str__()}"