from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_usuario,name="login"),
    path('logout_user',views.logout_user,name="logout"),
    path('register_user',views.registrar_user,name="register_user"),
    path('Dashboard/Clientes', views.Usuarios_register,name="clientes"),
    path('Dashboard/Clientes/<int:id>', views.Usuariomas,name="usuariomas"),

]