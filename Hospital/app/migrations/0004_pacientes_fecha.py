# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_consultorio'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacientes',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 11, 4, 20, 23, 33, 873963, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
