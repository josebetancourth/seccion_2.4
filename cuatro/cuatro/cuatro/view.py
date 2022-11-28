from django.http import HttpResponse
from django.shortcuts import render


def formulario(request):
    return render(request,"formulario.html")

def respuesta(request):
    nombre=request.GET["nombre"]
    mensaje="Hola %s, Bienvenido a Django"%nombre
    return HttpResponse(mensaje)