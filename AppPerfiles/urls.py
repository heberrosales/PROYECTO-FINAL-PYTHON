from django.urls import path
from AppPerfiles import views

urlpatterns = [
    path('registro/', views.registro, name="registro"),
]