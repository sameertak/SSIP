from _datetime import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
import django

# this model Stores the data of the Phones Verified
class phoneModel(models.Model):
    mobile = models.CharField(max_length=13, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return str(self.mobile)
