from django.db import models
from django.conf import settings


# Create your models here.


class Station(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    station_id = models.CharField(max_length=10)
    station_name = models.CharField(max_length=25)
    district = models.CharField(max_length=15)
    subdivision = models.CharField(max_length=10)
    address = models.CharField(default=' ', max_length=100)
    contact = models.CharField(max_length=12)
    pincode = models.CharField(max_length=6)

    def __str__(self):
        return str(self.station_name)
