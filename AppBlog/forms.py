from django import forms

class VinoFormulario(forms.Form):
   nombre = forms.CharField(required=True, max_length=64)
   bodega = forms.CharField(required=True, max_length=64)
   año = forms.IntegerField()