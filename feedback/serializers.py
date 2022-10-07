from rest_framework import serializers
from .models import responseModel
from django.db import models

class FeedbackSerializers(serializers.ModelSerializer):
    station_id = serializers.CharField(max_length=10)
    # created_at = serializers.DateTimeField(auto_now_add=True)
    # updated_at = serializers.DateTimeField(auto_now=True)
    res1 = serializers.CharField(max_length=50)
    res2 = serializers.CharField(max_length=50)
    res3 = serializers.CharField(max_length=300)
    res4 = serializers.CharField(max_length=1)


    class Meta:
        model = responseModel
        fields = ('__all__')
        # read_only_fields = ('date_created', 'ip_address')


class RatingCountSerializer(serializers.ModelSerializer):
    res4 = serializers.CharField(max_length=1)
    count = serializers.CharField(max_length=3)

    class Meta:
        model = responseModel
        fields = ('res4', 'count')

class SubdivisionCountSerializer(serializers.ModelSerializer):
    subdivision = serializers.CharField(max_length=20)
    count = serializers.CharField(max_length=3)

    class Meta:
        model = responseModel
        fields = ('subdivision', 'count')