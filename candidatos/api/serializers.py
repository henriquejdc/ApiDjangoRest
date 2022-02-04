from rest_framework import serializers
from candidatos import models

class CandidatosSerializer(serializers.ModelSerializer):
    def validate(self, data):
        dicionario = dict(data)
        front = False
        back = False

        for equipe in dicionario["equipes"]:
            if equipe.tipo_equipe == 'front-end':
                front = True
            if equipe.tipo_equipe == 'back-end':
                back = True

        # Se em equipes back e front = Full tem contribuição de back e front
        if front and back:
            numero = models.Candidatos.objects.all().count() + 1
            if int(dicionario["contribuicao"]) > numero:
                raise serializers.ValidationError('Contribuição Full-Stack Máxima de ' + str(numero) )

        # Se em equipe(s) Front apenas contando a parte de front-end
        elif front:
            numero = models.Candidatos.objects.filter(equipes__tipo_equipe='front-end').count() + 1
            if int(dicionario["contribuicao"]) > numero:
                raise serializers.ValidationError('Contribuição Front-End Máxima de ' + str(numero) )

        # Se em equipe(s) Back apenas contando a parte de back-end
        else:
            numero =  models.Candidatos.objects.filter(equipes__tipo_equipe='back-end').count() + 1
            if int(dicionario["contribuicao"]) > numero:
                raise serializers.ValidationError('Contribuição Back-End Máxima de ' + str(numero) )

        return data

    class Meta:
        model = models.Candidatos
        fields = '__all__'