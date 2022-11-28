from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    username=forms.CharField(label='Nombre de usuario')
    email=forms.CharField(label='Correo',widget=forms.EmailInput)
    password1=forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2=forms.CharField(label='Repita contraseña',widget=forms.PasswordInput)
    class Meta:
       model=User 
       
       fields = ['username','email','password1','password2']
       help_texts = {k:"" for k in fields}
       
def register(request):
    if request.method=='POST':
     form=UserRegisterForm(request.POST)
     if form.is_valid():
        username=form.cleaned_data['username'] 
        form.save()
    else:
        form=UserRegisterForm()
    return render(request,"register.html",{"form":form})
     
    