# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('juguetes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('donante', models.ForeignKey(to='juguetes.Donante')),
            ],
        ),
        migrations.CreateModel(
            name='Juguete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='juguetes/')),
                ('estado', models.ForeignKey(to='juguetes.EstadoJuguete')),
            ],
        ),
        migrations.RemoveField(
            model_name='jugeuete',
            name='estado',
        ),
        migrations.DeleteModel(
            name='Jugeuete',
        ),
        migrations.AddField(
            model_name='donacion',
            name='juguete',
            field=models.ForeignKey(to='juguetes.Juguete'),
        ),
    ]
