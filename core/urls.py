from django.contrib import admin
from django.urls import path, include
from core.views import home
from receives.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='HomePage'),
    path('auth/', include(('django.contrib.auth.urls', 'urls'), namespace='auth')), # new
    path('usuarios/', include(('receives.urls', 'receives'), namespace='usuarios')),
    path('painel/', register_users, name="painel"),
    path('', home, name='HomePage'),

]
