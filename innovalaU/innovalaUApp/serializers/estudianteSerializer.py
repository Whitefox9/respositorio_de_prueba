from rest_framework import serializers

from innovalaUApp.models.user import User_estudiante
from innovalaUApp.models.tutoria import Tutoria
'''
from innovalaUApp.models import comentarios
from innovalaUApp.models.comentarios import Comentarios
from innovalaUApp.models.tema import Tema
from innovalaUApp.models.tutor import Tutor

from innovalaUApp.serializers.comentarioSerializer import ComentariosSerializer
from innovalaUApp.serializers.temaSerializer import TemaSerializer
from innovalaUApp.serializers.tutorSerializer import TutorSerializer
'''
from innovalaUApp.serializers.tutoriaSerializer import TutoriaSerializer

class UserSerializer(serializers.ModelSerializer):
     tutoria = TutoriaSerializer()
     class Meta:
          model = User_estudiante
          fields = ['id', 'email', 'password', 'nombresEstudiante', 'apellidosEstudiante', 'edadEstudiante', 'tutoria']
     
     def create(self, validated_data_tutoria):
          tutoriaData = validated_data_tutoria.pop('tutoria')
          '''
          tutorData = validated_data_tutoria.pop('tutor')
          temaData = validated_data_tutoria.pop('tema')
          comentariosData = validated_data_tutoria.pop('comentarios')
          '''
          
          userInstance = User_estudiante.objects.create(**validated_data_tutoria)
          Tutoria.objects.create(estudianteID=userInstance, **tutoriaData)
          '''
          Tutor.objects.create(user=userInstance, **tutoriaData, **tutorData, **temaData, **comentariosData)
          Tema.objects.create(user=userInstance, **tutoriaData, **tutorData, **temaData, **comentariosData)
          Comentarios.objects.create(user=userInstance, **tutoriaData, **tutorData, **temaData, **comentariosData)
          '''
          return userInstance
          
     def to_representation(self, obj):
          user = User_estudiante.objects.get(id=obj.id)
          tutoria = Tutoria.objects.get(estudianteID=obj.id)
          
          return {
               'id': user.idEstudiante,
               'email': user.email,
               'password': user.password,
               'nombresEstudiante': user.nombresEstudiante,
               'apellidosEstudiante': user.apellidosEstudiante,
               'edadEstudiante': user.edadEstudiante,
               'tutoria': {
                    'idTutoria': tutoria.idTutoria,
                    'fechaTutoria': tutoria.fechaTutoria,
                    'calificacionTutoria': tutoria.calificacionTutoria
               }
     }

