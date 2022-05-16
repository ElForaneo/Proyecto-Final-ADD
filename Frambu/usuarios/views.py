from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.


def login_usuario(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            messages.success(request,("Gracias por iniciar sesion!!"))
            return redirect('home')
        else:
            messages.error(request,("Hubo un error al iniciar sesion, intenta de nuevo"))
            return redirect('login')
    return render(request, 'login/login.html',{})

def logout_user(request):
    logout(request)
    return redirect('login')