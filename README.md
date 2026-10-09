# Taller 3 — Tienda Virtual con Contenedores

Aplicación web desarrollada con arquitectura de tres capas utilizando Docker Compose para la orquestación de contenedores.

## Arquitectura de Servicios

* **`database`**: Base de datos relacional PostgreSQL.
* **`api`**: Servicio backend desarrollado en FastAPI que gestiona las consultas a la base de datos.
* **`web`**: Servicio frontend desarrollado en Flask que consume la API REST y renderiza las vistas con Jinja2 y Bootstrap.

## Requisitos Previos

* Docker Engine
* Docker Compose

## Instrucciones de Ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/michvalencia/taller3lp.git
   cd lp2-tallermich2-taller3

##Desplegar la aplicación
sudo docker compose up -d --build

##Acceso a los servicios
Interfaz Web (Flask): http://localhost:5000

API Backend (FastAPI): http://localhost:8000/docs
