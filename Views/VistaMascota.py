class Mascota:
    def __init__(self,codigo, nombre, especie, raza, propietario):
        self._codigo= codigo
        self._nombre= nombre
        self._especie = especie
        self._raza= raza
        self._propietario= propietario

#SETTERS
    #Setters
    #Se retorna un booleano para usar desde el controller llamando a la vista para imprimir un mensaje
    def set_name(self, name):
        if type(name) == str:
            self._name = name
            return True
        else:
            return False 

    def set_dni(self, dni):
        if type(dni) == str and dni.isnumeric() and len(dni) == 8:
            self._dni = dni
            return True
        else:
            return False



#GETTERS
    def getCodigo(self):
        return self._codigo

    def getNombre(self):
        return self._nombre

    def getEspecie(self):
        return self._especie

    def getRaza(self):
        return self._raza

    def getPropietario(self):
        return self._propietario

    def isActivas(self):
        return self._codigo == "1"

    def __str__(self):
        return f"{self.getCodigo()},{self.getNombre()}, {self.getEspecie()},{self.getRaza()},{self.getPropietario()} "

    def __repr__(self):
        return f"{self.getCodigo()}, {self.getNombre()},{self.getEspecie()},{self.getRaza()},{self.getPropietario()}"