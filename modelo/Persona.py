class Persona:
    def __init__(self,codigo, nombre, direccion, telefono):
        self._codigo = codigo
        self._nombre = nombre
        self._direccion= direccion
        self._telefono = telefono

    def getCodigo(self):
        return self._codigo

    def getNombre(self):
        return self._nombre

    def getDireccion(self):
        return self._direccion

    def getTelefono(self):
        return self._telefono
    
    def setNombre(self, dato):
        self._nombre = dato

    def setTelefono(self, dato):
        self._telefono = dato

    def setCodigo(self, dato):
        self._codigo = dato

    def __str__(self):
        return f"{self.getCodigo()},{self.getNombre()}, {self.getDireccion()}, {self.getTelefono()}"

    def __repr__(self):
        return f"{self.getCodigo()},{self.getNombre()}, {self.getDireccion()}, {self.getTelefono()}"

class Veterinario(Persona):
    def __init__(self, codigo, nombre, direccion, telefono):
        super().__init__(codigo, nombre, direccion, telefono)

class Propietario(Persona):
    def __init__(self, codigo, nombre, direccion, telefono, numMascota):
        super().__init__(codigo, nombre, direccion, telefono)
        self._numMascota = numMascota

    def getMascota(self):
        return self._numMascota

    def __str__(self):
        return super().__str__() + f", num mascota: {self.getMascota()}"

    def __repr__(self):
        return super().__str__()