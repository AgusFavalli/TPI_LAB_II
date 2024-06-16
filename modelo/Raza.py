class Raza:
    def __init__(self,codigo, nombre):
        self._codigo= codigo
        self._nombre= nombre

    def getCodigo(self):
        return self._codigo

    def getNombre(self):
        return self._nombre

    def __str__(self):
        return f"{self.getCodigo()}- {self.getNombre()}"