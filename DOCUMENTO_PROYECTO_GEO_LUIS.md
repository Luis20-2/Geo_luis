# Documento del Proyecto Geo Luis

## 1) ¿Qué se implementó?

Durante el desarrollo se construyó una solución completa de geolocalización con tres capas funcionales:

1. **Backend API (Django + DRF)**
   - Se expusieron endpoints REST para:
     - Empleados
     - Direcciones relacionadas a empleados
   - Se configuró autenticación para web y móvil:
     - Sesión (login web)
     - Token (login móvil)
   - Se agregaron endpoints móviles de registro y login.
   - Se ajustaron serializers y viewsets para soportar correctamente relaciones y respuestas útiles para frontend.
   - Se habilitó CORS para permitir consumo desde la app móvil.

2. **Frontend web (plantilla en Django)**
   - Se conectó `index.html` a endpoints reales (sin datos mock).
   - Se añadieron formularios para crear empleados y direcciones.
   - Se implementó un mapa real con marcadores dinámicos.
   - Se integró búsqueda por texto libre sobre empleados y direcciones.
   - Se conectaron botones de acceso y registro con autenticación real.

3. **App móvil (Expo + React Native)**
   - Se creó una app móvil separada para Expo Go.
   - Se implementaron pantallas de:
     - Login
     - Registro
     - Home
     - Empleados
     - Direcciones
     - Mapa
   - Se conectó la app a la API Django usando token.
   - Se mejoró UX del selector de empleados en creación de direcciones (búsqueda, lista legible y modal dedicado).

---

## 2) Problemas técnicos que se resolvieron

- Relación hipervinculada entre modelos (empleado/dirección).
- Persistencia y uso correcto de token en móvil.
- Error de contenido en requests (`Unsupported media type text/plain;charset=UTF-8`).
- Compatibilidad del backend con entradas en `text/plain` cuando el cliente móvil lo enviaba así.
- Ajustes de visualización en lista/selectores para nombres largos de empleados.
- Integración y despliegue inicial del repositorio con `.gitignore` correcto para entorno Python/venv.

---

## 3) ¿Por qué se separó en 2 proyectos diferentes?

Se separó en:

- **Proyecto 1:** `lab_geo_luis` (Backend Django + API + Web)
- **Proyecto 2:** `geo_luis_app` (App móvil Expo/React Native)

### Razones de arquitectura

1. **Separación de responsabilidades (SoC)**
   - El backend se enfoca en lógica de negocio, datos, seguridad y API.
   - El frontend móvil se enfoca en experiencia de usuario y consumo de API.

2. **Escalabilidad y mantenimiento**
   - Cambios en móvil no obligan a tocar backend y viceversa.
   - Permite crecer cada parte con su propio ritmo y equipo.

3. **Despliegue independiente**
   - API puede desplegarse en servidor cloud.
   - App móvil puede distribuirse por Expo/tiendas sin acoplarse al deploy web.

4. **Reutilización de API**
   - La misma API sirve para web, móvil y futuros clientes (por ejemplo dashboard admin o integraciones externas).

5. **Mejor control de dependencias**
   - Python/Django y Node/React Native tienen ecosistemas distintos.
   - Mantenerlos separados evita conflictos de entorno y simplifica debugging.

6. **Seguridad y autenticación más claras**
   - Web usa sesiones.
   - Móvil usa token.
   - La separación facilita aplicar estrategias adecuadas por canal.

---

## 4) Resultado final de la solución

La solución quedó preparada para trabajar de forma real en red local y evolucionar a producción:

- Backend funcional con API protegida y endpoints móviles.
- Web conectada a datos reales con operaciones CRUD.
- App móvil conectada por token, con flujos de creación/listado/mapa.
- Arquitectura desacoplada, mantenible y lista para escalar.

---

## 5) Recomendación siguiente fase

Para la siguiente etapa se recomienda:

- Migrar SQLite a PostgreSQL.
- Definir variables de entorno para URL base por ambiente (dev/stage/prod).
- Agregar pruebas automáticas de API y UI.
- Preparar pipeline CI/CD para backend y app móvil.
- Publicar documentación de endpoints (OpenAPI/Swagger).
