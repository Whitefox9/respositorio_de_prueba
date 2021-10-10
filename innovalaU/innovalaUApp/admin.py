from django.contrib import admin
from .models.user import User_estudiante
from .models.cuenta import Cuenta


admin.site.register(User_estudiante)

admin.site.register(Cuenta)
