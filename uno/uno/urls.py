"""uno URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from uno.cancion import videomusical
from uno.hijo import hijo
from uno.hijomolde import molde
from uno.hijomoldepadre import moldepadre

from uno.lista import pares, tareas
from uno.musica import video
from uno.numero import number
from uno.videomusical import videomusica


from uno.view import calculo, fecha, hola
from uno.view2 import fecha2, lista, saludar
from uno.vista import listado, mensaje

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/',hola),
    path('fecha/',fecha),
    path('calculo/<int:nacimiento>/<int:futuro>/',calculo),
    path('saludar/',saludar),
    path('fecha2/',fecha2),
    path('lista/',lista),
    path('listado/',tareas),
    path('mensaje/',mensaje),
    path('tareas/',listado),
    path('pares/',pares),
    path('listapar/',number),
    path('hereda/',hijo),
    path('musica/',video),
    path('cancion/',videomusical),
    path('video/',videomusica),
    path('molde/',molde),
    path('moldepadre/',moldepadre)
]
