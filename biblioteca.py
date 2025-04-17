def crear_tabla(conexion):
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            genero TEXT NOT NULL,
            estado TEXT NOT NULL
        )
    ''')
    conexion.commit()

def agregar_libro(conexion):
    titulo = input("Título: ")
    autor = input("Autor: ")
    genero = input("Género: ")
    estado = input("Estado (leído/no leído): ")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO libros (titulo, autor, genero, estado) VALUES (?, ?, ?, ?)",
                   (titulo, autor, genero, estado))
    conexion.commit()
    print("Libro agregado correctamente.")

def actualizar_libro(conexion):
    ver_libros(conexion)
    id_libro = input("ID del libro a actualizar: ")
    campo = input("Campo a actualizar (titulo, autor, genero, estado): ")
    nuevo_valor = input("Nuevo valor: ")
    cursor = conexion.cursor()
    cursor.execute(f"UPDATE libros SET {campo} = ? WHERE id = ?", (nuevo_valor, id_libro))
    conexion.commit()
    print("Libro actualizado correctamente.")

def eliminar_libro(conexion):
    ver_libros(conexion)
    id_libro = input("ID del libro a eliminar: ")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM libros WHERE id = ?", (id_libro,))
    conexion.commit()
    print("Libro eliminado correctamente.")

def ver_libros(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM libros")
    libros = cursor.fetchall()
    print("\n--- Lista de Libros ---")
    for libro in libros:
        print(f"ID: {libro[0]}, Título: {libro[1]}, Autor: {libro[2]}, Género: {libro[3]}, Estado: {libro[4]}")
    if not libros:
        print("No hay libros en la base de datos.")

def buscar_libros(conexion):
    criterio = input("Buscar por (titulo, autor, genero): ")
    valor = input(f"Ingrese el {criterio}: ")
    cursor = conexion.cursor()
    cursor.execute(f"SELECT * FROM libros WHERE {criterio} LIKE ?", ('%' + valor + '%',))
    libros = cursor.fetchall()
    print("\n--- Resultados de la búsqueda ---")
    for libro in libros:
        print(f"ID: {libro[0]}, Título: {libro[1]}, Autor: {libro[2]}, Género: {libro[3]}, Estado: {libro[4]}")
    if not libros:
        print("No se encontraron resultados.")