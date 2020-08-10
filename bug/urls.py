from django.urls import path
from django.conf.urls import url
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', paginaInicio, name='index'),
    path('result/', analisisImagen, name='result')
    
]