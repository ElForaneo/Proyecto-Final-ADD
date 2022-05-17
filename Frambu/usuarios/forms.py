from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    
    class Meta:
        model = Empleado
        fields = ['nombre','nombre_2','Apellido_Paterno','Apellido_Materno','telefono']
        labels = {
            'nombre':'Nombre del Usuario',
            'nombre_2':'Segundo nombre (opcionla)',
            'Apellido_Paterno': 'Apellido Paterno',
            'Apellido_Materno': 'Apellido Materno',
            'telefono': 'Celular',

        }