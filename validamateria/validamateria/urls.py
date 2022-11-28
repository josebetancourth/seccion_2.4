from django.contrib import admin
from django.urls import path
from validador.views import guardar
urlpatterns = [
    path('admin/', admin.site.urls),
    path('guardar/',guardar)
]
