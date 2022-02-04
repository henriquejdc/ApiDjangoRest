from rest_framework import serializers
from equipes import models

class EquipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Equipes
        fields = '__all__' #todos os campos do model id_book, author..