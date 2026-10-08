import os
import requests
from flask import Blueprint, render_template, request

main_bp = Blueprint('main', __name__)

# Leemos la dirección de la API desde la variable de entorno
API_URL = os.environ.get("API_URL", "http://api:8000")

@main_bp.route('/')
def index():
    categoria_id = request.args.get('categoria_id')
    
    # Consultar productos desde la API
    url_productos = f"{API_URL}/productos/"
    params = {}
    if categoria_id:
        params['categoria_id'] = categoria_id
        
    try:
        res_prod = requests.get(url_productos, params=params)
        productos = res_prod.json() if res_prod.status_code == 200 else []
    except Exception as e:
        print(f"Error conectando con la API: {e}")
        productos = []

    # Consultar categorías desde la API para el filtro
    url_categorias = f"{API_URL}/categorias/"
    try:
        res_cat = requests.get(url_categorias)
        categorias = res_cat.json() if res_cat.status_code == 200 else []
    except Exception as e:
        print(f"Error conectando con la API: {e}")
        categorias = []

    return render_template('index.html', productos=productos, categorias=categorias)

@main_bp.route('/producto/<sku>')
def detalle_producto(sku):
    url_producto = f"{API_URL}/productos/{sku}"
    try:
        res = requests.get(url_producto)
        if res.status_code == 200:
            producto = res.json()
            return render_template('detalle.html', producto=producto)
    except Exception as e:
        print(f"Error conectando con la API: {e}")

    return "Producto no encontrado", 404
