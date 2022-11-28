from django.http import HttpResponse
from django.shortcuts import render
import datetime

def formulario(request):
    return render(request,"formulario.html")

def respuesta(request):#request={"nombre":jose,"fecha":2022-1-3,"genero":M}
    nombre=request.GET["nombre"]
    fecha=int(request.GET["fecha"].split("-")[0])
    genero=request.GET["genero"]
    agno=datetime.datetime.now().year
    edad= agno - fecha 
    
    return render(request,"saludo.html",{"nombre":nombre,"genero":genero,"edad":edad})