from django import forms

class CrearArticulo(forms.Form):
   titulo = forms.CharField(max_length=64)
   subtitulo= forms.CharField(max_length=150)
   cuerpo= forms.CharField(widget=forms.Textarea())
   Autor = forms.CharField(max_length=64)
   fecha= forms.DateField(required=False)
   #imagen