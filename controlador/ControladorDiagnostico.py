from vista.VistaGeneral import VistaGeneral
from modelo.Diagnostico import Diagnostico

class ControladorDiagnostico:
    def __init__(self,controladorTratamiento, controladorVacunas):
        self.vista = VistaGeneral()
        self.listaDiagnosticos = []
        self.controladorTratamiento= controladorTratamiento
        self.controladorVacunas= controladorVacunas


    def cargarArchivoDiagnosticos(self):
        with open("archivos/diagnosticos.txt", encoding="utf-8") as archivo:
            for linea in archivo.readlines():
                codigo, descripcion, tratamientos, vacunas = linea.strip().split(",")
                objTratamientos = self.controladorTratamiento.buscarObjetoTratamiento(tratamientos)
                objVacunas= self.controladorVacunas.buscarObjetoVacuna(vacunas)
                diagnostico= Diagnostico(codigo, descripcion)
                if objTratamientos:
                    diagnostico.registrarTratamiento(f"Tratamiento: {objTratamientos}")
                if objVacunas == None:
                    diagnostico.registrarVacuna("Vacunas: no se requieren vacunas")
                else:
                    diagnostico.registrarVacuna(f"Vacunas: {objVacunas}")
                self.listaDiagnosticos.append(diagnostico)

    def buscarObjeto(self,diagnostico):
        for i in self.listaDiagnosticos:
            if i.getCodigo() == diagnostico:
                return i

    def listadoDiagnosticos(self):
        self.vista.mostrarLista(self.listaDiagnosticos)