from django.shortcuts import render

def LOGIN(request):
     if request.method == "POST":
          Username = request.POST.get('Username')
          password = request.POST.get('password')

          return render(request, 'index_home.html')     
     return render(request, 'index_login.html')

def CADASTRO(request):
     return render(request, 'index_cadastro.html')

def HOME(request):
     return render(request, 'index_home.html')