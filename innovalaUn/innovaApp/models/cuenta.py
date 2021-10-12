'''from django.db import models
from .user import User_estudiante

class Cuenta(models.Model):
     idCuenta = models.AutoField(primary_key=True)
     estudianteID = models.ForeignKey(User_estudiante, related_name='estudianteID', on_delete=models.CASCADE)
     lastChangeDate = models.DateTimeField()
     isActive = models.BooleanField(default=True)

     class Meta:
          verbose_name = 'Cuenta'
          verbose_name_plural = 'Cuentas'
          ordering = ['idCuenta']'''