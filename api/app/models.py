from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False, unique=True)
    
    # Relación de 1 Categoria a Muchos Productos
    productos = relationship("Producto", back_populates="categoria")

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, unique=True, index=True, nullable=False)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)
    precio = Column(Float, nullable=False)
    imagen = Column(String, nullable=True)
    
    # Clave foránea que conecta con la tabla de categorías
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)
    
    # Relación inversa hacia Categoria
    categoria = relationship("Categoria", back_populates="productos")
