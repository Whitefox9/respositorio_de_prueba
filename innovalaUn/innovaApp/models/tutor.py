'''from django.db import models

class Tutor(models.Model):
     idTutor = models.AutoField(primary_key=True)
     nombresTutor = models.CharField('Nombres Tutor', max_length = 50,)
     apellidosTutor = models.CharField('Apellidos Tutor', max_length = 50)
     emailTutor = models.EmailField('Email Tutor', max_length = 100, unique=True)
     profesionTutor = models.CharField('Profesión Tutor', max_length = 50)
     experienciaTutor = models.CharField('ExperienciaTutor', max_length = 50)
     calificacionTutor = models.IntegerField(default = 0)'''