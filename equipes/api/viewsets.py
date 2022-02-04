from rest_framework import viewsets
from equipes.api import serializers
from equipes import models

class EquipesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EquipesSerializer
    queryset = models.Equipes.objects.all()