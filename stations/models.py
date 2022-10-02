from django.db import models

# Create your models here.


class Station(models.Model):
    station_id = models.CharField(max_length=10)
    station_name = models.CharField(max_length=25)