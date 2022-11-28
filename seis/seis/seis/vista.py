from django.http import HttpResponse
from django.shortcuts import render

def cargarf(request):
    return render(request,"formulario.html")


def formulario(request): 
    nombre=request.GET["nombre"]
    nacimiento=request.GET["nacimiento"]
    genero=request.GET["genero"]
    mensaje = "Hola %s, su fecha de nacimiento es: %s, escogio el genero: %s"%(nombre,nacimiento,genero)
    return HttpResponse(mensaje)