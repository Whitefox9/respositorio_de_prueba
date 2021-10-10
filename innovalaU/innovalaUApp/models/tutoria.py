from django.db import models
from .user import User_estudiante


class Tutoria(models.Model):
     idTutoria = models.AutoField(primary_key=True)
     estudianteID = models.ForeignKey(User_estudiante, related_name='estudianteID', on_delete=models.CASCADE)
     #tutorID = models.ForeignKey(Tutor, related_name='tutorID', on_delete=models.CASCADE)
     fechaTutoria = models.DateTimeField()
     calificacionTutoria = models.IntegerField(default=0)