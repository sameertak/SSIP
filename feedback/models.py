from django.db import models

# Create your models here.


class responseModel(models.Model):
    res_id = models.ForeignKey('verification.phoneModel', on_delete=models.CASCADE)
    res1 = models.CharField(max_length=1, blank=False)
    res2 = models.CharField(max_length=1, blank=False)
    res3 = models.CharField(max_length=200)
    res4 = models.CharField(max_length=1, blank=False)

    def __str__(self):
        return str(self.res_id)
