class Vacuna:
    def __init__(self, codigo, nombre, descripcion):
        self._codigo= codigo
        self._nombre= nombre
        self._descripcion= descripcion

    def getCodigo(self):
        return self._codigo

    def getNombre(self):
        return self._nombre

    def getDescripcion(self):
        return self._descripcion

    def setNombre(self,vacuna):
        self._nombre = vacuna

    def getDatosVacunas(self):
        return self.getNombre(), self.getDescripcion()

    def __str__(self):
        return f"{self.getCodigo()}, {self.getNombre()}, {self.getDescripcion()}"

    def __repr__(self):
        return f"{self.getCodigo()}, {self.getNombre()}, {self.getDescripcion()}"