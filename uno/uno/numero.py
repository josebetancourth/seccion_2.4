from urllib.parse import parse_qsl
from django.http import HttpResponse 
from django.template import loader

#funcion o vista que selecciona numeros pares de una lista y los envia al front o plantilla

def number(request):
    lista = [23,45,65,34,21,2,8,5,238,2313,10,11,32,101,242,55]
    pares = []
    
    for numero in lista: #for mejorado que rrecorre la lista
        if numero % 2 == 0: # pregunta si un numero es par
           pares.append(numero) # si lo es lo agrega a la lista pares
    
    #cargamos la plantilla y la renderizamos con el contexto(variables del backend)
    
    plantilla = loader.get_template("par.html")#cargar la plantilla
    pagina = plantilla.render({"pares":pares})#renderizar plantilla y generar pagina HTML puro 
    
    return HttpResponse(pagina)
    
    
            
    
    