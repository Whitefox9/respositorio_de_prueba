# from innovalaUApp.models.tutoria import Tutoria
# from innovalaUApp.models.cuenta import Cuenta
# from innovalaUApp.models.tutor import Tutor

# from rest_framework import serializers

# from innovalaUApp.serializers.estudianteSerializer import UserSerializer
# class TutoriaSerializer(serializers.ModelSerializer):
#      user = UserSerializer()
#      class Meta:
#           model = Tutoria
#           fields = ['idTutoria', 'calificacionTutoria', 'fechaTutoria', 'temaTutoria', 'comentario', 'cuenta', 'tutor']

#      def create(self, validated_data, validated_data_tutor):
#           cuentaData = validated_data.pop('cuenta')
#           tutorData = validated_data_tutor.pop('tutor')
#           userInstance = Tutoria.objects.create(**validated_data)
#           Cuenta.objects.create(estudianteID=userInstance, **cuentaData, **tutorData)
#           Tutor.objects.create(tutorID=userInstance, **tutorData)
#           return userInstance

#      def to_representation(self, obj):
#           tutoria = Tutoria.objects.get(idTutoria=obj.id)
#           cuenta = Cuenta.objects.get(estudianteID=obj.id)
#           tutor = Tutor.objects.get(tutorID=obj.id)
          
#           return {
#                'idTutoria': tutoria.idTutoria,
#                'calificacionTutoria': tutoria.calificacionTutoria,
#                'fechaTutoria': tutoria.fechaTutoria,
#                'temaTutoria': tutoria.temaTutoria,
#                'comentario': tutoria.comentario,
#                'cuenta': {
#                     'idCuenta': cuenta.idCuenta,
#                     'lastChangeDate': cuenta.lastChangeDate,
#                     'isActive': cuenta.isActive
#                },
#                'tutor': {
#                     'idTutor': tutor.idTutor,
#                     'nombresTutor': tutor.nombresTutor,
#                     'apellidosTutor': tutor.apellidosTutor,
#                     'emailTutor': tutor.emailTutor,
#                     'profesionTutor': tutor.profesionTutor,
#                     'experienciaTutor': tutor.experienciaTutor,
#                     'calificacionTutor': tutor.calificacionTutor
#                }
#      }
