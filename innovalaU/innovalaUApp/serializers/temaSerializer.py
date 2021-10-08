from innovalaUApp.models.tema import Tema
from rest_framework import serializers
class TemaSerializer(serializers.ModelSerializer):
     class Meta:
          model = Tema
          fields = ['TutorID', 'tema']