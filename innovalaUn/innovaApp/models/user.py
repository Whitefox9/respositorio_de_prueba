from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from simple_history.models import HistoricalRecords
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def _create_user(self, username, emailEstudiante, nombresEstudiante, apellidosEstudiante, edadEstudiante, password, is_staff, is_superuser, **extra_fields):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(
            username=username,
            emailEstudiante=emailEstudiante,
            nombresEstudiante=nombresEstudiante,
            apellidosEstudiante=apellidosEstudiante,
            edadEstudiante=edadEstudiante,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
            )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self,  username, emailEstudiante, nombresEstudiante, apellidosEstudiante,  edadEstudiante, password=None, **extra_fields):
        return self._create_user(username, emailEstudiante, nombresEstudiante, apellidosEstudiante, edadEstudiante, password, False, False, **extra_fields)
          
    def create_superuser(self,  username, emailEstudiante, nombresEstudiante, apellidosEstudiante, edadEstudiante, password=None, **extra_fields):
        return self._create_user(username, emailEstudiante, nombresEstudiante, apellidosEstudiante,  edadEstudiante, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username', max_length = 50, unique=True)
    emailEstudiante = models.EmailField('Email', max_length = 100, unique=True)
    password = models.CharField('Password', max_length = 256)
    nombresEstudiante = models.CharField('Nombres Estudiante', max_length = 50, blank=True)
    apellidosEstudiante = models.CharField('Apellidos Estudiante', max_length = 50, blank=True)
    edadEstudiante = models.IntegerField(default = 18, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    historical = HistoricalRecords()
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['nombresEstudiante']
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['emailEstudiante', 'nombresEstudiante', 'apellidosEstudiante', 'edadEstudiante']

    def natural_key(self):
        return (self.username)
        
    def __str__(self):
        return f'{self.nombresEstudiante} {self.apellidosEstudiante}'
