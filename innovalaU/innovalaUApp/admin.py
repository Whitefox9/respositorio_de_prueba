from django.contrib import admin
from .models.estudiante import User_estudiante
from .models.tutoria import Tutoria
from .models.comentarios import Comentarios
from .models.tutor import Tutor
from .models.tema import Tema

admin.site.register(User_estudiante)
admin.site.register(Comentarios)
admin.site.register(Tutoria)
admin.site.register(Tutor)
admin.site.register(Tema)