# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_auto_20150818_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='key',
            field=models.IntegerField(unique=True),
        ),
    ]
