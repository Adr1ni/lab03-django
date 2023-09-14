from django.contrib import admin
from .models import * 

modelos = [Direccion,Producto,Proveedor,Categoria,Cliente,Telefono,Venta,
VentaProducto,]

admin.site.register(modelos)
