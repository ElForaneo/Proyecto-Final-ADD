from django.contrib import admin
from .models import Empleado, EmpleadoAdmin
# Register your models here.


admin.site.register(Empleado,EmpleadoAdmin)