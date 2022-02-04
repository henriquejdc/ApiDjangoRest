from django.db import models
from uuid import  uuid4
from equipes.models import Equipes
from django.core.exceptions import ValidationError
# Create your models here.

class Candidatos(models.Model):
    nome = models.CharField('Nome do Candidato', max_length=255)
    contribuicao = models.IntegerField('Contribuição')
    equipes = models.ManyToManyField(Equipes)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        front = self.equipes.all().filter(tipo_equipe='front-end').exists()
        back = self.equipes.all().filter(tipo_equipe='front-back').exists()

        if front and back:
            tipo = 'Full-Stack'
        elif front:
            tipo = 'Front-End'
        else:
            tipo = 'Back-End'

        return '%s - %s - %s' % (self.id, self.nome, tipo)