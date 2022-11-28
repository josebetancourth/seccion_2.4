from django.http import HttpResponse 
from django.template import loader
import datetime

def videomusica(request):
    hora = datetime.datetime.now().hour
    minuto = datetime.datetime.now().minute
    segundo = datetime.datetime.now().second
    
    hora = "%s:%s:%s"% (hora,minuto,segundo)
    
    plantilla = loader.get_template("hijo3.html")
    pagina = plantilla.render({"hora":hora})
    
    return HttpResponse(pagina)