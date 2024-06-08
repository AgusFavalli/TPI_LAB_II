from Prueba_repositorio.controlador.ControladorMascotas import ControladorMascotas

def inicio():
    controlador = ControladorMascotas()
    controlador.menu()

if __name__ =="__main__":
    inicio()