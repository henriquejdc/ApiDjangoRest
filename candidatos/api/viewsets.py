from rest_framework import viewsets
from candidatos.api import serializers
from candidatos import models
from django.db.models import Sum, Count
from rest_framework.response import Response

def teams(candidato):
    teams = []
    for equipe in candidato.equipes.all():
        processos = []

        for processo in equipe.processos.all():
            processos.append({"id": processo.id,
                              "name": processo.nome,
                              "end": processo.finalizado_em })

        teams.append({"id": equipe.id, "name": equipe.nome, "processes": processos})

    return teams


class CandidatosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CandidatosSerializer
    queryset = models.Candidatos.objects.all()

class AprovadosViewSet(viewsets.ViewSet):
    def list(self, request):
        max_cont = models.Candidatos.objects.all().aggregate(sum=Sum('contribuicao'))['sum'] or 0
        front = []
        back = []
        full = []
        candidatos_front = models.Candidatos.objects.filter(equipes__tipo_equipe='front-end')
        candidatos_back = models.Candidatos.objects.filter(equipes__tipo_equipe='back-end')

        for candidato in candidatos_front.exclude(id__in=candidatos_back.values_list('id', flat=True)):
            front.append({"id": candidato.id,
                          "name": candidato.nome,
                          "contribution": candidato.contribuicao,
                          "teams": teams(candidato)
                        })
        for candidato in candidatos_back.exclude(id__in=candidatos_front.values_list('id', flat=True)):
            back.append({"id": candidato.id,
                          "name": candidato.nome,
                          "contribution": candidato.contribuicao,
                          "teams": teams(candidato)
                        })

        for candidato in candidatos_back.filter(id__in=candidatos_front.values_list('id', flat=True)):
            full.append({"id": candidato.id,
                          "name": candidato.nome,
                          "contribution": candidato.contribuicao,
                          "teams": teams(candidato)
                        })


        return Response({"status": "200",
                         "max_contribution": max_cont,
                            "approved_candidates": {
                             "backend": back,
                             "frontend": front,
                             "fullstack": full
                            }
                         })