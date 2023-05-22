from django.urls import path
from AppBlog import views

urlpatterns = [
    #path('saludo/', views.saludo, name="saludo"),
    #path('fecha/', views.DiaDeHoy, name="fecha"),
    #path('nombre/<nombre>', views.MiNombre, name="nombre"),
    #path('plantilla/', views.pruebaPlantilla, name="plantilla"),
    # path('', views.inicio, name="Inicio"),
    # path('frutos-secos/', views.frutosSecos,name="frutossecos"),
    # path('vinos/', views.listar_vinos, name="vinos"),
    # path('sucursales/', views.comentarios,name="sucursales"),
    # path('sumar-vino/', views.sumar_vino, name="sumar_vino"),
    # path('buscar-vino/', views.buscar_vinos, name="buscar_vinos")
    path('', views.home, name="home"),
    path('article/', views.article, name="articulos"),
    path('pages/', views.ListaDeArticulos, name="ListaArticulos"),
    path('about/', views.about, name="about"),
    path('crear-articulo/', views.crear_articulo, name="crear-articulo"),
    path('buscar-articulo/', views.buscar_articulo, name="buscar_articulo"),
    path('eliminar-articulo/<int:id>/', views.eliminar_articulo, name="eliminar_articulo"),
    path('editar-articulo/<int:id>/', views.editar_articulo, name="editar_articulo"),
]
