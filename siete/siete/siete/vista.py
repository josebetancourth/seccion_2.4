from django.shortcuts import render
from materia.models import materia
from django.http import HttpResponse

def inicio(request): #URL: iniciar/
    return render(request,"guardar.html")

def validador(codi,nom,carre,sem):
    error = {} 
    
    #verificar codigo
    if codi == "":#si codigo vacio
        error["codigovacio"] = "el codigo no puede estar vacio"
    elif len(codi) < 3 or len(codi) > 6:# si codigo es meno a 3 o mayor a 6 digitos
        error["codigolargo"] = "el codigo solo puede tener entre 3 y 6 digitos"
    
    for letra in codi:
        if ord(letra) < 48 or ord(letra) > 57:# si codigo tiene letras
            error["codigoletra"] = "el codigo no puede contener letras"
            break
        
    #verificar nombre
    if nom == "":
        error["nombrevacio"] = "el nombre no puede estar vacio"
    elif len(nom) > 15:
        error["nombrelargo"] = "el tamaño max del nombre es de 15 caracteres"
        
    #verificar carrera
    if carre == "":
        error["carreravacio"] = "la carrera no puede estar vacia"
    elif len(carre) > 15:
        error["carreralargo"] = "el tamaño max de la carrera es de 15 caracteres"
    
    #verificar semestre
    if sem == "":
        error["semestrevacio"] = "el semestre no puede estar vacio"
    elif len(sem) > 15:
        error["semestrelargo"] = "el tamaño max del semestre es de 15 caracteres"
                
    return error

def recibe(request): # URL: salvar/
    cod = request.POST["codigo"]
    nom = request.POST["nombre"]
    car = request.POST["carrera"]
    sem = request.POST["semestre"]
    
    status = validador(cod,nom,car,sem) 
     
    if len(list(status.keys())) > 0:
        return render(request,"guardar.html",{"status":status})  
    else:
        materia.objects.create(idmateria=cod,nombre=nom,carrera=car,semestre=sem)
        return HttpResponse("<h1>la informacion se guardo correctamente</h1>")
    
    

     
     
                   
             


    
