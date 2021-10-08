from innovalaUApp.models.comentarios import Comentarios
from rest_framework import serializers
class ComentariosSerializer(serializers.ModelSerializer):
     class Meta:
          model = Comentarios
          fields = ['tutoriaID', 'comentarioTutoria']