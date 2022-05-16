from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist 
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .models import Productos
from .forms import PedidoForm, PedidoFromEdit

# Create your views here.

@login_required
def ordenes(request):
    ord = Productos.objects.all()
    queryset = request.GET.get("buscar")
    if queryset:
        ord = Productos.objects.filter(
            Q(nombre__icontains = queryset)|
            Q(estado__icontains = queryset)
        ).distinct()
    context = {
        'ord':ord
    }
    return render(request,'ordenes/ordenes.html', context)


@login_required
def crear_ord(request): 
    if request.method == 'POST': 
        ord_form =PedidoForm(request.POST) 
        if ord_form.is_valid(): 
            ord_form.save() 
            return redirect('ordenes') 
    else: 
           ord_form =PedidoForm() 
    return render(request, 'ordenes/crear_ord.html',{'ord_form': ord_form}) 

@login_required
def editar_ord(request, id): 
    ord_form = None 
    error = None 
    try: 
        orde = Productos.objects.get(id = id) 
        if request.method == 'GET': 
            ord_form = PedidoFromEdit(instance=orde) 
        else: 
            ord_form = PedidoFromEdit(request.POST, instance = orde) 
            if ord_form.is_valid(): 
                ord_form.save() 
                return redirect('ordenes') 
    except ObjectDoesNotExist as e: 
        error = e 
    return render(request,'ordenes/editar_ord.html',{'ord_form':ord_form, 'error':error}) 


class BorrarOrden(DeleteView):
    model = Productos
    success_url = reverse_lazy('ordenes')
