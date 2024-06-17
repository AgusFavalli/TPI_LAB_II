class FichaMedica:
    def __init__(self,codigo, mascota, veterinario, fecha):
        self._codigo=codigo
        self._mascota= mascota
        self._veterinario= veterinario
        self._diagnosticos= []
        self._fecha= fecha

    def getCodigo(self):
        return self._codigo

    def getMascota(self):
        return self._mascota

    def getVeterinario(self):
        return self._veterinario

    def getDiagnosticos(self):
        return self._diagnosticos

    def getFecha(self):
        return self._fecha


    def __str__(self):
        return f"{self.getMascota()}, {self.getVeterinario()}, {self.getDiagnosticos()}, {self.getFecha()}"

    def __repr__(self):
        return f"{self.getMascota()}, {self.getVeterinario()}, {self.getDiagnosticos()}, {self.getFecha()}"