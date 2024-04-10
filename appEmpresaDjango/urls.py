from django.urls import path, include
from .views import (
    DepartamentoListApiView,
    DepartamentoDetailApiView
)

urlpatterns = [
    path('departamentos', DepartamentoListApiView.as_view()),
    path('departamentos/<int:departamento_id>', DepartamentoDetailApiView.as_view()),
]