from rest_framework import serializers
from .models import responseModel
from django.db import models

class FeedbackSerializers(serializers.ModelSerializer):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    res1 = serializers.CharField(max_length=50)
    res2 = serializers.CharField(max_length=50)
    res3 = serializers.CharField(max_length=300)
    res4 = serializers.CharField(max_length=1)


    class Meta:
        model = responseModel
        fields = ('__all__')
        read_only_fields = ('date_created', 'ip_address')
