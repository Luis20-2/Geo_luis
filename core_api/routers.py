from core_api.Viewsets.direccion_viewsets import DireccionViewSet
from core_api.Viewsets.empleado_viewsets import EmpleadoViewSet
from rest_framework import routers


router = routers.DefaultRouter()


router.register(r'empleados', EmpleadoViewSet)
router.register(r'direcciones', DireccionViewSet)