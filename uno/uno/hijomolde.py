from django.http import HttpResponse
from django.template import loader
import datetime

def molde(request):
    agno = datetime.datetime.now().year
    mes = datetime.datetime.now().month
    dia = datetime.datetime.now().day
    
    fecha = "%s / %s / %s"% (dia,mes,agno)
    
    plantilla = loader.get_template("videogamer.html")         
    pagina = plantilla.render({"fecha":fecha})
    
    return HttpResponse(pagina)
