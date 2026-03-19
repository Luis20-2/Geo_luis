from core_api.Serializers.empleado_serializer import *
from rest_framework import  viewsets

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)