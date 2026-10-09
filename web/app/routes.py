import os
import requests
from flask import Blueprint, render_template, request

main_bp = Blueprint('main', __name__)

API_URL = os.environ.get("API_URL", "http://api:8000")

@main_bp.route('/')
def index():
    categoria_id = request.args.get('categoria_id')

    # Consultar productos desde la API
    productos = []
    try:
        res = requests.get(f"{API_URL}/products", timeout=3)
        if res.status_code == 200:
            productos = res.json()
        else:
            res_es = requests.get(f"{API_URL}/productos", timeout=3)
            if res_es.status_code == 200:
                productos = res_es.json()
    except Exception:
        productos = []

    # Filtrar por categoría si viene el parámetro
    if categoria_id and productos:
        productos = [p for p in productos if str(p.get('categoria_id', '')) == str(categoria_id)]

    # Consultar categorías
    categorias = []
    try:
        res_cat = requests.get(f"{API_URL}/categories", timeout=3)
        if res_cat.status_code == 200:
            categorias = res_cat.json()
        else:
            res_cat_es = requests.get(f"{API_URL}/categorias", timeout=3)
            if res_cat_es.status_code == 200:
                categorias = res_cat_es.json()
    except Exception:
        categorias = []

    return render_template('index.html', productos=productos, categorias=categorias)

@main_bp.route('/categorias')
def categorias():
    return index()

@main_bp.route('/producto/<sku>')
def detalle_producto(sku):
    producto = None
    try:
        res = requests.get(f"{API_URL}/products/{sku}", timeout=3)
        if res.status_code == 200:
            producto = res.json()
        else:
            res_es = requests.get(f"{API_URL}/productos/{sku}", timeout=3)
            if res_es.status_code == 200:
                producto = res_es.json()
    except Exception:
        producto = None

    return render_template('detalle.html', producto=producto) if producto else index()
