from django.shortcuts import render

def LOGIN(request):
     return render(request, 'idx_home.html')

def HOME(request):
     return render(request, 'login.html')