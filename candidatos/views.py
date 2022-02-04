from django.shortcuts import render
from candidatos import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum, Count
# Create your views here.

# Feito por view também
# @api_view(['GET'])
# def approved_candidates(request):
#     max_cont = models.Candidatos.objects.all().aggregate(sum=Sum('contribuicao'))['sum'] or 0
#
#     front = []
#     back = []
#
#     for candidato in models.Candidatos.objects.filter(equipes__tipo_equipe='front-end'):
#         teams = []
#
#         for equipe in candidatos.equipes.all():
#             processos = []
#
#             for processo in candidatos.processos.all():
#                 processos.append({"id": processo.id, "name": processo.nome})
#
#             teams.append({"id": equipe.id, "name": equipe.nome, "processes": processos})
#
#         front.append({"id": candidato.id,
#                       "name": candidato.nome,
#                       "contribution": candidato.contribuicao,
#                       "teams": teams
#                     })
#
#     for candidato in models.Candidatos.objects.filter(equipes__tipo_equipe='back-end'):
#         back.append({"id": candidato.id,
#                       "name": candidato.nome,
#                       "contribution": candidato.contribuicao,
#                     })
#
#     return Response({"status": "200",
#                      "max_contribution": max_cont,
#                         "approved_candidates": {
#                          "backend": back,
#                          "frontend": front
#                         }
#                      })