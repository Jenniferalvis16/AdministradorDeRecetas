from pathlib import Path
import os
from os import system

# Ruta base donde se encuentran las recetas
mi_ruta = Path("C:/Users/Jenni/Desktop/Curso Python/Curso/AdministradordeRecetas/Recetas")

# Función para contar recetas en todas las subcarpetas
def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador

# Función para limpiar la pantalla (compatible con Windows y otros sistemas)
def limpiar_pantalla():
    system('cls' if os.name == 'nt' else 'clear')

# Función para mostrar las categorías disponibles
def mostrar_categorias():
    categorias = [carpeta for carpeta in mi_ruta.iterdir() if carpeta.is_dir()]
    print("\nCategorías disponibles:")
    for i, carpeta in enumerate(categorias, 1):
        print(f"{i}. {carpeta.name}")
    return categorias

# Función para elegir una categoría
def elegir_categoria():
    categorias = mostrar_categorias()
    while True:
        try:
            eleccion = int(input("Elige una categoría por número: "))
            if 1 <= eleccion <= len(categorias):
                return categorias[eleccion - 1]
            else:
                print("Error: Elige un número válido.")
        except ValueError:
            print("Error: Ingresa un número válido.")

# Función para leer recetas
def leer_receta():
    categoria = elegir_categoria()
    recetas = list(categoria.glob("*.txt"))
    if not recetas:
        print("Esta categoría no tiene recetas.")
        return
    print("\nRecetas disponibles:")
    for i, receta in enumerate(recetas, 1):
        print(f"{i}. {receta.name}")
    while True:
        try:
            eleccion = int(input("Elige una receta por número: "))
            if 1 <= eleccion <= len(recetas):
                with open(recetas[eleccion - 1], "r", encoding="utf-8") as archivo:
                    print("\nContenido de la receta:")
                    print("-" * 50)
                    print(archivo.read())
                    print("-" * 50)
                break
            else:
                print("Error: Elige un número válido.")
        except ValueError:
            print("Error: Ingresa un número válido.")

# Función para crear una nueva receta
def crear_receta():
    categoria = elegir_categoria()
    nombre_receta = input("Ingresa el nombre de la nueva receta: ") + ".txt"
    contenido = input("Escribe el contenido de la receta:\n")
    ruta_receta = categoria / nombre_receta
    with open(ruta_receta, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)
    print(f"\nReceta '{nombre_receta}' creada con éxito en la categoría '{categoria.name}'.")

# Función para eliminar una receta
def eliminar_receta():
    categoria = elegir_categoria()
    recetas = list(categoria.glob("*.txt"))
    if not recetas:
        print("Esta categoría no tiene recetas para eliminar.")
        return
    print("\nRecetas disponibles:")
    for i, receta in enumerate(recetas, 1):
        print(f"{i}. {receta.name}")
    while True:
        try:
            eleccion = int(input("Elige una receta para eliminar por número: "))
            if 1 <= eleccion <= len(recetas):
                recetas[eleccion - 1].unlink()
                print(f"\nReceta '{recetas[eleccion - 1].name}' eliminada con éxito.")
                break
            else:
                print("Error: Elige un número válido.")
        except ValueError:
            print("Error: Ingresa un número válido.")

# Función principal del programa
def inicio():
    while True:
        limpiar_pantalla()
        print('*' * 50)
        print('*' * 5 + " Bienvenido al administrador de recetas " + '*' * 5)
        print('*' * 50)
        print(f"\nLas recetas se encuentran en: {mi_ruta}")
        print(f"Total recetas: {contar_recetas(mi_ruta)}")
        print("\nMenú:")
        print("1. Leer receta")
        print("2. Crear nueva receta")
        print("3. Eliminar receta")
        print("4. Salir\n")

        try:
            opcion = int(input("Elige una opción (1-4): "))
            if opcion == 1:
                leer_receta()
            elif opcion == 2:
                crear_receta()
            elif opcion == 3:
                eliminar_receta()
            elif opcion == 4:
                print("\nGracias por usar el administrador de recetas. ¡Hasta pronto!")
                break
            else:
                print("Error: La opción debe estar entre 1 y 4.")
        except ValueError:
            print("Error: Ingresa un número válido.")
        input("\nPresiona Enter para continuar...")

# Llamar a la función de inicio
if __name__ == "__main__":
    if not mi_ruta.exists():
        print("La ruta de recetas no existe. Verifica la ruta y vuelve a intentarlo.")
    else:
        inicio()

