
from django.db import models

# Create your models here.
from django.utils import timezone
import django


class responseModel(models.Model):
    res_id = models.ForeignKey('verification.phoneModel', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    res1 = models.CharField(max_length=50, blank=False)
    res2 = models.CharField(max_length=50, blank=False)
    res3 = models.CharField(max_length=300)
    res4 = models.CharField(max_length=1, blank=False)
    ip_address = models.CharField(max_length=30)
    city = models.CharField(max_length=15, null=True, blank=True)
    lat_lng = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.res_id)
