from django.db import models
from uuid import  uuid4
# Create your models here.

class Processos(models.Model):
    nome = models.CharField('Nome do Processo:', max_length=255)
    criado_em = models.DateField(auto_now_add=True)
    finalizado_em = models.DateField('Finaliza em:')

    def __str__(self):
        return '%s - %s' % (self.id, self.nome)