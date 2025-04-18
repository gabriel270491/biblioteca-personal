from .modelos import Libro
from .database import SessionLocal

def agregar_libro():
    session = SessionLocal()
    try:
        titulo = input("Título: ")
        autor = input("Autor: ")
        genero = input("Género: ")
        estado = input("Estado (leído/no leído): ")
        nuevo_libro = Libro(titulo=titulo, autor=autor, genero=genero, estado=estado)
        session.add(nuevo_libro)
        session.commit()
        print("Libro agregado correctamente.")
    except Exception as e:
        session.rollback()
        print("Error al agregar libro:", e)
    finally:
        session.close()

def actualizar_libro():
    session = SessionLocal()
    try:
        ver_libros()
        id_libro = int(input("ID del libro a actualizar: "))
        campo = input("Campo a actualizar (titulo, autor, genero, estado): ")
        nuevo_valor = input("Nuevo valor: ")
        libro = session.query(Libro).filter(Libro.id == id_libro).first()
        if libro:
            setattr(libro, campo, nuevo_valor)
            session.commit()
            print("Libro actualizado correctamente.")
        else:
            print("Libro no encontrado.")
    except Exception as e:
        session.rollback()
        print("Error al actualizar libro:", e)
    finally:
        session.close()

def eliminar_libro():
    session = SessionLocal()
    try:
        ver_libros()
        id_libro = int(input("ID del libro a eliminar: "))
        libro = session.query(Libro).filter(Libro.id == id_libro).first()
        if libro:
            session.delete(libro)
            session.commit()
            print("Libro eliminado correctamente.")
        else:
            print("Libro no encontrado.")
    except Exception as e:
        session.rollback()
        print("Error al eliminar libro:", e)
    finally:
        session.close()

def ver_libros():
    session = SessionLocal()
    try:
        libros = session.query(Libro).all()
        print("\n--- Lista de Libros ---")
        for libro in libros:
            print(f"ID: {libro.id}, Título: {libro.titulo}, Autor: {libro.autor}, Género: {libro.genero}, Estado: {libro.estado}")
        if not libros:
            print("No hay libros en la base de datos.")
    except Exception as e:
        print("Error al ver libros:", e)
    finally:
        session.close()

def buscar_libros():
    session = SessionLocal()
    try:
        criterio = input("Buscar por (titulo, autor, genero): ")
        valor = input(f"Ingrese el {criterio}: ")
        libros = session.query(Libro).filter(getattr(Libro, criterio).ilike(f"%{valor}%")).all()
        print("\n--- Resultados de la búsqueda ---")
        for libro in libros:
            print(f"ID: {libro.id}, Título: {libro.titulo}, Autor: {libro.autor}, Género: {libro.genero}, Estado: {libro.estado}")
        if not libros:
            print("No se encontraron resultados.")
    except Exception as e:
        print("Error en la búsqueda:", e)
    finally:
        session.close()
