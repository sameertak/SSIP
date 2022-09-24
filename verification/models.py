from _datetime import datetime
from django.db import models


# Create your models here.

# this model Stores the data of the Phones Verified
class phoneModel(models.Model):
    Mobile = models.CharField(max_length=13, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)   # For HOTP Verification

    def __str__(self):
        return str(self.Mobile)
