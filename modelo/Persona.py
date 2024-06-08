class Persona:
    def __init__(self, nombre="", telefono=0, codigo=0):
        self._nombre = nombre
        self._telefono = telefono
        self._codigo=codigo

    def getNombre(self):
        return self._nombre
    
    def getTelefono(self):
        return self._telefono
    
    def getCodigo(self):
        return self._codigo
    
    def setNombre(self, dato):
        self._nombre = dato

    def setTelefono(self, dato):
        self._telefono = dato

    def setCodigo(self, dato):
        self._codigo = dato

    def __str__(self):
        return f"{self.getNombre()} - {self.getTelefono()} - {self.getCodigo()}"


class Propietarios(Persona):
    def __init__(self, nombre, telefono, codigo):
        super().__init__(nombre, telefono, codigo)


class Veterinario(Persona):
    def __init__(self, nombre, telefono, codigo):
        super().__init__(nombre, telefono, codigo)

