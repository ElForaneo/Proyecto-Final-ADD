from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_usuario,name="login"),
    path('logout_user',views.logout_user,name="logout")
]