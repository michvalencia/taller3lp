from fastapi import FastAPI
from .database import engine, Base
from .routers import productos, categorias

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Tienda Virtual", version="1.0.0")

app.include_router(productos.router)
app.include_router(categorias.router)

@app.get("/")
def root():
    return {"mensaje": "API funcionando perfectamente"}
