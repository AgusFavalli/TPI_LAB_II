class FichaMedica:
    def __init__(self, fecha, tratamiento, veterinario, diagnosticos, vacunas):
        self.fecha = fecha
        self.tratamiento = tratamiento
        self.veterinario = veterinario
        self.diagnosticos = diagnosticos
        self.vacunas = vacunas

    def getTratamientos(self):
        return self.tratamiento

    def getVeterinario(self):
        return self.veterinario

    def getDiagnosticos(self):
        return self.diagnosticos

    def getVacunas(self):
        return self.vacunas

    def getFecha(self):
        return self.fecha



    def __str__(self):
        return f"{self.getFecha()}, {self.getTratamientos()}, {self.getVeterinario()}, {self.getDiagnosticos()}, {self.getVacunas()}"

    def __repr__(self):
        return f"{self.getFecha()}, {self.getTratamientos()}, {self.getVeterinario()}, {self.getDiagnosticos()}, {self.getVacunas()}"
 