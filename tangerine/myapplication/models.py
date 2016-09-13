from django.db import models
from django.contrib.auth.models import User, Group
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid


class BicycleItem:
    picture = models.ImageField(upload_to='bicycle_images', blank=True)
    name = models.CharField(max_length=360)

    bike_style = models.CharField(max_length=360)
    brake_style = models.CharField(max_length=360)
    color = models.CharField(max_length=360)
    frame_material = models.CharField(max_length=360)
    speeds = models.CharField(max_length=360)
    package_height = models.CharField(max_length=360)
    shipping_weight = models.CharField(max_length=360)
    wheel_size = models.CharField(max_length=360)

    bike_description = models.TextField(max_length=50000)

    average_star_rating = size = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(5)])

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class ItemReview:
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    review = models.TextField(max_length=50000)
    star_rating = size = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])