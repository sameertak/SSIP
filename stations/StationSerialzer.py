from rest_framework import serializers
from stations.models import stationModel
from django.db import models
from django.conf import settings

class StationSerializer(serializers.ModelSerializer):
    email = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    station_id = models.CharField(max_length=10)
    station_name = models.CharField(max_length=25)
    district = models.CharField(max_length=15)
    subdivision = models.CharField(max_length=10)
    address = models.CharField(default=' ', max_length=100)
    contact = models.CharField(max_length=12)
    pincode = models.CharField(max_length=6)

    class Meta:
        model = stationModel
        fields = ('__all__')