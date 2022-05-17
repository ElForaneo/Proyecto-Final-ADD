from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist 
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import EmpleadoForm
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

def registrar_user(request):
    if request.method == "POST":
        reg_user = UserCreationForm(request.POST)
        if reg_user.is_valid():
            reg_user.save()
            username = reg_user.cleaned_data['username']
            password = reg_user.cleaned_data['password1']
            user = authenticate(request, username = username, password = password)
            login(request,user)
            messages.success(request,("Gracias por registrarte!!"))
            return redirect('usuariomas')
    else:
        reg_user = UserCreationForm()

    return render(request,'login/registrar.html',{'reg_user':reg_user})


@login_required
def Usuarios_register(request):
    usuarios = User.objects.all()
    return render(request, 'users/usuarios.html',{'usuarios':usuarios})


@login_required
def Usuariomas(request):
    user_form = None 
    error = None 
    try: 
        orde = User.objects.get(id = id) 
        if request.method == 'GET': 
            user_form = EmpleadoForm(instance=orde) 
        else: 
            user_form = EmpleadoForm(request.POST, instance = orde) 
            if user_form.is_valid(): 
                user_form.save() 
                return redirect('usuarios') 
    except ObjectDoesNotExist as e: 
        error = e 
    return render(request,'users/usuariosmas.html',{'user_form':user_form, 'error':error}) 