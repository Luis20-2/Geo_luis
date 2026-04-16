# Documentación de Endpoints - Geo Luis API

## 1. Empleados
### GET /api-luis/empleados/
Devuelve la lista de empleados.

Respuesta esperada:
- 200 OK con arreglo JSON

### POST /api-luis/empleados/
Crea un empleado nuevo.

Parámetros de entrada:
- nombre_completo: string
- puesto: string

Respuesta esperada:
- 201 Created
- 401 Unauthorized si no hay autenticación

## 2. Direcciones
### GET /api-luis/direcciones/
Devuelve la lista de direcciones registradas.

### POST /api-luis/direcciones/
Crea una dirección asociada a un empleado.

Parámetros de entrada:
- empleado: id
- latitud: string
- longitud: string

Respuesta esperada:
- 201 Created
- 401 Unauthorized si no hay autenticación

## 3. Registro móvil
### POST /api/mobile/register/
Crea un usuario y devuelve token clásico además de JWT.

Parámetros:
- username
- password

Respuesta:
- 201 Created
- token
- access
- refresh

## 4. Login móvil
### POST /api/mobile/login/
Autentica al usuario.

Parámetros:
- username
- password

Respuesta:
- 200 OK
- token
- access
- refresh

## 5. JWT estándar
### POST /api/token/
Recibe username y password; devuelve access y refresh.

### POST /api/token/refresh/
Recibe refresh; devuelve nuevo access.

### POST /api/token/verify/
Recibe un token y valida su vigencia.

## 6. Documentación interactiva
- GET /api/docs/
- GET /api/redoc/
- GET /api/schema/
