import sqlite3
from biblioteca import crear_tabla, agregar_libro, actualizar_libro, eliminar_libro, ver_libros, buscar_libros

def menu():
    print("\n--- Biblioteca Personal ---")
    print("1. Agregar nuevo libro")
    print("2. Actualizar información de un libro")
    print("3. Eliminar libro existente")
    print("4. Ver listado de libros")
    print("5. Buscar libros")
    print("6. Salir")

def main():
    conexion = sqlite3.connect("biblioteca.db")
    crear_tabla(conexion)

    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_libro(conexion)
        elif opcion == "2":
            actualizar_libro(conexion)
        elif opcion == "3":
            eliminar_libro(conexion)
        elif opcion == "4":
            ver_libros(conexion)
        elif opcion == "5":
            buscar_libros(conexion)
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

    conexion.close()

if __name__ == "__main__":
    main()