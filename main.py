from Mascota import Mascota
from Raza import Raza
from Persona import Persona
from Propietario import Propietario
from Veterinario import Veterinario

def main():
  razas = []
  propietarios = []
  veterinarios = []
  mascotas = []

  while True:
    print("\nSISTEMA VETERINARIA\n")
    print("1- Registrar Raza en el Sistema")
    print("2- Registrar Persona en el Sistema")
    print("3- Registrar Veterinario en el Sistema")
    print("4- Registrar Mascota en el Sistema")
    print("5- Mostar Mascotas en el Sistema")
    print("5- Salir")

    opcion = input("\nSeleccione una opcion:\n")

    if opcion == "1":
      nombre_raza = input("\nIngrese el nombre de la raza:\n")
      raza = Raza(nombre_raza)
      razas.append(raza)
      print(f"\nRaza {nombre_raza} agregada.")

    elif opcion == "2":
      nombre = input("\nIngrese su nombre:\n")
      apellido = input("\nIngrese su apellido:\n")
      telefono = input("\nIngrese su telefono:\n")
      propietario = Propietario(nombre, apellido, telefono)
      propietarios.append(propietario)
      print(f"\n{nombre} {apellido} agregado/a como Propietario.")

    elif opcion == "3":
      nombre = input("\nIngrese su nombre:\n")
      apellido = input("\nIngrese su apellido:\n")
      telefono = input("\nIngrese su telefono:\n")
      veterinario = Veterinario(nombre, apellido, telefono)
      veterinarios.append(veterinario)
      print(f"\n{nombre} {apellido} agregado como Veterinario.")
      
    elif opcion == "4":
      nombre_mascota = input("\nNombre de la mascota: ")
      especie = input("\nIngrese su especie: ")
      print("\nRazas disponibles:")
      for i, raza in enumerate(razas, 1):
        print(f"{i}. {raza}")
      raza_index = int(input("\nSeleccione la raza de la mascota: ")) - 1
      raza_mascota = razas[raza_index]
      print("\nPropietarios disponibles:")
      for i, propietario in enumerate(propietarios, 1):
        if propietario.tipo == "Propietario":
          print(f"{i}. {propietario}")
      propietario_index = int(input("\nSeleccione el propietario de la mascota: ")) - 1
      propietario_mascota = propietarios[propietario_index]
      mascota = Mascota(nombre_mascota, especie, raza_mascota, propietario_mascota)
      mascotas.append(mascota)
      print(f"Mascota '{nombre_mascota}' agregada.")

    elif opcion == '5':
      print("\nListado de Mascotas:")
      for mascota in mascotas:
        print("-" * 30) # Separador visual entre mascotas
        print(f"Nombre: {mascota.nombre_mascota}")
        print(f"Especie: {mascota.especie}")
        print(f"Raza: {mascota.raza.nombre_raza}")
        print(f"Propietario: {mascota.propietario.nombre} {mascota.propietario.apellido}")
        print(f"Telefono: {mascota.propietario.telefono}")

    elif opcion == '5':
      print("Saliendo del programa...")
      break

    else:
      print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
  main()