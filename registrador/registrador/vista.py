from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    
    username=forms.CharField(label="nombre de usuario")
    email=forms.CharField(label="correo",widget=forms.EmailInput)
    direccion=forms.CharField(label="Direccion",widget=forms.TextInput)
    password1=forms.CharField(label="contraseña",widget=forms.PasswordInput)
    password2=forms.CharField(label="Repite contraseña",widget=forms.PasswordInput)
    
    class Meta:
        model=User
        
        fields=['username','direccion','email','password1','password2']
        


def register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=UserRegisterForm()
        
        
    return render(request,"register.html",{"form":form})
            

    