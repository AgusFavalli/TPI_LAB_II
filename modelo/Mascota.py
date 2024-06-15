class Mascota:
    def __init__(self,codigo, nombre, especie, raza, propietario):
        self._codigo= codigo
        self._nombre= nombre
        self._especie = especie
        self._raza= raza
        self._propietario= propietario

    def getCodigo(self):
        return self._codigo

    def getNombre(self):
        return self._nombre

    def getEspecie(self):
        return self._especie

    def getRaza(self):
        return self._raza

    def getPropietario(self):
        return self._propietario

    def isActivas(self):
        return self._codigo == "1"

    def __str__(self):
        return f"{self.getCodigo()},{self.getNombre()}, {self.getEspecie()},{self.getRaza()},{self.getPropietario()} "

    def __repr__(self):
        return f"{self.getCodigo()}, {self.getNombre()},{self.getEspecie()},{self.getRaza()},{self.getPropietario()}"
