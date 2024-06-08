class Mascota:
    def __init__(self, nombre="", edad=0, fechaNacimiento=0, estado=0, raza):
        self._nombre= nombre
        self._edad = edad
        self._fechaNacimiento = fechaNacimiento
        self._estado = estado
        self._raza = raza    #boxer,labrador,etc


    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getFechaNacimiento(self):
        return self._fechaNacimiento

    def getEstado(self):
        return self._estado

    def getRaza(self):
        return self._raza

    def isActivas(self):
        return self.getEstado() == 1

    def __str__(self):
        return f"nombre: {self.getNombre()}, edad: {self.getEdad()}, estado: {self.getEstado()}, fecha nacimiento:{self.getFechaNacimiento()}, raza: {self.getRaza()}"


