# Geo Luis API REST

Proyecto backend desarrollado con Django y Django REST Framework para la gestión de empleados y direcciones geográficas, con autenticación JWT y documentación interactiva de endpoints.

## Objetivo
Construir una API REST profesional, segura y documentada, lista para ser consumida por cliente web y aplicación móvil.

## Tecnologías utilizadas
- Python 3
- Django 6
- Django REST Framework
- JWT con SimpleJWT
- Swagger / OpenAPI con drf-spectacular
- SQLite3
- CORS Headers

## Requisitos previos
- Python 3.12 o superior
- pip
- Git
- Navegador web moderno
- Opcional para móvil: Node.js y Expo Go

## Instalación local
1. Clona el repositorio.
2. Crea y activa un entorno virtual.
3. Instala dependencias:

   pip install -r requirements.txt

4. Configura variables de entorno según el archivo .env.example.
5. Aplica migraciones:

   python manage.py migrate

6. Crea un superusuario opcional:

   python manage.py createsuperuser

7. Inicia el servidor:

   python manage.py runserver

## Variables de entorno
Puedes definir estas variables en tu sistema local:
- DJANGO_SECRET_KEY
- DJANGO_DEBUG
- DJANGO_ALLOWED_HOSTS

## Endpoints principales
### Autenticación
- POST /api/mobile/register/
- POST /api/mobile/login/
- POST /api/token/
- POST /api/token/refresh/
- POST /api/token/verify/

### Recursos REST
- GET, POST /api-luis/empleados/
- GET, PUT, PATCH, DELETE /api-luis/empleados/{id}/
- GET, POST /api-luis/direcciones/
- GET, PUT, PATCH, DELETE /api-luis/direcciones/{id}/

## Documentación de la API
- Swagger UI: /api/docs/
- ReDoc: /api/redoc/
- Esquema OpenAPI: /api/schema/

## Seguridad
La API protege las rutas de escritura con autenticación. Para clientes modernos se incluye JWT mediante encabezado Authorization Bearer.

## Repositorio GitHub
https://github.com/Luis20-2/Geo_luis
