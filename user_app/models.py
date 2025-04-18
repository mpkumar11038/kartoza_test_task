from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models as geomodels

# Custom user model extending Django's AbstractUser
class CustomUser(AbstractUser):
    home_address = models.CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        help_text="User's home address"
    )
    phone_number = models.CharField(
        max_length=15, 
        blank=True, 
        null=True, 
        help_text="User's phone number"
    )
    location = geomodels.PointField(
        blank=True, 
        null=True, 
        help_text="Geographical location of the user (latitude and longitude)"
    )  # GeoDjango PointField for storing geographic points

    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"

    def __str__(self):
        return f"{self.username} ({self.email})"