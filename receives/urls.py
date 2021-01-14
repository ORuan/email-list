from django.contrib import admin
from django.urls import path, include
from receives.views import *


urlpatternsadm = [
    path('painel/', register_users, name="painel"),
]
urlpatterns = [
    path('cadastro/', register_users, name="cadastro"),
    path('editar/', edit_users, name="editar"),
    #path('adm/', include((urlpatternsadm, 'adm'), namespace="adm")),
]