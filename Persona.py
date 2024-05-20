class Persona:
  def __init__(self, nombre, apellido, telefono, tipo):
    self.nombre = nombre
    self.apellido = apellido
    self.telefono = telefono
    self.tipo = tipo  # Propietario o Veterinario

  def datos_completos(self):
    return f"{self.nombre} {self.apellido} ({self.telefono}) - {self.tipo}"    

  def __str__(self):
    return f"{self.nombre} {self.apellido}"    
  