from django.contrib import admin

from appEmpresaDjango.models import Habilidad,Departamento,Empleado

# Register your models here.
admin.site.register(Habilidad)
admin.site.register(Departamento)
admin.site.register(Empleado)
