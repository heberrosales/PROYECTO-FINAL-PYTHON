from django.urls import path
from AppPerfiles import views

urlpatterns = [
    path('registro/', views.registro, name="registro"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.CustomLogoutView.as_view, name="logout"),

]