from rest_framework import serializers
from processos import models

class ProcessosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Processos
        fields = '__all__'