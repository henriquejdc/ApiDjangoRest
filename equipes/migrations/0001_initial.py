# Generated by Django 4.0.2 on 2022-02-03 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome da Equipe')),
                ('tipo_equipe', models.CharField(choices=[('front-end', 'Front-End'), ('back-end', 'Back-End')], default='front-end', max_length=20, verbose_name='Tipo da Equipe')),
                ('criado_em', models.DateField(auto_now_add=True)),
            ],
        ),
    ]