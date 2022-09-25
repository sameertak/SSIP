from _datetime import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
import django

# this model Stores the data of the Phones Verified
class phoneModel(models.Model):
    Mobile = models.CharField(max_length=13, blank=False)
    created_at = models.DateTimeField(default=django.utils.timezone.now)
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)
    ip_address = models.CharField(default='0.0.0.0', max_length=30)
    city = models.CharField(default='NaN', max_length=15, null=True, blank=True)
    lat_lng = models.CharField(default='NaN', max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.Mobile)
