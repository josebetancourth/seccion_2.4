from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django import forms

class UserRegisterForm(UserCreationForm):
      username=forms.CharField(label="Nombre de usuario")
      email=forms.CharField(label="correo",widget=forms.EmailInput)
      password1=forms.CharField(label="contraseña",widget=forms.PasswordInput)
      password2=forms.CharField(label="confirma contraseña",widget=forms.PasswordInput)  
      class Meta:
          model=User  
          fields = ['username','email','password1','password2']
          help_texts = { k:"" for k in fields} 
          
def creacion(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            messages.success(request,"usuario %s creado correctamente"%username)
            return redirect("home")
        else:
            messages.error(request,"Error insertando usuario")    
    else:
        form=UserRegisterForm()
        
    return render(request,"registro.html",{"form":form})

def MakeLogin(request):
    if request.method == 'POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            passw = form.cleaned_data.get("password")
            usuario = authenticate(username=usuario,password=passw)
            if usuario is not None:
                login(request,usuario)
                messages.success(request,"Bienvenido %s nuevamente"%usuario)
                return redirect("home") 
            else:
                messages.error(request,"Usuario o clave incorrecta") 
        else:
            messages.error(request,"Usuario o clave incorrecta")    
    else:
        form=AuthenticationForm()
        
    return render(request,"login.html",{"form":form})

def salir(request):
    logout(request)
    messages.success(request,"Sesion cerrada")
    return redirect("home")
def home(request):
    return render(request,"index.html")