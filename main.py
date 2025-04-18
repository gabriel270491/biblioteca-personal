from biblioteca_personal.database import Base, engine
from biblioteca_personal.modelos import Libro
from biblioteca_personal.operaciones import agregar_libro, actualizar_libro, eliminar_libro, ver_libros, buscar_libros

def crear_tablas():
    Base.metadata.create_all(bind=engine)

def menu():
    print("\n--- Biblioteca Personal ---")
    print("1. Agregar nuevo libro")
    print("2. Actualizar información de un libro")
    print("3. Eliminar libro existente")
    print("4. Ver listado de libros")
    print("5. Buscar libros")
    print("6. Salir")

def main():
    crear_tablas()
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            actualizar_libro()
        elif opcion == "3":
            eliminar_libro()
        elif opcion == "4":
            ver_libros()
        elif opcion == "5":
            buscar_libros()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
