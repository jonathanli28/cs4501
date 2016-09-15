from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid

class User:
    username = models.CharField(max_length=360)
    first_name = models.CharField(max_length=360)
    last_name = models.CharField(max_length=360)
    date_created = models.DateTimeField(auto_now_add=True)
    userid = models.BigIntegerField(max_length=360)
    #user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

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

    #item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class ItemReview:
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    review = models.TextField(max_length=50000)
    star_rating = size = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])