from pyexpat import model
from django import forms
from .models import Productos

class PedidoForm(forms.ModelForm):

    class Meta:
        model = Productos
        fields = ['nombre','producto_pedido','estado']
        labels = {
            'nombre':'Nombre del Producto',
            'producto_pedido':'Productos pedidos por usuario',
            'estado': 'Estado del Producto'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["estado"].disabled = True

class PedidoFromEdit(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Ingresa el nombre del titulo"}))
    producto_pedido = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder":"Numero pedido de productos"}))

    class Meta:
        model = Productos
        fields = ['nombre','producto_pedido','producto_enviado','producto_entregado','estado']
        labels ={
            'nombre': 'Nombre del Producto',
            'producto_pedido':'Productos pedidos por usuario',
            'producto_enviado':'Producto enviado hacia el usuario',
            'producto_entregado':'Producto entregado al usuario',
            'estado':'Estado del Producto'
        }