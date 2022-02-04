from django.db import models
from uuid import  uuid4
from processos.models import Processos
# Create your models here.

class Equipes(models.Model):
    nome = models.CharField('Nome da Equipe', max_length=255)
    tipo_equipe = models.CharField('Tipo da Equipe',
                                   max_length=20,
                                   choices=(('front-end','Front-End'),('back-end','Back-End')),
                                   default='front-end')
    # Deixei podendo ser nula/branco pela frase "pode ser" e
    # Equipe pode ter candidatos, sem ter ainda um processo ainda.
    processos = models.ManyToManyField(Processos, null=True, blank=True)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s - %s - %s' % (self.id, self.nome, self.get_tipo_equipe_display())