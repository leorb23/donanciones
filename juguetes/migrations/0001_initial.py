# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donante',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('apellidos', models.CharField(max_length=150)),
                ('identificacion', models.CharField(unique=True, max_length=15)),
                ('nombres', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoJuguete',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('descripcion', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Jugeuete',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='juguetes/')),
                ('estado', models.ForeignKey(to='juguetes.EstadoJuguete')),
            ],
        ),
    ]
