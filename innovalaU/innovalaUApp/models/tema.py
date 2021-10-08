from django.db import models
from .tutor import Tutor

class Tema(models.Model):
     TutorID = models.ManyToManyField(Tutor)
     tema = models.CharField('Tema', max_length = 50, unique=True)