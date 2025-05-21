from django.db import models

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class Cur_Pessoal(models.Model):
    id = models.BigAutoField(primary_key=True)
    telefone = models.CharField(max_length=16)
    celular  = models.CharField(max_length=16)
    estado   = models.CharField(max_length=2)
    Cidade   = models.CharField(max_length=40)
    bairro   = models.CharField(max_length=40)
    rua      = models.CharField(max_length=40)
    numero   = models.CharField(max_length=4)
    links    = models.CharField(max_length=60)
    user     = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name="user_pessoal")
    

    class Meta:
        managed = True
        db_table = 'cur_pessoal'

class Cur_Academicos(models.Model):
    id = models.BigAutoField(primary_key=True)
    curso      = models.CharField(max_length=40)
    istituicao = models.CharField(max_length=40)
    descricao  = models.CharField(max_length=250)
    dt_inicio  = models.DateField()
    dt_final   = models.DateField()  
    user       = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name="user_academico")

    class Meta:
        managed = True
        db_table = 'cur_academico'

class Cur_Carreiras(models.Model):
    id = models.BigAutoField(primary_key=True)
    cargo     = models.CharField(max_length=40)
    empresa   = models.CharField(max_length=40)
    descricao = models.CharField(max_length=250)
    dt_inicio = models.DateField()
    dt_final  = models.DateField()
    user      =  models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name="user_carreira")

    class Meta:
        managed = True
        db_table = 'cur_carreira'

class Idiomas(models.Model):
    id = models.BigAutoField(primary_key=True)
    Idioma = models.CharField(max_length=40)

    class Meta:
        managed = True
        db_table = 'idiomas'

class Vagas(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome       = models.CharField(max_length=40)
    empresa    = models.CharField(max_length=40)
    descricao  = models.CharField(max_length=250)
    beneficios = models.CharField(max_length=100)
    salario    = models.FloatField(null=True)
    user       = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name="user_vaga")

    class Meta:
        managed = True
        db_table = 'vagas'

class Cursos(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome        = models.CharField(max_length=40)
    descricao   = models.CharField(max_length=100)
    qnt_modulo  = models.IntegerField()
    valor       = models.FloatField()
    gratis      = models.BooleanField() 
    user        =  models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name="user_curso")

    class Meta:
        managed = True
        db_table = 'cursos'

class Modulos(models.Model):
    id = models.BigAutoField(primary_key=True)
    name      = models.CharField( max_length=40)
    conteudo1 = models.CharField(max_length=250)
    conteudo2 = models.CharField(max_length=250)
    conteudo3 = models.CharField(max_length=250)
    conteudo4 = models.CharField(max_length=250)
    conteudo5 = models.CharField(max_length=250)

    class Meta:
        managed = True
        db_table = 'modulos'

class User_Idiomas(models.Model):
    id = models.BigAutoField(primary_key=True)
    nivel  = models.CharField(max_length=20)
    user   =  models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name="user_n_idioma")
    idioma =  models.ForeignKey(Idiomas, on_delete=models.CASCADE, related_name="idioma_n_user")


    class Meta:
        managed = True
        db_table = 'user_idiomas'

class User_Vagas(models.Model):
    id = models.BigAutoField(primary_key=True)
    user   =  models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name="user_n_vaga")
    vaga   =  models.ForeignKey(Vagas, on_delete=models.CASCADE, related_name="vaga_n_user")

    class Meta:
        managed = True
        db_table = 'user_vagas'

class User_Cursos(models.Model):
    id = models.BigAutoField(primary_key=True)
    user   =  models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name="user_n_curso")
    Curso  =  models.ForeignKey(Cursos, on_delete=models.CASCADE, related_name="curso_n_user")
    modulo =  models.ForeignKey(Modulos, on_delete=models.CASCADE, related_name="modulo_curso",null=True)

    class Meta:
        managed = True
        db_table = 'user_cursos'

class Modulos_Cursos(models.Model):
    id = models.BigAutoField(primary_key=True)
    nivel   =  models.IntegerField()
    modulo  =  models.ForeignKey(Modulos, on_delete=models.CASCADE, related_name="modulo_n_curso")
    curso   =  models.ForeignKey(Cursos, on_delete=models.CASCADE, related_name="curso_n_modulo")

    class Meta:
        managed = True
        db_table = 'modulos_cursos'