import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Leemos la variable de entorno DATABASE_URL que configuramos en docker-compose
DATABASE_URL = os.environ.get("DATABASE_URL")

# Creamos el motor de conexión de SQLAlchemy
engine = create_engine(DATABASE_URL)

# Creamos la fábrica de sesiones (SessionLocal)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base de la que heredarán nuestros modelos de la base de datos
Base = declarative_base()

# Dependencia que FastAPI inyectará en los endpoints para abrir y cerrar la conexión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
