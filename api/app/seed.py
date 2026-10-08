import json
import os
from .database import SessionLocal
from .models import Categoria, Producto

def cargar_semilla():
    db = SessionLocal()
    ruta_json = os.path.join(os.path.dirname(__file__), "..", "data", "productos.json")
    
    if not os.path.exists(ruta_json):
        print("No se encontró el archivo productos.json")
        return

    with open(ruta_json, "r", encoding="utf-8") as f:
        productos_data = json.load(f)

    categorias_map = {}

    for item in productos_data:
        nombre_cat = item["categoria"]
        if nombre_cat not in categorias_map:
            cat_existente = db.query(Categoria).filter(Categoria.nombre == nombre_cat).first()
            if not cat_existente:
                cat_existente = Categoria(nombre=nombre_cat)
                db.add(cat_existente)
                db.flush()
            categorias_map[nombre_cat] = cat_existente

        sku = item["sku"]
        prod_existente = db.query(Producto).filter(Producto.sku == sku).first()
        if not prod_existente:
            nuevo_prod = Producto(
                sku=sku,
                nombre=item["nombre"],
                descripcion=item.get("descripcion"),
                precio=item["precio"],
                imagen=item.get("imagen"),
                categoria_id=categorias_map[nombre_cat].id
            )
            db.add(nuevo_prod)

    db.commit()
    db.close()
    print("¡Semilla cargada con éxito!")

if __name__ == "__main__":
    cargar_semilla()
