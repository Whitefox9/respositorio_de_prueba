from django.contrib import admin
from .models.user import User_estudiante
from .models.tutoria import Tutoria


admin.site.register(User_estudiante)

admin.site.register(Tutoria)
