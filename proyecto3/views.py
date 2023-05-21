from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def DiaDeHoy(request):
    dia = datetime.now()
    documento_de_texto = f"hoy es el dia {dia.day}/{dia.month}"
    return HttpResponse(documento_de_texto)


def MiNombre(request, nombre):
    presentacion = f"mi nombre es: <br></br> {nombre}"
    return HttpResponse(presentacion)

def pruebaPlantilla(request):
    nom= "heber"
    ap="rosales"
    fecha=datetime.now()
    frase= f"este template fue creado el {fecha.day}/{fecha.month}"
    diccionario = {"nombre":nom, "apellido":ap, "fecha":frase}

    #miHtml = open('C:/Users/E-User/Desktop/coder python/3raEntrega/proyecto3/proyecto3/plantillas/template1.html')
    #plantilla=Template(miHtml.read())
    #miHtml.close()
    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

