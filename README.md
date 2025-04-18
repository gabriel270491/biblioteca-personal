# Biblioteca Personal con SQLAlchemy y MariaDB

Una aplicación de línea de comandos en Python que permite gestionar una biblioteca personal utilizando MariaDB como sistema de base de datos y SQLAlchemy como ORM.

## Requisitos

- Python 3
- MariaDB
- pip

## Instalación

1. Clona este repositorio.
2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Crea la base de datos `biblioteca` en MariaDB:

```sql
CREATE DATABASE biblioteca;
```

4. Asegúrate de que MariaDB esté corriendo y escuche en el puerto `3307`.

## Configuración

Edita el archivo `database.py` si necesitas cambiar usuario, contraseña o puerto de conexión a la base de datos.

## Ejecución

```bash
python main.py
```

## Funcionalidades

- Agregar libros
- Actualizar información
- Eliminar libros
- Ver listado
- Buscar por título, autor o género
