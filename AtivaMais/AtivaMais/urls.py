from django.contrib import admin
from django.urls    import path
from app            import views

urlpatterns = [
    path('',views.LOGIN, name='LOGIN'),
    path('Cadastro/',views.CADASTRO, name='CADASTRO'),
    path('home/',views.HOME, name='HOME'),
    path('admin/', admin.site.urls),
]