from sqlalchemy import Column, Integer, String
from .database import Base

class Libro(Base):
    __tablename__ = "libros"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)
    autor = Column(String(255), nullable=False)
    genero = Column(String(255), nullable=False)
    estado = Column(String(255), nullable=False)
