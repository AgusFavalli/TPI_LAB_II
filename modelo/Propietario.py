class Propietario:
    def __init__(self, nombre, direccion, telefono, codigo, numMascota):
        self._nombre = nombre
        self._direccion= direccion
        self._telefono = telefono
        self._codigo=codigo
        self._numMascota= numMascota

    def getNombre(self):
        return self._nombre

    def getDireccion(self):
        return self._direccion

    def getTelefono(self):
        return self._telefono
    
    def getCodigo(self):
        return self._codigo

    def getNumMascota(self):
        return self.getNumMascota
    
    def setNombre(self, dato):
        self._nombre = dato

    def setTelefono(self, dato):
        self._telefono = dato

    def setCodigo(self, dato):
        self._codigo = dato



    def __str__(self):
        return f"{self.getNombre()}, {self.getDireccion()}, {self.getTelefono()}, {self.getCodigo()}"

    def __repr__(self):
        return f"{self.getNombre()}, {self.getDireccion()}, {self.getTelefono()}, {self.getCodigo()}"




