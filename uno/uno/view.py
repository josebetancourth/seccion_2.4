from django.http import HttpResponse #el objeto HttResponse permite enviar al navegador
import datetime # importa modulo datetime para funcion que toma fecha y hora del sistema

#funcion que envia la frase hola mundo al navegador
def hola(request): #declaracion de una funcion python 
    return HttpResponse("Hola mundo") #envia la frase hola mundo al navegador
#fin funcion


#funcion que toma fecha y hora del sistema y la muestra en el navegador
def fecha(request):
    fechaactual=datetime.datetime.now()#toma la fecha y hora y la guarda en fechactual
    #en la variable documento se almacena un string con HTML para enviar al navegador
    documento=""" 
                <html>
                  <head>
                  </head>  
                  <body>
                    <h1>Esta vista se abrio en: %s</h1>
                  </body>
                </html>
              """% fechaactual #usa el marcador de posicion %s para poner el contenido de la variable fechaactual
    return HttpResponse(documento)
#fin funcion


#funcion que recibe año de nacimiento, futuro y devuelve edad y edad futura
def calculo(request,nacimiento,futuro):
    agnoactual=datetime.datetime.now().year
    edad=agnoactual - nacimiento
    edadfutura=futuro - nacimiento
    documento=""" 
                <html>
                  <head>
                  </head>  
                  <body>
                    <h1>ud tiene: %s años, y en el año %s tendra %s años</h1>
                  </body>
                </html>
              """% (edad,futuro,edadfutura) #usa el marcador de posicion %s para poner el contenido de las variables
    return HttpResponse(documento)
#fin funcion
    

    
    