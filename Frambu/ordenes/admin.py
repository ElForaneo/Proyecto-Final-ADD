from django.contrib import admin
from .models import Estatus
from .models import Productos

# Register your models here.

admin.site.register(Estatus)
admin.site.register(Productos)