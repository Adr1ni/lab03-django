from django.shortcuts import render
from .models import *

def index(request):
    return render(request,'tarea/index.html')

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request,'client/clientes.html',{"clientes":clientes})

def cliente(request,cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    telefonos = cliente.telefonos.all()
    return render(request,'client/client.html',{"cliente":cliente,"telefonos":telefonos})

def proveedor(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/proveedores.html',{"proveedores":proveedores})


def productos(request):
    productos = Producto.objects.all()
    return render(request,'producto/productos.html',{'productos':productos})

def producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, 'producto/producto.html',{'producto':producto})

def ventas(request):
    ventas = VentaProducto.objects.all()
    return render(request,'ventas/ventas.html',{'ventas':ventas})