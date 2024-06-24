from vista.VistaDiagnostico import VistaDiagnostico
from modelo.Diagnostico import Diagnostico

class ControladorDiagnostico:
    def __init__(self,controladorTratamiento, controladorVacunas):
        self.vista = VistaDiagnostico()
        self.listaDiagnosticos = []
        self.controladorTratamiento= controladorTratamiento
        self.controladorVacunas= controladorVacunas


    def cargarArchivoDiagnosticos(self):
        self.listaDiagnosticos = []  # Reiniciar la lista de diagnósticos
        self.contadorDiagnostico = {}  # Reiniciar el contador de diagnósticos
        with open("archivos/diagnosticos.txt", encoding="utf-8") as archivo:
            for linea in archivo.readlines():
                codigo, descripcion, tratamientos, vacunas = linea.strip().split(",")
                objTratamientos = self.controladorTratamiento.buscarObjetoTratamiento(tratamientos)
                objVacunas= self.controladorVacunas.buscarObjeto(vacunas)
                diagnostico= Diagnostico(codigo, descripcion)
                if objTratamientos:
                    diagnostico.registrarTratamiento(f"Tratamiento: {objTratamientos}")
                if objVacunas == None:
                    diagnostico.registrarVacuna("Vacunas: no se requieren vacunas")
                else:
                    diagnostico.registrarVacuna(f"Vacunas: {objVacunas}")
                self.listaDiagnosticos.append(diagnostico)

    def actualizarArchivoDiagnostico(self):
        with open("archivos/diagnosticos.txt", "w", encoding="utf-8") as archivo:
            for diagnostico in self.listaDiagnosticos:
                archivo.write(f"{diagnostico.getCodigo()}, {diagnostico.getDescripcion()}, {diagnostico.getVacunas()}, {diagnostico.getTratamientos()}\n")

    def buscarObjeto(self,diagnostico):
        for i in self.listaDiagnosticos:
            if str(i.getCodigo()) == diagnostico:
                return i

    def listadoDiagnosticos(self):
        self.vista.mostrarLista(self.listaDiagnosticos)

    def agregarDiagnostico(self):
        codigo = len(self.listaDiagnosticos) + 1
        descripcion, tratamiento, vacunas = self.vista.obtenerDiagnostico()
        nuevoDiagnostico= Diagnostico(codigo, descripcion)
        nuevoDiagnostico.registrarTratamiento(tratamiento)
        nuevoDiagnostico.registrarVacuna(vacunas)
        self.listaDiagnosticos.append(nuevoDiagnostico)
        with open('archivos/diagnosticos.txt', 'a', encoding="utf-8") as file:
            file.write(f"{codigo},{descripcion},{tratamiento},{vacunas}\n")
        self.vista.mostrarMensaje("Diagnostico agregado con éxito.")
        self.actualizarArchivoDiagnostico()

    def modificarDiagnostico(self):
        self.listadoDiagnosticos()
        diagnostico_actual, nuevo_diagnostico= self.vista.modificarDiagnostico()
        diagnostico_modificar= self.buscarObjeto(diagnostico_actual)
        if diagnostico_modificar:
            diagnostico_modificar.setDescripcion(nuevo_diagnostico)
            self.vista.mostrarMensaje("El diagnostico fue modificado con exito")
            with open('archivos/diagnosticos.txt', 'w', encoding="utf-8") as file:
                for diagnostico in self.listaDiagnosticos:
                    objVacuna= self.controladorVacunas.buscarNombreVacuna(diagnostico.getVacunas())
                    objTratamiento= self.controladorTratamiento.buscarNombreTratamiento(diagnostico.getTratamientos())
                    if not objVacuna:
                        self.controladorVacunas.agregarVacuna()
                        self.ejecutarMenuDiagnosticos()
                    if not objTratamiento:
                        self.controladorTratamiento.agregarTratamiento()
                        self.ejecutarMenuDiagnosticos()
                    self.actualizarArchivoDiagnostico()

    def eliminarDiagnostico(self):
        self.vista.mostrarLista(self.listaDiagnosticos)
        codigo = self.vista.eliminarDiagnostico()
        diagnosticoEncontrado = False
        for i in self.listaDiagnosticos:
            if str(i.getCodigo()) == codigo:
                self.listaDiagnosticos.remove(i)
                self.actualizarArchivoDiagnostico()
                self.vista.mostrarMensaje("diagnostico eliminado")
                diagnosticoEncontrado= True
                break
            else:
                self.vista.mostrarMensaje("diagnostico no encontrado")

    def ejecutarMenuDiagnosticos(self):
        opcion = self.vista.mostrarMenuDiagnosticos()
        while True:
            if opcion == "1":  # 1- mostrar listado de diagnosticos
                self.listadoDiagnosticos()
            elif opcion == "2":  # 2- agregar diagnosticos
                self.agregarDiagnostico()
            elif opcion == "3":  # 3- modificar diagnosticos
                self.modificarDiagnostico()
            elif opcion == "4":  # 4- eliminar diagnosticos
                self.eliminarDiagnostico()
            elif opcion == "5":  # 6- salir
                self.vista.mostrarMensaje("Volviendo al menu principal...")
                return
            else:
                print("Opción inválida. Por favor, intente nuevamente.\n")
            opcion = self.vista.mostrarMenuDiagnosticos()
