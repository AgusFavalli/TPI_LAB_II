class Diagnostico:
    def __init__(self, codigo, descripcion):
        self._codigo= codigo
        self._descripcion= descripcion
        self._tratamientos = []
        self._vacunas= []

    def getCodigo(self):
        return self._codigo

    def getDescripcion(self):
        return self._descripcion

    def registrarVacuna(self, vacuna):
        self._vacunas.append(vacuna)

    def registrarTratamiento(self, tratamiento):
        self._tratamientos.append(tratamiento)

    def getVacunas(self):
        return self._vacunas

    def getTratamientos(self):
        return self._tratamientos

    def __str__(self):
        return f"{self.getCodigo()}- {self.getDescripcion()}, {self.getTratamientos()}, {self.getVacunas()}"

    def __repr__(self):
        return f"{self.getCodigo()}- {self.getDescripcion()}, {self.getTratamientos()}, {self.getVacunas()}"