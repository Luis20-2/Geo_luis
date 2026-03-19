from core_api.Serializers.direccion_serializer import *
from rest_framework import  viewsets

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer