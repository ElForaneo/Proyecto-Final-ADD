from django.contrib import admin
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Create your models here.


class Empleado(models.Model):
    usuario = models.OneToOneField(User,null=False,blank=False,on_delete=models.CASCADE)
    nombre = models.CharField(null=False,blank=False,unique=True,max_length=50)
    nombre_2 = models.CharField(null=True,blank=True,unique=True,max_length=50)
    Apellido_Paterno = models.CharField(null=False,blank=False,unique=True,max_length=50)
    Apellido_Materno = models.CharField(null=False,blank=False,unique=True,max_length=50)
    telefono = PhoneNumberField(blank=True,null=True)


class EmpleadoAdmin(admin.ModelAdmin):
    list_display =('usuario', 'nombre', 'nombre_2', 'Apellido_Paterno','Apellido_Materno')