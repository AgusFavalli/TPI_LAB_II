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

    def getvacunas(self):
        return self.vacunas

    def getFecha(self):
        return self.fecha

    def toDict(self):
        return {
            'fecha': self.fecha,
            'tratamiento': self.tratamiento,
            'veterinario': self.veterinario,
            'diagnosticos': self.diagnosticos,
            'vacunas': self.vacunas
        }

    def __str__(self):
        return f"{self.getTratamientos()}, {self.getVeterinario()}, {self.getDiagnosticos()}, {self.getvacunas()}, {self.getFecha()}"

    def __repr__(self):
        return f"{self.getTratamientos()}, {self.getVeterinario()}, {self.getDiagnosticos()}, {self.getvacunas()}, {self.getFecha()}"