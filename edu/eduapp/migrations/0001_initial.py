# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('cid', models.CharField(max_length=50)),
                ('nooflectures', models.IntegerField()),
                ('instructorname', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100, blank=True)),
                ('duration', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('lecid', models.IntegerField()),
                ('videoid', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('audio', models.FileField(null=True, upload_to=b'files/%Y/%m/%d', blank=True)),
                ('course', models.ForeignKey(to='eduapp.Course', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(null=True)),
                ('course_comp', models.ManyToManyField(related_name='cc', to='eduapp.Course')),
                ('course_prog', models.ManyToManyField(related_name='cp', to='eduapp.Course')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
