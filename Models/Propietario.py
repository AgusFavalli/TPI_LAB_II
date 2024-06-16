class Propietario:
    def __init__(self, nombre, direccion, telefono, codigo, numMascota):
        self._nombre = nombre
        self._direccion= direccion
        self._telefono = telefono
        self._codigo=codigo
        self._numMascota= numMascota



#SETTERS
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not isinstance(value, str):
            raise ValueError("El nombre debe ser una cadena de caracteres")
        self._nombre = value
#.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-
    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, value):
        if not value.isdigit() or len(value) != 8:
            raise ValueError("El DNI debe ser un número de 8 dígitos")
        self._dni = value
#.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-
    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, value):
        if not value.isdigit():
            raise ValueError("El teléfono debe ser un número")
        self._telefono = value
#.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-
    @property
    def direccion(self):
        return self._direccion
#.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-
    @direccion.setter
    def direccion(self, value):
        if not isinstance(value, str):
            raise ValueError("La dirección debe ser una cadena de caracteres")
        self._direccion = value
#.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-
    def setCodigo(self, dato):
        self._codigo = dato
#.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-
    def setNumMascota(self, dato):
        self._numMascota = dato

# GETTERS
   
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
    
#.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-
    def __str__(self):
        return f"{self.getNombre()}, {self.getDireccion()}, {self.getTelefono()}, {self.getCodigo()}"

    def __repr__(self):
        return f"{self.getNombre()}, {self.getDireccion()}, {self.getTelefono()}, {self.getCodigo()}"