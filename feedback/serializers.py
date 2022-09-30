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
    ip_address = models.CharField(max_length=30)
    city = models.CharField(max_length=15, null=True, blank=True)
    lat_lng = models.CharField(max_length=30, null=True, blank=True)


    class Meta:
        model = responseModel
        fields = ('__all__')
        read_only_fields = ('date_created', 'ip_address')

    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').META.get("REMOTE_ADDR")
        return Loglist.objects.create(**validated_data)
