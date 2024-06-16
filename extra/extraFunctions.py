#Se importa este módulo para verificar el SO del usuario
import os

#Dependiendo del SO, cls limpia la pantalla en windows y clear en linux
def clearScreen(): 
    os.system("cls" if os.name == "nt" else "clear")

#La funcion getch() del modulo msvcrt espera el ingreso de una tecla sin retornarla. En linux se configura la terminal en modo RAW y leer un caracter con la funcion sys.stdin.read(1)
def waitKey():
    if os.name == "nt": #Para Windows
        import msvcrt
        msvcrt.getch()
    