from rest_framework import serializers
from innovaApp.models.user import User_estudiante
from innovaApp.models.cuenta import Cuenta
 '''
 from innovalaUApp.models import comentarios
 from innovalaUApp.models.comentarios import Comentarios
 from innovalaUApp.models.tema import Tema
 from innovalaUApp.models.tutor import Tutor
 from innovalaUApp.serializers.comentarioSerializer import ComentariosSerializer
 from innovalaUApp.serializers.temaSerializer import TemaSerializer
 from innovalaUApp.serializers.tutorSerializer import TutorSerializer
 '''
 from innovalaUApp.serializers.cuentaSerializer import CuentaSerializer
 class UserSerializer(serializers.ModelSerializer):
      cuenta = CuentaSerializer()
      class Meta:
           model = User_estudiante
           fields = ['__all__']
    
      def create(self, validated_data):
           cuentaData = validated_data.pop('cuenta')
           '''
           tutorData = validated_data_tutoria.pop('tutor')
           temaData = validated_data_tutoria.pop('tema')
           comentariosData = validated_data_tutoria.pop('comentarios')
           '''
         
           userInstance = User_estudiante.objects.create(**validated_data)
           Cuenta.objects.create(estudianteID=userInstance, **cuentaData)
           '''
           Tutor.objects.create(user=userInstance, **tutoriaData, **tutorData, **temaData, *comentariosData)
           Tema.objects.create(user=userInstance, **tutoriaData, **tutorData, **temaData, *comentariosData)
           Comentarios.objects.create(user=userInstance, **tutoriaData, **tutorData, **temaData, *comentariosData)
           '''
           return userInstance
         
      def to_representation(self, obj):
           user = User_estudiante.objects.get(id=obj.id)
           cuenta = Cuenta.objects.get(estudianteID=obj.id)
         
           return {
                'id': user.idEstudiante,
                'email': user.email,
                'password': user.password,
                'nombresEstudiante': user.nombresEstudiante,
                'apellidosEstudiante': user.apellidosEstudiante,
                'edadEstudiante': user.edadEstudiante,
                'cuenta': {
                     'idCuenta': cuenta.idCuenta,
                     'lastChangeDate': cuenta.lastChangeDate,
                     'isActive': cuenta.isActive
                }
      }

