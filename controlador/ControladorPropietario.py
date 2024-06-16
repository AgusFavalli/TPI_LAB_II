from vista.VistaGeneral import VistaGeneral
from modelo.Propietario import Propietario

class ControladorPropietario:
    def __init__(self):
        self.vista= VistaGeneral()
        self.listaPropietarios=[]

    def cargarArchivoPropietarios(self):
        with open("archivos/propietarios.txt") as archivo:
            for linea in archivo.readlines():
                nombre, direccion, telefono, codigo, numMascota= linea.strip().split(",")
                self.listaPropietarios.append(Propietario(nombre, direccion, telefono, codigo, numMascota))


    def buscarObjeto(self,propietario):
        for i in self.listaPropietarios:
            if i.getCodigo() == propietario:
                return i