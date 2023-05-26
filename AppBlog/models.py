from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Articulo(models.Model):
    titulo = models.CharField(max_length=64)
    subtitulo= models.CharField(max_length=150)
    cuerpo= models.TextField()
    Autor = models.CharField(max_length=64)
    fecha= models.DateField(null=True)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    #imagen




#class FrutosSecos(models.Model):
    #nombre = models.CharField(max_length=64)  # Equivalente de str
    #gramos = models.IntegerField()  # Equivalent de int

    #def __str__(self):
        #return f"{self.nombre} | {self.gramos}"


#class Vinos(models.Model):
    #nombre = models.CharField(max_length=256)
    #bodega = models.CharField(max_length=256)
    #año = models.IntegerField()

    #def __str__(self):
       # return f"{self.nombre}, {self.bodega}, {self.año}"


#class Sucursales(models.Model):
 #   direccion = models.CharField(max_length=256)
  #  email = models.EmailField(blank=True)
   # telefono = models.CharField(max_length=20, blank=True)

    #def __str__(self):
     #   return f"{self.direccion}, {self.email}, {self.telefono}"



