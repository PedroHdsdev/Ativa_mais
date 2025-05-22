from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login as lg
from django.db.models import Q
from app.models import  AuthUser, AuthGroup, AuthUserGroups, Vagas, User_Vagas
from app.models import Cursos, User_Cursos, Modulos, Modulos_Cursos

def LOGIN(request):
     if request.method == "POST":
          Username = request.POST.get('Username')
          password = request.POST.get('password')

          user = authenticate(username=Username, password=password)
          if user:
               lg(request, user)  
               grups = user.groups.all().first() 
               request.session['grupo'] = grups.name if grups else None

               if grups.name == "Recrutador":
                    vagas = Vagas.objects.filter(user=user)
               else:
                    vagas =  Vagas.objects.all()

               return render(request, 'index_home.html',{'Grups':grups.name, 'T_Vagas':vagas})
          else:
               v_aviso = True
               return render(request, 'index_login.html', {'Aviso':v_aviso})
     
     v_aviso = False
     return render(request, 'index_login.html', {'Aviso':v_aviso})

def CADASTRO(request):
     if request.method == "POST":
          Grupo = request.POST.get('grupo')
          Nome  = request.POST.get('Username')
          password = request.POST.get('password')
          conf_password = request.POST.get('conf_password')
          email = request.POST.get('m_email')

          if password != conf_password:
               v_aviso = True
               return render(request, 'index_cadastro.html')
          else:
               user = User.objects.create_user(
                    username=Nome,
                    email=email,
                    password=password
               )

               try:
                    auth_user = AuthUser.objects.get(username=Nome)
                    auth_group = AuthGroup.objects.get(name=Grupo)
               except AuthUser.DoesNotExist:
                    return render(request, 'index_cadastro.html', {'error': 'Grupo inválido.'})
               
               AuthUserGroups.objects.create(user=auth_user, group=auth_group)

               
          return render(request, 'index_login.html')
     return render(request, 'index_cadastro.html')

def HOME(request):
     if request.user.is_authenticated:
          grupo = request.session.get('grupo')
          query = request.GET.get('Buscar', '')
          
          if grupo == "Recrutador":
               if query:
                    vagas = Vagas.objects.filter( nome__icontains=query,
                                                  user=request.user)
               else:
                    vagas = Vagas.objects.filter(user=request.user)
          else:
               if query:  
                    vagas = Vagas.objects.filter(
                                                  Q(nome__icontains=query) | Q(empresa__icontains=query)
                                                  )
               else:     
                    vagas  = Vagas.objects.all()
          
          return render(request, 'index_home.html',{   'Grups':grupo,
                                                       'T_Vagas':vagas,
                                                       'query':query})     

     return render(request, 'index_login.html')

def CURSOS(request):
     grupo = request.session.get('grupo')

     t_Cursos = Cursos.objects.all()

     return render(request, 'index_cursos.html',{'Grups':grupo})

def PERFIL(request):
     grupo = request.session.get('grupo')
     return render(request, 'index_perfil.html',{'Grups':grupo})

def CAD_VAGAS(request):
     grupo = request.session.get('grupo')
     return render(request, 'index_cad_vagas.html',{'Grups':grupo})

def VAGADETALHES(request, id):
     if request.user.is_authenticated:

          grupo = request.session.get('grupo')
          vaga = Vagas.objects.get(id=id)
          
          return render(request, 'index_vagadetalhes.html',{'Grups':grupo,
                                                            'W_vagas':vaga})
     
     return render(request, 'index_login.html')