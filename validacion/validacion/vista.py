from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render

class UserRegisterForm(UserCreationForm):
  username=forms.CharField(label='Nombre de usuario',widget=forms.TextInput)
  email=forms.CharField(label='Correo',widget=forms.EmailInput)
  password1=forms.CharField(label='Contraseña',widget=forms.PasswordInput)
  password2= forms.CharField(label='Repetir Contraseña',widget=forms.PasswordInput)
  
  class Meta:
      model=User
      fields =['username','email','password1','password2']
      

def register(request):
    if request.method== 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
           form.save()
    else:
        form = UserRegisterForm()
    
    return render(request,"registro.html",{"form":form}) 
          
        
    
    