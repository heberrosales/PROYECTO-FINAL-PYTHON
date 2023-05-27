from django.test import TestCase

# Create your tests here.
from django.db import IntegrityError
from AppBlog.models import Articulo

class ArticuloTests(TestCase):
   """En esta clase van todas las pruebas del modelo Articulo."""

   def test_creacion_articulo(self):
       # caso uso esperado
       articulo = Articulo(titulo="Titulo", subtitulo="subtitulo")
       articulo.save()

       # Compruebo que el articulo fue creado y la data fue guardad correctamente
       self.assertEqual(Articulo.objects.count(), 1)
       self.assertEqual(articulo.titulo, "Titulo")
       self.assertEqual(articulo.subtitulo, "subtitulo")

   def test_articulo_str(self):
       articulo = Articulo(titulo="Jujuy", subtitulo="viajes")
       articulo.save()

       # Compruebo el str funciona como se desea
       self.assertEqual(articulo.__str__(), "Jujuy | viajes")