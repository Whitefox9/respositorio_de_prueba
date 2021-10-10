from innovalaUApp.models.cuenta import Cuenta
from rest_framework import serializers
class CuentaSerializer(serializers.ModelSerializer):
     class Meta:
          model = Cuenta
          fields = ['lastChangeDate', 'isActive']