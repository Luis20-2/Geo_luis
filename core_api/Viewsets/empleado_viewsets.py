from core_api.Serializers.empleado_serializer import *
from core_api.parsers import PlainTextJSONParser
from rest_framework import permissions, viewsets
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser


class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    parser_classes = [JSONParser, FormParser, MultiPartParser, PlainTextJSONParser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)