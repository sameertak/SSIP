import json
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from stations.models import stationModel
from django.core import serializers
from django.conf import settings
from rest_framework.response import Response
from django.contrib.auth.models import User
from stations.models import stationModel

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        # Add extra responses here
        data['role'] = self.user.groups.values_list('name', flat=True)

        try:
            data['station_id'] = (stationModel.objects.filter(email=self.user.username).values())[0]['station_id']
            return data
        except:
            return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterHere(APIView):
    def get(self, request):
        username = request.data['username']
        password = request.data['password']
        role = request.data['role']
        station_id = request.data['station_id']

        station = stationModel.objects.get(station_id=station_id)

        station.email=username
        station.save()
        if role=='Admin':
            role=1
        else:
            role=2
        try:
            users = User.objects.create_user(username=username, password=password)

            if users:
                users.groups.add(role)
                users.save()
                return Response('Data is stored', status=200)
            else:
                return Response('Data cannot be stored, try again later', status=400)
        except:
            return Response('User Already Exists', status=400)