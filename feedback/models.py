
from django.db import models

# Create your models here.
from django.utils import timezone
import django


class responseModel(models.Model):
    res_id = models.ForeignKey('verification.phoneModel', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    res1 = models.CharField(max_length=1, blank=False)
    res2 = models.CharField(max_length=1, blank=False)
    res3 = models.CharField(max_length=300)
    res4 = models.CharField(max_length=1, blank=False)

    def __str__(self):
        return str(self.res_id)
