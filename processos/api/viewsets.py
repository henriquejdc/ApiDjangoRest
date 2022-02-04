from rest_framework import viewsets
from processos.api import serializers
from processos import models

class ProcessosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProcessosSerializer
    queryset = models.Processos.objects.all() #tambem todos os campos do nosso modelo