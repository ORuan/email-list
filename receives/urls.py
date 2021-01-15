from django.contrib import admin
from django.urls import path, include
from receives.views import *
from django.contrib.auth.urls import *

urlpatterns = [
    path('cadastro/', register_users, name="cadastro"),
    path('edicao/', edit_users, name="editar"),
    path('perfil/', view_user, name="verperfil"),
]