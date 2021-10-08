from rest_framework import serializers
from innovalaUApp.models import comentarios

from innovalaUApp.models.estudiante import User_estudiante
from innovalaUApp.models.comentarios import Comentarios
from innovalaUApp.models.tema import Tema
from innovalaUApp.models.tutoria import Tutoria
from innovalaUApp.models.tutor import Tutor

from innovalaUApp.serializers.comentarioSerializer import ComentariosSerializer
from innovalaUApp.serializers.temaSerializer import TemaSerializer
from innovalaUApp.serializers.tutoriaSerializer import TutoriaSerializer
from innovalaUApp.serializers.tutorSerializer import TutorSerializer

class UserSerializer(serializers.ModelSerializer):
     tutoria = TutoriaSerializer()
     tutor = TutorSerializer()
     comentarios = ComentariosSerializer()
     tema = TemaSerializer()
     class Meta:
          model = User_estudiante
          fields = ['idEstudiante', 'email', 'password', 'nombresEstudiante', 'apellidosEstudiante', 'edadEstudiante', 'tutoria', 'tutor', 'comentarios', 'tema']
     
     def create(self, validated_data_tutoria, validated_data_tutor, validated_data_comentario, validated_data_tema):
          tutoriaData = validated_data_tutoria.pop('tutoria')
          tutorData = validated_data_tutoria.pop('tutor')
          temaData = validated_data_tutoria.pop('tema')
          comentariosData = validated_data_tutoria.pop('comentarios')

          userInstance = User_estudiante.objects.create(**validated_data_tutoria, **validated_data_tutor, **validated_data_comentario, **validated_data_tema)
          Tutoria.objects.create(user=userInstance, **tutoriaData, **tutorData, **temaData, **comentariosData)
          '''
          Tutor.objects.create(user=userInstance, **tutoriaData, **tutorData, **temaData, **comentariosData)
          Tema.objects.create(user=userInstance, **tutoriaData, **tutorData, **temaData, **comentariosData)
          Comentarios.objects.create(user=userInstance, **tutoriaData, **tutorData, **temaData, **comentariosData)
          '''
          return userInstance
          
     def to_representation(self, obj):
          user = User_estudiante.objects.get(idEstudiante=obj.id)
          tutoria = Tutoria.objects.get(estudianteID=obj.id)
          tutor = Tutor.objects.get(tutorID=obj.id)
          comentarios = Comentarios.objects.get(tutoriaID=obj.id)
          tema = Tema.objects.get(TutorID=obj.id)
          
          return {
               'idEstudiante': user.idEstudiante,
               'email': user.email,
               'password': user.password,
               'nombresEstudiante': user.nombresEstudiante,
               'apellidosEstudiante': user.apellidosEstudiante,
               'edadEstudiante': user.edadEstudiante,
               'tutoria': {
                    'idTutoria': tutoria.idTutoria,
                    'tutorID': tutoria.tutorID,
                    'fechaTutoria': tutoria.fechaTutoria,
                    'calificacionTutoria': tutoria.calificacionTutoria
               },
               'comentarios':{
                    'comentarioTutoria': comentarios.comentarioTutoria
               },
               'tutor':{
                    'idTutor': tutor.idTutor,
                    'nombresTutor': tutor.nombresTutor,
                    'apellidosTutor': tutor.apellidosTutor,
                    'emailTutor': tutor.emailTutor,
                    'profesionTutor': tutor.profesionTutor,
                    'experienciaTutor': tutor.experienciaTutor,
                    'calificacionTutor': tutor.calificacionTutor
               },
               'tema':{
                    'tema': tema.tema
               }
          }