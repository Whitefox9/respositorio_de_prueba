from django.db import models
from .tutoria import Tutoria

class Comentarios(models.Model):
     tutoriaID = models.ForeignKey(Tutoria, related_name='tutoriaID', on_delete=models.CASCADE)
     comentarioTutoria = models.CharField('Comentario Tutoria', max_length = 500, unique=True)