from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login as lg
from django.db.models import Q
from django.db import IntegrityError
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
          userNome  = request.POST.get('Username')
          Nome  = request.POST.get('name') 
          password = request.POST.get('password')
          conf_password = request.POST.get('conf_password')
          email = request.POST.get('m_email')

          if Grupo == None or Grupo == "":
               v_aviso = True
               return render(request, 'index_cadastro.html', {'error': 'Grupo inválido.'})
          else:
               if password != conf_password:
                    return render(request, 'index_cadastro.html', {'error_sh': 'senha inválida.'})
               else:
                    # Verifica se usuário já existe
                    if User.objects.filter(username=userNome).exists():
                         return render(request, 'index_cadastro.html', {'error': 'Usuário já existe.'})

                    try:
                         user = User.objects.create_user(
                              username=userNome,
                              email=email,
                              password=password
                         )

                         #auth_user = User.objects.get(username=userNome)
                         group = Group.objects.get(name=Grupo)
                         #AuthUserGroups.objects.create(user=auth_user, group=auth_group)
                         user.groups.add(group)

                    except AuthGroup.DoesNotExist:
                         return render(request, 'index_cadastro.html', {'error': 'Grupo inválido.'})
               
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
     if request.user.is_authenticated:

          grupo = request.session.get('grupo')
          query = request.GET.get('Buscar', '')

          if query:
               t_Cursos = Cursos.objects.filter(nome__icontains=query)
          else:
               t_Cursos = Cursos.objects.all()

          return render(request, 'index_cursos.html',{ 'Grups':grupo,
                                                       'T_Cursos':t_Cursos})
     
     return render(request, 'index_login.html')

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

def CURSODETALHES(request, id):
     if request.user.is_authenticated:
          if request.method == "POST":
               curso_id = request.POST.get('curso_id')
               curso = Cursos.objects.get(id=curso_id)

               try:
                    User_Curso_obj, created = User_Cursos.objects.get_or_create(
                    user=request.user,
                    Curso=curso  # Corrigido: campo com C maiúsculo!
                    )
               except Cursos.DoesNotExist:
                    print(f"Curso com id {curso_id} não encontrado.")
               # Pode redirecionar para uma página de erro ou mostrar mensagem
               except Exception as e:
                    print(f"Erro ao adicionar curso ao usuário: {e}")

               return CURSOS(request)
          else:

               grupo = request.session.get('grupo')
               curso = Cursos.objects.get(id=id)
          

               return render(request, 'index_cusodetalhes.html',{'Grups':grupo,
                                                                 'W_Curso':curso})
     
     return render(request, 'index_login.html')

def MEUSCURSOS(request):
     if request.user.is_authenticated:

          grupo = request.session.get('grupo')

          user_cursos = User_Cursos.objects.filter(user=request.user).select_related('Curso')

          return render(request, 'index_meuscursos.html',{'Grups':grupo,
                                                            'T_Cursos':user_cursos})

     return render(request, 'index_login.html')

def AULA(request, id):
     if request.user.is_authenticated:

          
          return render(request, 'index_aula.html')
     
     return render(request, 'index_login.html')