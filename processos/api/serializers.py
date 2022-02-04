from rest_framework import serializers
from processos import models

class ProcessosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Processos
        fields = '__all__' #todos os campos do model id_book, author..