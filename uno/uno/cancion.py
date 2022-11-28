from django.http import HttpResponse
from django.template import loader
import datetime


def videomusical(request):
    hora = datetime.datetime.now().hour
    minuto = datetime.datetime.now().minute
    segundo = datetime.datetime.now().second
    
    horas = "%s:%s:%s"% (hora,minuto,segundo)
    
    plantilla = loader.get_template("hijo4.html")
    pagina = plantilla.render({"horas":horas})
    
    return HttpResponse(pagina)
    