import os

def anadir_coche():
    ruta = r"C:\Users\Usuario\Desktop\Inventory management system\Lista_coches.txt"
    
    marca = input("Agregar marca: ")
    modelo = input("Agregar modelo: ")
    
    with open(ruta, "a", encoding="utf-8") as archivo:
        archivo.write(f"Modelo: {modelo}, Marca: {marca}\n")
    
    print("Coche añadido correctamente.")

while True:
    print("\nMenú")
    print("-------------")
    print("1. Agregar nuevo vehículo")
    print("2. Abrir lista de vehículos")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        anadir_coche()
    elif opcion == "2":
        ruta = r"C:\Users\Usuario\Desktop\Inventory management system\Lista_coches.txt"
        os.system(f'notepad "{ruta}"')
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
