from pydantic import BaseModel
from typing import Optional, List

# Esquema base para Categoría
class CategoriaBase(BaseModel):
    id: int
    nombre: str

    class Config:
        from_attributes = True

# Esquema base para Producto (JSON de salida)
class ProductoBase(BaseModel):
    id: int
    sku: str
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    imagen: Optional[str] = None
    categoria: CategoriaBase  # Anidamos el esquema de categoría para que incluya su nombre directamente

    class Config:
        from_attributes = True
