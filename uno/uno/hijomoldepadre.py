from django.http import HttpResponse
from django.template import loader
import datetime

def moldepadre(request):
    dia = datetime.datetime.now().day
    mes = datetime.datetime.now().month
    agno = datetime.datetime.now().year
    
    fecha = "%s / %s / %s"% (dia,mes,agno)
            
    plantilla = loader.get_template("gamermoldepadre.html")
    pagina = plantilla.render({"fecha":fecha})
    
    return HttpResponse(pagina)

