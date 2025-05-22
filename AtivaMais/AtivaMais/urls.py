from django.contrib import admin
from django.urls    import path
from app            import views

urlpatterns = [
    path('',views.LOGIN, name='login'),
    path('Cadastro/',views.CADASTRO, name='cadastro'),
    path('home/',views.HOME, name='home'),
    path('cursos/',views.CURSOS, name='cursos'),
    path('perfil/',views.PERFIL, name='perfil'),
    path('CadastroVagas/',views.CAD_VAGAS, name='cadastrovagas'),
    path('vaga/<int:id>/',views.VAGADETALHES, name='vagadetalhes'),
    path('admin/', admin.site.urls),
]