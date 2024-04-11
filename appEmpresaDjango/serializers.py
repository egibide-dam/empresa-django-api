from rest_framework import serializers
from .models import Departamento
from djoser.serializers import UserSerializer, UserCreateSerializer as BaseUserSerializer
class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ["nombre", "telefono", "created", "updated"]

class UserCreateSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'email', 'username', 'password']

class CurrentUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ['id', 'email', 'username', 'password']