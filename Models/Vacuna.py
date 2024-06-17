# Clase Vacuna que representa una vacuna con sus atributos.
class Vacuna:
    def __init__(self, codigoVacuna, nombre, fabricante, observaciones):
        self.codigoVacuna = codigoVacuna
        self.nombre = nombre
        self.fabricante = fabricante
        self.observaciones = observaciones

    def __str__(self):
        return f"{self.codigoVacuna};{self.nombre};{self.fabricante};{self.observaciones}"
