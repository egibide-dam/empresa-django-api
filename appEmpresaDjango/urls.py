from django.urls import path, include
from .views import (
    DepartamentoListApiView,
    DepartamentoDetailApiView, HabilidadListApiView, HabilidadDetailApiView, EmpleadoDetailApiView, EmpleadoListApiView,
    EmpleadoImagenUpload
)

urlpatterns = [
    path('departamentos', DepartamentoListApiView.as_view()),
    path('departamentos/<int:departamento_id>', DepartamentoDetailApiView.as_view()),
    path('habilidades', HabilidadListApiView.as_view()),
    path('habilidades/<int:habilidad_id>', HabilidadDetailApiView.as_view()),
    path('empleados', EmpleadoListApiView.as_view()),
    path('empleados/<int:empleado_id>', EmpleadoDetailApiView.as_view()),
    path("empleados/<int:empleado_id>/imagen/", EmpleadoImagenUpload.as_view(), name="empleado_imagen_upload"),
]