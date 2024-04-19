from rest_framework import serializers
from .models import Departamento, Habilidad, Empleado
from djoser.serializers import UserSerializer, UserCreateSerializer as BaseUserSerializer
class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ["id","nombre", "telefono", "created", "updated"]

class HabilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habilidad
        fields = ["id","nombre","created", "updated"]

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ["id","nombre","fecha_nacimiento","antiguedad","departamento","habilidades","created", "updated"]
