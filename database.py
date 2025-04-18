from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys

DB_USER = "Gabriel"
DB_PASSWORD = "Yusa_777"
DB_HOST = "localhost"
DB_PORT = "3307"
DB_NAME = "biblioteca"

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

try:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
except Exception as e:
    print("Error al conectar con la base de datos:", e)
    sys.exit(1)
