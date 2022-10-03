import json
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from stations.models import Station
from django.core import serializers

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        # Add extra responses here
        data['role'] = self.user.groups.values_list('name', flat=True)
        # context = {
        #     'staions':
        # }
        # print(context)
        data['station_id'] = (Station.objects.filter(email=self.user.id).values())[0]['station_id']
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer