class FichaMedica:
    def __init__(self, fecha, tratamiento, veterinario, diagnosticos, vacunas):
        # Inicializa los atributos de la ficha médica
        self.fecha = fecha
        self._tratamiento = tratamiento
        self._veterinario = veterinario
        self._diagnosticos = diagnosticos
        self._vacunas = vacunas

    def getFecha(self):
        return self.fecha
    def getTratamientos(self):
        # Devuelve el tratamiento
        return self._tratamiento

    def getVeterinario(self):
        # Devuelve el veterinario
        return self._veterinario

    def getDiagnosticos(self):
        # Devuelve los diagnósticos
        return self._diagnosticos

    def getVacunas(self):
        # Devuelve las vacunas
        return self._vacunas

    def setTratamiento(self, tratamiento):
        # Establece un nuevo tratamiento
        self._tratamiento = tratamiento

    def setVeterinario(self, veterinario):
        # Establece un nuevo veterinario
        self._veterinario = veterinario

    def setDiagnosticos(self, diagnosticos):
        # Establece nuevos diagnósticos
        self._diagnosticos = diagnosticos

    def setVacunas(self, vacunas):
        # Establece nuevas vacunas
        self._vacunas = vacunas

    def __str__(self):
        # Representación en cadena de la ficha médica
        return f"Fecha: {self.getFecha()}, Tratamiento: {self.getTratamientos()}, Veterinario: {self.getVeterinario()}, Diagnósticos: {self.getDiagnosticos()}, Vacunas: {self.getVacunas()}"

    def __repr__(self):
        return f"{self.getFecha()}, {self.getTratamientos()}, {self.getVeterinario()}, {self.getDiagnosticos()}, {self.getVacunas()}"
