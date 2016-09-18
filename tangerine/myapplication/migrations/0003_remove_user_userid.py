# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0002_auto_20160917_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='userid',
        ),
    ]
