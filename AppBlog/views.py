from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
#from django.template import loader   CREO QUE EL PROFESOR NO LO USO
from AppBlog.models import Articulo
from AppBlog.forms import CrearArticulo
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.
def home(request):
    return render(request, "AppBlog/home.html")

def about(request):
    return render(request, "AppBlog/about.html")

def article(request):
    return render(request, "AppBlog/article.html")

def ListaDeArticulos(request):
    contexto = {
        "articulos": Articulo.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='AppBlog/pages.html',
        context=contexto,
    )
    return http_response


def crear_articulo(request):
   if request.method == "POST":
       formulario = CrearArticulo(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           titulo = data["titulo"]
           subtitulo = data["subtitulo"]
           cuerpo = data["cuerpo"]
           Autor = data["Autor"]
           fecha = data["fecha"]
           articulo = Articulo(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, Autor=Autor, fecha=fecha, )  # lo crean solo en RAM
           articulo.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la lista de cursos
           #url_exitosa = reverse('crear-articulo')  
           return redirect("ListaArticulos")
   else:  # GET
       formulario = CrearArticulo()
       http_response = render(
       request=request,
       template_name='AppBlog/crear_articulo.html',
       context={'formulario': formulario}
   )
   return http_response

def buscar_articulo(request):
   if request.method == "POST":
       data = request.POST
       busqueda = data["busqueda"]
       articulos = Articulo.objects.filter(titulo__icontains=busqueda)
       contexto = {
           "articulos": articulos,
       }
       http_response = render(
           request=request,
           template_name='AppBlog/pages.html',
           context=contexto,
       )
       return http_response 
   
def eliminar_articulo(request, id):
   articulo = Articulo.objects.get(id=id)
   if request.method == "POST":
       articulo.delete()
       url_exitosa = reverse('ListaArticulos')
       return redirect(url_exitosa)
   
def editar_articulo(request, id):
    articulo = get_object_or_404(Articulo, id=id)
    if request.method == "POST":
        formulario = CrearArticulo(request.POST)

        if formulario.is_valid():
             data = formulario.cleaned_data
             articulo.titulo = data["titulo"]
             articulo.subtitulo = data["subtitulo"]
             articulo.cuerpo = data["cuerpo"]
             articulo.Autor = data["Autor"]
             articulo.fecha = data["fecha"]
             articulo.save()
             url_exitosa = reverse('ListaArticulos')
             return redirect(url_exitosa)
    else:  # GET
        inicial = {
            'titulo': articulo.titulo, 
            'subtitulo': articulo.subtitulo, 
            'cuerpo': articulo.cuerpo, 
            'Autor': articulo.Autor, 
            'fecha': articulo.fecha,
        }
        formulario = CrearArticulo(initial=inicial)
    return render(
        request=request,
        template_name='AppBlog/editar_articulo.html',
        context={'formulario': formulario},
    )

class ArticuloDetailView(DetailView):
   model = Articulo
   success_url = reverse_lazy('ListaArticulos')

# def editar_articulo(request, id):
#     articulo = get_object_or_404(Articulo, id=id)

#     if request.method == "POST":
#         formulario = CrearArticulo(request.POST, instance=articulo)

#         if formulario.is_valid():
#             formulario.save()

#             url_exitosa = reverse('ListaArticulos')
#             return redirect(url_exitosa)
#     else:
#         formulario = CrearArticulo(instance=articulo)

#     return render(
#         request=request,
#         template_name='AppBlog/editar_articulo.html',
#         context={'formulario': formulario},
#     )

#def comentarios(request):
    #Sucursales
    #return render(request, "AppBlog/sucursales.html")

#def frutosSecos(request):
    #return render(request, "AppBlog/frutossecos.html")

#def vinos(request):
 #   return render(request, "AppBlog/vinos.html")

#def listar_vinos(request):
    #contexto = {
    #    "vinos": Vinos.objects.all(),
    #}
   # http_response = render(
   #     request=request,
    #    template_name='AppBlog/vinos.html',
    #    context=contexto,
  #  )
  #  return http_response

#def sumar_vino(request): #formulario usando Django
   #if request.method == "POST":
    #   formulario = VinoFormulario(request.POST)

      # if formulario.is_valid():
#            data = formulario.cleaned_data  # es un diccionario
#            nombre = data["nombre"]
#            bodega = data["bodega"]
#            año = data["año"]
#            vino = Vinos(nombre=nombre, bodega=bodega, año=año)  # lo crean solo en RAM
#            vino.save()  # Lo guardan en la Base de datos

#            # Redirecciono al usuario a la lista de cursos
#            url_exitosa = reverse('vinos')  # estudios/cursos/
#            return redirect(url_exitosa)
#    else:  # GET
#        formulario = VinoFormulario()
#        http_response = render(
#        request=request,
#        template_name='AppBlog/sumarvino.html',
#        context={'formulario': formulario}
#    )
#    return http_response


#def buscar_vinos(request):
#    if request.method == "POST":
#        data = request.POST
#        busqueda = data["busqueda"]
#        vinos = Vinos.objects.filter(bodega__contains=busqueda)
#        contexto = {
#            "vinos": vinos,
#        }
#        http_response = render(
#            request=request,
#            template_name='AppBlog/vinos.html',
#            context=contexto,
#        )
#        return http_response