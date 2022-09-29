
from django.db import models

# Create your models here.
from django.utils import timezone
import django


class responseModel(models.Model):
    res_id = models.ForeignKey('verification.phoneModel', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    res1 = models.CharField(max_length=25, blank=False)
    res2 = models.CharField(max_length=25, blank=False)
    res3 = models.CharField(max_length=200)
    res4 = models.CharField(max_length=1, blank=False)
    ip_address = models.CharField(default='0.0.0.0', max_length=30)
    city = models.CharField(default='NaN', max_length=15, null=True, blank=True)
    lat_lng = models.CharField(default='NaN', max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.res_id)
