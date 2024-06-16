#Se importa el controlador
from Controllers.ControllerGeneral import ControllerGeneral

#En esta funcion definimos el controller y invocamos unicamente a su función main(). Desde allí se maneja todo el sistema.
def main():
    controller = ControllerGeneral()
    controller.menu()

if __name__ == "__main__":
    main()

    