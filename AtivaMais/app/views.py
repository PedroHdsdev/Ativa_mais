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
               vg_aviso = "usuario nao existe"
               return render(request, 'index_login.html',{'vg_aviso'})
    
     return render(request, 'index_login.html')

def CADASTRO(request):
     return render(request, 'index_cadastro.html')

def HOME(request):
     return render(request, 'index_home.html')

def CURSOS(request):
     return render(request, 'index_cursos.html')

def PERFIL(request):
     return render(request, 'index_perfil.html')

def VAGADETALHES(request):
     return render(request, 'index_vagadetalhes.html')