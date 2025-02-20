from django.urls import path
from .views import logar, registrar, menu, deslogar

urlpatterns = [
    path("login/", logar, name="login"),
    path("registrar/", registrar, name="registrar"),
    path("menu/", menu, name="menu"),
    path("logout/", deslogar, name="logout"),
]
