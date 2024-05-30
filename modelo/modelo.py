class Persona:
    def __init__(self, nombre="", telefono=int, email="", direccion=""):
        self._nombre = nombre
        self._telefono = telefono
        self._email = email
        self._direccion = direccion

    def getNombre(self):
        return self._nombre
    
    def getTelefono(self):
        return self._telefono
    
    def getEmail(self):
        return self._email
    
    def getDireccion(self):
        return self._direccion
    
    def setNombre(self, dato):
        self._nombre = dato

    def setTelefono(self, dato):
        self._telefono = dato

    def setEmail(self, dato):
        self._email = dato

    def setDireccion(self, dato):
        self._direccion = dato

    def __str__(self):
        return str (self._dni) + " - " + self._nombre + self._email + self._direccion