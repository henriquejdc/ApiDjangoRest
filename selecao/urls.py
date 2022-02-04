from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from equipes.api import viewsets as equipesviewsets
from candidatos.api import viewsets as candidatosviewsets
from processos.api import viewsets as processosviewsets

from candidatos import views


route = routers.DefaultRouter()
route.register(r'equipes', equipesviewsets.EquipesViewSet, basename='Equipes')
route.register(r'candidatos', candidatosviewsets.CandidatosViewSet, basename='Candidatos')
route.register(r'processos', processosviewsets.ProcessosViewSet, basename='Processos')
route.register(r'api/selection_process/approved_candidates', candidatosviewsets.AprovadosViewSet, basename='Teste')


urlpatterns = [
    path('', include(route.urls)),
# Outro modo de chamar pela view, entretanto não aparece o registro para acesso simplificado.
#     path('api/selection_process/approved_candidates/', views.approved_candidates),
]
