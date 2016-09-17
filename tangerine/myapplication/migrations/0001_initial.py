# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BicycleItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('picture', models.ImageField(blank=True, upload_to='bicycle_images')),
                ('name', models.CharField(max_length=360)),
                ('bike_style', models.CharField(max_length=360)),
                ('brake_style', models.CharField(max_length=360)),
                ('color', models.CharField(max_length=360)),
                ('frame_material', models.CharField(max_length=360)),
                ('speeds', models.CharField(max_length=360)),
                ('package_height', models.CharField(max_length=360)),
                ('shipping_weight', models.CharField(max_length=360)),
                ('wheel_size', models.CharField(max_length=360)),
                ('bike_description', models.TextField(max_length=50000)),
                ('average_star_rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('username', models.CharField(max_length=360)),
                ('first_name', models.CharField(max_length=360)),
                ('last_name', models.CharField(max_length=360)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('userid', models.BigIntegerField(max_length=360)),
            ],
        ),
    ]
