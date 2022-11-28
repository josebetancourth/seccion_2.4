
from django.contrib import admin
from django.urls import path
from validador.views import guardar
from validacion.vista import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('guardar/',guardar),
    path('register/',register)
]
