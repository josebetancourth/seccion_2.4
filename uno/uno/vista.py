from django.http import HttpResponse
from django.template import Template,Context

def mensaje(request):
    frase="Hola, esta es una plantilla de Django"
    
    #abrir, leer y cerrar plantilla
    
    archivo=open("uno/plantillas/frase.html")#abre archivo
    plantilla=Template(archivo.read())#leer archivo
    archivo.close()#cerrar archivo
    
    #crear el contexto y renderizar la plantilla con el contexto(variables Backend)
    
    contexto=Context({"frase":frase})#crear contexto
    documento=plantilla.render(contexto)#renderizar plantilla con el contexto
    
    return HttpResponse(documento)


def listado(request):
    tareas=["Aprender HTML","Aprender CSS","Aprender ingles","Repasar Python","Aprender Django","Aprender base de datos"]
    
    #abrir, leer y cerrar plantilla
    
    archivo=open("uno/plantillas/tareas.html")#abre archivo
    plantilla=Template(archivo.read())#leer archivo
    archivo.close()#cerrar archivo
    
    #crear el contexto y renderizar la plantilla con el contexto(variables Backend)
    
    contexto=Context({"lista":tareas})#crear contexto
    documento=plantilla.render(contexto)#renderizar plantilla con el contexto
    
    return HttpResponse(documento)