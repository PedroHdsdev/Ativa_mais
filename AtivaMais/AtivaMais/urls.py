from django.contrib import admin
from django.urls    import path
from app            import views

urlpatterns = [
    path('',views.LOGIN, name='LOGIN'),
    path('Cadastro/',views.CADASTRO, name='CADASTRO'),
    path('home/',views.HOME, name='HOME'),
    path('cursos/',views.CURSOS, name='cursos'),
    path('perfil/',views.PERFIL, name='perfil'),
    path('vagadetalhes/',views.VAGADETALHES, name='vagadetalhes'),
    path('admin/', admin.site.urls),
]