from django.http import HttpResponse
from django.shortcuts import render
import datetime
def formulario(request):
    return render(request,"formulario.html")

def respuesta(request):
    nombre=request.GET["nombre"]
    genero=request.GET["genero"]
    agnonace=int(request.GET["nacimiento"].split('-')[0])
    agno=datetime.datetime.now().year
    edad=agno - agnonace
    return render(request,"respu.html",{'edad':edad,'genero':genero,'nombre':nombre})

