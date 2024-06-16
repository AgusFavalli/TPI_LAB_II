class Diagnostico:
    def __init__(self, codigo, nombre, observaciones, mascota):
        self.codigo = codigo
        self.nombre = nombre
        self.observaciones = observaciones
        self.mascota = mascota


    def __str__(self):
        return f"Diagnostico(codigo={self.codigo}, nombre={self.nombre}, observaciones={self.observaciones}, mascota={self.mascota})"
