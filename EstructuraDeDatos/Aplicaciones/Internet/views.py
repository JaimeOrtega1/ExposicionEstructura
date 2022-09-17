from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Cliente
# Create your views here.
def home(request):
    Listadoclientes = Cliente.objects.all()
    return render(request,"GestionClientes.html" ,  {"clientes" : Listadoclientes})

def registrarCliente(request):
    cedula = request.POST['txtcedula']
    nombre = request.POST['txtnombre']
    monto = request.POST['nummonto']
    pagado = request.POST['txtpagado']
    
    cliente = Cliente.objects.create(cedula=cedula,nombre = nombre,monto = monto,pagado = pagado)
    messages.success(request,'¡Cliente Registrado!')

    return redirect('/')

def edicionCliente(request,cedula):
    cliente = Cliente.objects.get(cedula=cedula)
    return render(request,'edicionCliente.html',{"cliente":cliente})

def editarCliente(request):
    cedula = request.POST['txtcedula']
    nombre = request.POST['txtnombre']
    monto = request.POST['nummonto']
    pagado = request.POST['txtpagado']
    cliente = Cliente.objects.get(cedula=cedula)
    cliente.nombre = nombre
    cliente.monto = monto
    cliente.pagado = pagado
    cliente.save()
    messages.success(request,'¡Cliente Actualizado!')

    return redirect('/')



def eliminarCliente(request,cedula):
    cliente = Cliente.objects.get(cedula=cedula)
    cliente.delete()
    messages.success(request,'¡Cliente Eliminado!')
    return redirect('/')

