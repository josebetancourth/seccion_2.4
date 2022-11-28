from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib import messages

def registro(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,"Usuario: %s creado"%username)
    else:
        form = UserCreationForm(request.POST)
    return render(request,"registrar.html",{"form":form})