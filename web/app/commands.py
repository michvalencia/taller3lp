import os
import json
import click
from flask import current_app
from app.extensions import db
from app.models import Categoria, Producto

def register_commands(app):

    @app.cli.command('reset-db')
    def reset_db():
        """Elimina y recrea la base de datos."""
        if click.confirm('¿Estás segura de reiniciar la base de datos? Se perderán todos los datos.'):
            with app.app_context():
                db.drop_all()
                db.create_all()
            click.echo('Base de datos reiniciada.')
        else:
            click.echo('Operación cancelada.')

    @app.cli.command('seed-db')
    def seed_db():
        """Llena la base de datos desde productos.json."""
        with app.app_context():

            db.create_all()

            json_path = os.path.join(app.root_path, 'data', 'productos.json')

            if not os.path.exists(json_path):
                click.echo(f'Error: No se encontró el archivo en {json_path}')
                return

            with open(json_path, 'r', encoding='utf-8') as f:
                productos_data = json.load(f)

            for prod in productos_data:
                nombre_cat = prod.get('categoria', 'General')
                categoria = Categoria.query.filter_by(nombre=nombre_cat).first()
                if not categoria:
                    categoria = Categoria(nombre=nombre_cat)
                    db.session.add(categoria)
                    db.session.commit()

                nombre_prod = prod.get('nombre')
                producto_existente = Producto.query.filter_by(nombre=nombre_prod).first()

                if not producto_existente:
                    nuevo_producto = Producto(
                        nombre=nombre_prod,
                        precio=prod.get('precio', 0.0),
                        stock=prod.get('stock', 0),
                        descripcion=prod.get('descripcion', ''),
                        categoria_id=categoria.id
                    )
                    db.session.add(nuevo_producto)

            db.session.commit()
            click.echo('¡Base de datos poblada exitosamente con productos.json!')
