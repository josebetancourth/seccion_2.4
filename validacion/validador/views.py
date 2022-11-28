from django.shortcuts import render
from validador.models import materia
from django.http import HttpResponse

def validador(codigo,nombre,carrera,semestre):
    error = {}
    
    #validacion codigo
    if codigo=="":#valida codigo vacio
        error['codigovacio']='El codigo no puede estar vacio'
    elif len(codigo) < 3 or len(codigo) > 6:#valida tamaño codigo
        error['codigorango']='El codigo solo puede tener entre 3 y 6 digitos'
    for caracter in codigo: 
        if ord(caracter) < 48 or ord(caracter) > 57:#valida codigo sin letras
            error['errorletra']='El codigo solo puede tener numeros'
            break    
    
    #validacion nombre
    if nombre=="":
        error['nombrevacio']='El nombre no puede estar vacio'
    elif len(nombre) > 15:
        error['nombrelargo']='El nombre puede contener max 15 caracteres'
   
   #validacion carrera
    if carrera=="":
        error['carreravacio']='La carrera no puede estar vacia'
    elif len(carrera) > 15:
        error['carreralargo']='La carrera puede contener max 15 caracteres'
        
    #validacion nombre
    if semestre=="":
        error['semestrevacio']='El semestre no puede estar vacio'
    elif len(semestre) > 15:
        error['semestrelargo']='El semestre puede contener max 15 caracteres'     
    
    return error
        
def guardar(request):
  if request.method == 'POST':
      codigo=request.POST["codigo"]
      nombre=request.POST["nombre"]
      carrera=request.POST["carrera"]
      semestre=request.POST["semestre"]
      status=validador(codigo,nombre,carrera,semestre)
      
      if len(list(status.keys())) > 0:
          return render(request,"guardar.html",{"error":status,"codigo":codigo,"nombre":nombre,"carrera":carrera,"semestre":semestre})
      else:
         materia.objects.create(codigo=codigo,nombre=nombre,carrera=carrera,semestre=semestre) 
         return HttpResponse("<h1>La materia se guardo correctamente</h1>")
  else:
      return render(request,"guardar.html")
    
    

