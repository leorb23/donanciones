# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('juguetes', '0002_auto_20151121_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juguete',
            name='imagen',
            field=models.ImageField(null=True, upload_to='juguetes/'),
        ),
    ]
