# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0004_itemreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bicycleitem',
            name='average_star_rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], default=1),
        ),
        migrations.AlterField(
            model_name='itemreview',
            name='star_rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], default=1),
        ),
    ]
