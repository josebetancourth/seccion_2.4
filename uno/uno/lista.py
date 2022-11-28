from django.http import HttpResponse
from django.template import loader


def tareas(request):
    lista_tareas=["Aprender HTML","Aprender CSS","Aprender Django","Repasar Python","Aprender Base de datos"]
    
    plantilla=loader.get_template("tarea.html")
    
    documento=plantilla.render({"lista":lista_tareas})
    
    return HttpResponse(documento)

def pares(request):
    numbers=[1,2,3,4,5,6,7,8]
    pares=[]
    for numero in numbers:
        if numero % 2 == 0:
           pares.append(numero)
            
    
    plantilla=loader.get_template("pares.html")
    
    documento=plantilla.render({"numeros":pares})
    
    return HttpResponse(documento)