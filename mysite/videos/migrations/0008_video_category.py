# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_auto_20150820_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='category',
            field=models.CharField(default='L', choices=[('CS', 'Case Study'), ('L', 'Lesson'), ('P', 'Promo')], max_length=2),
        ),
    ]
