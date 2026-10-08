from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.get("/", response_model=List[schemas.ProductoBase])
def listar_productos(categoria_id: Optional[int] = None, db: Session = Depends(get_db)):
    return crud.get_productos(db, categoria_id=categoria_id)

@router.get("/{sku}", response_model=schemas.ProductoBase)
def obtener_producto(sku: str, db: Session = Depends(get_db)):
    producto = crud.get_producto_por_sku(db, sku=sku)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto
