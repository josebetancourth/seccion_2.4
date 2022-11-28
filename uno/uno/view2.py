from django.http import HttpResponse
from django.template import Template,Context
import datetime


#funcion que renderiza una plantilla que dice hola mundo
def saludar(request):
    archivo=open("uno/plantillas/saludo.html")#abre plantilla
    plantilla=Template(archivo.read())#lee plantilla
    archivo.close()#cierra plantilla
    contexto=Context()#crea el contexto, o las variables que se envian a la plantilla
    documento=plantilla.render(contexto) #guarda plantilla con contexto en documento
    return HttpResponse(documento)#envia a navegador
#fin funcion

    
def fecha2(request):
    fechaactual=datetime.datetime.now()#toma fecha y hora actual del sistema

    #abrir, leer y cerrar plantilla
    archivo=open("uno/plantillas/fecha.html")#abre plantilla
    plantilla=Template(archivo.read())#lee plantilla
    archivo.close()#cierra plantilla

    #crear el contexto y enviar a navegador
    contexto=Context({"fechaactual":fechaactual})#crea el contexto, o las variables que se envian a la plantilla
    documento=plantilla.render(contexto) #guarda plantilla con contexto en documento
    return HttpResponse(documento)#envia a navegador

def lista(request):
    listatareas=["aprender sobre internet","aprender HTML","aprender CSS","practicar python","aprender Django"]
    
    #abrir, leer y cerrar plantilla
    archivo=open("uno/plantillas/listado.html")#abre plantilla
    plantilla=Template(archivo.read())#lee plantilla
    archivo.close()#cierra plantilla

    #crear el contexto y enviar a navegador
    contexto=Context({"listatareas":listatareas})#crea el contexto, o las variables que se envian a la plantilla
    documento=plantilla.render(contexto) #guarda plantilla con contexto en documento
    return HttpResponse(documento)#envia a navegador
    