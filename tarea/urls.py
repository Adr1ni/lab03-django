from django.urls import path
from . import views

app_name = 'tarea'

urlpatterns = [
    path('', views.index,name='index'),
    path('clientes/', views.clientes,name='clientes'),
    path('client/<int:cliente_id>/',views.cliente,name='cliente'),
    path('productos/',views.productos,name='productos'),
    path('producto/<int:producto_id>/',views.producto,name='producto'),
    path('proveedores/',views.proveedor,name='proveedores'),
    path('ventas/',views.ventas,name='ventas'),
]