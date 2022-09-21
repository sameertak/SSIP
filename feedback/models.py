from django.db import models

# Create your models here.


class responseModel(models.Model):
    res1 = models.CharField(max_length=1, blank=False)
    res2 = models.CharField(max_length=1, blank=False)
    res3 = models.CharField(max_length=200)
