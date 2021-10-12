'''from django.db import close_old_connections, models
from django.db.models.fields import CharField
from .cuenta import Cuenta
from .tutor import Tutor

class Tutoria(models.Model):
     idTutoria = models.AutoField(primary_key=True)
     tutorID = models.ForeignKey(Tutor, related_name='tutorID', on_delete=models.CASCADE)
     cuentaID = models.ForeignKey(Cuenta, related_name='cuentaID', on_delete=models.CASCADE)
     calificacionTutoria = models.IntegerField(default=0)
     fechaTutoria = models.DateTimeField()
     temaTutoria = models.CharField('temaTutotia', max_length = 50)
     comentario = models.TextField('comentario', blank= True, null=True) 
     '''