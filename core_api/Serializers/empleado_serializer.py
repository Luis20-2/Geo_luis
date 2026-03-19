from admin_geoluis.models import Empleado
from rest_framework import  serializers

class EmpleadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Empleado
        fields = ['url', 'nombre_completo', 'puesto']