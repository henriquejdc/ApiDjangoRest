# Generated by Django 4.0.2 on 2022-02-04 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processos', '0002_remove_processos_equipes'),
        ('equipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipes',
            name='processos',
            field=models.ManyToManyField(to='processos.Processos'),
        ),
    ]
