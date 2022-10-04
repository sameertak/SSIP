from rest_captcha.serializers import RestCaptchaSerializer
from rest_framework import serializers, status
from rest_framework.serializers import Serializer
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

        data['role'] = self.user.groups.values_list('name', flat=True)
        print(self.user.groups.values_list)
        try:
            data['station_id'] = (stationModel.objects.filter(email=self.user.username).values())[0]['station_id']
            return data
        except:
            return data

class GetTokenSerializer(RestCaptchaSerializer, Serializer):
    def verifu(self, po):
        print(po)
        return Response('hmm')

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterHere(APIView):
    def get(self, request):
        username = request.data['username']
        password = request.data['password']
        station_id = request.data['station_id']

        try:
            station = stationModel.objects.get(station_id=station_id)
        except:
            return Response('Station does not exists.', status=status.HTTP_404_NOT_FOUND)
        station.email=username
        station.save()

        try:
            users = User.objects.create_user(username=username, password=password)
            if users:
                users.groups.add(2)
                print(users.groups)
                users.save()
                return Response('Data is stored', status=200)
            else:
                return Response('Data cannot be stored, try again later', status=status.HTTP_502_BAD_GATEWAY)
        except:
            return Response('User Already Exists', status=400)

class HumanOnlyDataSerializer(RestCaptchaSerializer):
    pass