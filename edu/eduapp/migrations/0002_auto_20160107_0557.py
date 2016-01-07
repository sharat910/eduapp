# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eduapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='course',
            field=models.ForeignKey(to='eduapp.Course'),
        ),
    ]
