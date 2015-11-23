# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_medico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultorio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('horario', models.CharField(max_length=200)),
                ('telefono', models.IntegerField()),
                ('especialidad', models.CharField(max_length=200)),
                ('descripcion_es', models.TextField(max_length=500)),
            ],
        ),
    ]
