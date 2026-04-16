from core_api.Serializers.direccion_serializer import *
from core_api.parsers import PlainTextJSONParser
from rest_framework import permissions, viewsets
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser


class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    parser_classes = [JSONParser, FormParser, MultiPartParser, PlainTextJSONParser]