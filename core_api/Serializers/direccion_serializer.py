from admin_geoluis.models import Direccion
from rest_framework import serializers


class DireccionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Direccion
        fields = ['empleado', 'latitud', 'longitud']