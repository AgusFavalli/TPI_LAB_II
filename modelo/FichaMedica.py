class FichaMedica:
    def __init__(self, fecha, tratamiento, veterinario, diagnosticos, vacunas):
        # Inicializa los atributos de la ficha médica
        self.fecha = fecha
        self.tratamiento = tratamiento
        self.veterinario = veterinario
        self.diagnosticos = diagnosticos
        self.vacunas = vacunas

    def getTratamientos(self):
        # Devuelve el tratamiento
        return self.tratamiento

    def getVeterinario(self):
        # Devuelve el veterinario
        return self.veterinario

    def getDiagnosticos(self):
        # Devuelve los diagnósticos
        return self.diagnosticos

    def getVacunas(self):
        # Devuelve las vacunas
        return self.vacunas

    def setTratamiento(self, tratamiento):
        # Establece un nuevo tratamiento
        self.tratamiento = tratamiento

    def setVeterinario(self, veterinario):
        # Establece un nuevo veterinario
        self.veterinario = veterinario

    def setDiagnosticos(self, diagnosticos):
        # Establece nuevos diagnósticos
        self.diagnosticos = diagnosticos

    def setVacunas(self, vacunas):
        # Establece nuevas vacunas
        self.vacunas = vacunas

    def __str__(self):
        # Representación en cadena de la ficha médica
        return f"Fecha: {self.fecha}, Tratamiento: {self.tratamiento}, Veterinario: {self.veterinario}, Diagnósticos: {self.diagnosticos}, Vacunas: {self.vacunas}"

    def __repr__(self):
        return f"{self.getFecha()}, {self.getTratamientos()}, {self.getVeterinario()}, {self.getDiagnosticos()}, {self.getVacunas()}"
