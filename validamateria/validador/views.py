from django.shortcuts import render
from validador.models import materia
from django.http import HttpResponse


def validacion(codigo,nombre,carrera,semestre): 
    error={}
    #validar codigo
    if codigo=="":
        error['codigovacio']='El codigo no puede estar vacio'
    else:
        if len(codigo) < 3 or len(codigo) > 6:
            error['codigorango'] = 'El codigo solo puede tener entre 3 y 6 digitos'
        for caracter in codigo:  
            if ord(caracter) < 48 or ord(caracter) > 57:
                error['errorletra']='El codigo solo puede contener numeros'
                break
    #validar nombre            
    if nombre=="":
        error['nombrevacio']='EL nombre no puede estar vacio'
    elif len(nombre) > 15:
        error['nombrelargo']='El nombre no puede tener mas de 15 caracteres'
      #validar carrera            
    if carrera=="":
        error['carreravacio']='La carrera no puede estar vacio'
    elif len(carrera) > 15:
        error['carreralargo']='La carrera no puede tener mas de 15 caracteres'
      #validar semestre            
    if semestre=="":
        error['semestrevacio']='EL semestre no puede estar vacio'
    elif len(semestre) > 15:
        error['semestrelargo']='El semestre no puede tener mas de 15 caracteres'        
    return error    

def guardar(request):
    if request.method == 'POST':
       codigo=request.POST['codigo'] 
       nombre=request.POST['nombre']
       carrera=request.POST['carrera']
       semestre=request.POST['semestre']
       status=validacion(codigo,nombre,carrera,semestre)
       
       if len(list(status.keys())) > 0:
           contexto={"error":status,"codigo":codigo,"nombre":nombre,"carrera":carrera,"semestre":semestre}
           return render(request,"guardar.html",contexto)
       else:
            materia.objects.create(codigo=codigo,nombre=nombre,carrera=carrera,semestre=semestre)
            return HttpResponse("La materia se guardo correctamente") 
    else:
        return render(request,"guardar.html") 
    
    
      
       
       
       
    
    
       
       
        
