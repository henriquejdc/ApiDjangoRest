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

        if front and back:
            numero = models.Candidatos.objects.all().count() + 1
            if int(dicionario["contribuicao"]) > numero:
                raise serializers.ValidationError('Contribuição Full-Stack Máxima de ' + str(numero) )
        elif front:
            numero = models.Candidatos.objects.filter(equipes__tipo_equipe='front-end').count() + 1
            if int(dicionario["contribuicao"]) > numero:
                raise serializers.ValidationError('Contribuição Front-End Máxima de ' + str(numero) )
        else:
            numero =  models.Candidatos.objects.filter(equipes__tipo_equipe='back-end').count() + 1
            if int(dicionario["contribuicao"]) > numero:
                raise serializers.ValidationError('Contribuição Back-End Máxima de ' + str(numero) )

        return data

    class Meta:
        model = models.Candidatos
        fields = '__all__' #todos os campos do model id_book, author..