from django.http import HttpResponse
from django.template import loader
import datetime
def hijo(request):
    agno=datetime.datetime.now().year
    mes=datetime.datetime.now().month
    dia=datetime.datetime.now().day
    hora=datetime.datetime.now().hour
    
    fecha="%s/%s/%s a las: %s"% (dia, mes, agno, hora)
    
    plantilla=loader.get_template("hijo.html")
    pagina=plantilla.render({"fecha":fecha})
    
    return HttpResponse(pagina)
    