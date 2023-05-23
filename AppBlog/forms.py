from django import forms
from .models import Articulo

class CrearArticulo(forms.Form):
    titulo = forms.CharField(max_length=64)
    subtitulo= forms.CharField(max_length=150)
    cuerpo= forms.CharField(widget=forms.Textarea())
    Autor = forms.CharField(max_length=64)
    fecha= forms.DateField(required=False)
    #imagen

# class CrearArticulo(forms.ModelForm):
#     class Meta:
#         model = Articulo
#         fields = ['titulo', 'subtitulo', 'cuerpo', 'Autor', 'fecha']