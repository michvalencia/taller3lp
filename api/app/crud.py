from sqlalchemy.orm import Session
from . import models

def get_productos(db: Session, categoria_id: int = None):
    query = db.query(models.Producto)
    if categoria_id:
        query = query.filter(models.Producto.categoria_id == categoria_id)
    return query.all()

def get_producto_por_sku(db: Session, sku: str):
    return db.query(models.Producto).filter(models.Producto.sku == sku).first()

def get_categorias(db: Session):
    return db.query(models.Categoria).all()
