from django.contrib import admin
from django.urls import path, include
from core.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='HomePage'),
    path('usuarios/', include(('receives.urls', 'receives'), namespace='usuarios')),
    path('', home, name='HomePage'),
]
