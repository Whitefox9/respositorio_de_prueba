from innovalaUApp.models.tutoria import Tutoria
from rest_framework import serializers
class TutoriaSerializer(serializers.ModelSerializer):
     class Meta:
          model = Tutoria
          fields = ['fechaTutoria', 'calificacionTutoria']