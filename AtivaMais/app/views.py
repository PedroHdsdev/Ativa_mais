from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as lg

def LOGIN(request):
     if request.method == "POST":
          Username = request.POST.get('Username')
          password = request.POST.get('password')

          user = authenticate(username=Username, password=password)
          if user:
               lg(request, user)         
               return render(request, 'index_home.html')
          else:
               return render(request, 'index_login.html')
    
     return render(request, 'index_login.html')

def CADASTRO(request):
     return render(request, 'index_cadastro.html')

def HOME(request):
     return render(request, 'index_home.html')