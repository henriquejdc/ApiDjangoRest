from django.shortcuts import render
from candidatos import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum, Count
# Create your views here.

@api_view(['GET'])
def approved_candidates(request):
    max_cont = models.Candidatos.objects.all().aggregate(sum=Sum('contribuicao'))['sum'] or 0

    front = []
    back = []
    for candidato in models.Candidatos.objects.filter(equipes__tipo_equipe='front-end'):
        front.append({"id": candidato.id,
                      "name": candidato.nome,
                      "contribution": candidato.contribuicao,
                    })
    for candidato in models.Candidatos.objects.filter(equipes__tipo_equipe='back-end'):
        back.append({"id": candidato.id,
                      "name": candidato.nome,
                      "contribution": candidato.contribuicao,
                    })

    return Response({"status": "200",
                     "max_contribution": max_cont,
                        "approved_candidates": {
                         "backend": back,
                         "frontend": front
                        }
                     })