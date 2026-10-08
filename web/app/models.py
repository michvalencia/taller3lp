from app.extensions import db


class Categoria(db.Model):
    __tablename__ = 'categorias'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False, unique=True)
    
    # Relación uno-a-muchos: una categoría tiene muchos productos
    productos = db.relationship("Producto", backref="categoria", lazy=True)

    def __repr__(self):
        return f"<Categoria {self.nombre}>"


class Producto(db.Model):
    __tablename__ = 'productos'
    
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(20), nullable=False, unique=True)
    marca = db.Column(db.String(80), nullable=False)
    nombre = db.Column(db.String(160), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    foto = db.Column(db.String(200), nullable=True)
    stock = db.Column(db.Integer, nullable=False, default=0)
    activo = db.Column(db.Boolean, nullable=False, default=True)
    
    # Llave foránea que conecta con la tabla categorias
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)

    @property
    def disponible(self):
        # Retorna True si el producto está activo y tiene stock mayor a 0
        return self.activo and self.stock > 0

    def __repr__(self):
        return f"<Producto {self.sku} - {self.nombre}>"
