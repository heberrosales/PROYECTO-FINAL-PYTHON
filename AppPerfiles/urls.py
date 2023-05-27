from django.urls import path
from AppPerfiles import views
#from AppPerfiles.views import registro, login_view, CustomLogoutView, MiPerfilUpdateView



urlpatterns = [
    path('registro/', views.registro, name="registro"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.CustomLogoutView.as_view(), name="logout"),
    path('editar-mi-perfil/', views.MiPerfilUpdateView.as_view(), name="editar_perfil"),
    path('agregar-avatar/', views.agregar_avatar, name="agregar_avatar"),
]