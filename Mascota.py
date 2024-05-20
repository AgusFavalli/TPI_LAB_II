class Mascota():
  def __init__(self, nombre_mascota, especie, raza, propietario):
    self.nombre_mascota = nombre_mascota
    self.especie = especie
    self.raza = raza
    self.propietario = propietario

  def __str__(self):
    return f"{self.nombre_mascota} {self.especie} {self.raza} {self.propietario}"
  
  def __repr__(self):
    return f"{self.nombre_mascota} {self.especie} {self.raza} {self.propietario}"
    