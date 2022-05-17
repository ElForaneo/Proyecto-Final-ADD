from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import  BorrarOrden
from . import views

urlpatterns = [
    path('Ordenes/',views.ordenes,name="ordenes"),
    path('Ordenes/Crear_Orden',views.crear_ord,name="crear_ord"),
    path('Ordenes/Editar_Orden/<int:id>', views.editar_ord, name="editar_ord"),
    path('Ordenes/Eliminar_Orden/<int:pk>', login_required(BorrarOrden.as_view()),name="eliminar_ord"),
    
]