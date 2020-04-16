from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings

# Create your models here.

class Listing_Database(models.Model):
    User = settings.AUTH_USER_MODEL
    user = models.ForeignKey(User, on_delete=models.CASCADE,default="1")
    itemTitle = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=15)
    description = models.TextField()
    price = models.IntegerField()
    county = models.CharField(max_length=30)
    image = models.ImageField(upload_to='house_preview/')


    def __str__(self):
        return f'{self.itemTitle} Listing'

    def save(self, *args, **kwargs):
        super(Listing_Database, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        # if img.height > 500 or img.width > 600:
        output_size = (300,300)
        img.thumbnail(output_size)
        img.save(self.image.path)

