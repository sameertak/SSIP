from rest_captcha.serializers import RestCaptchaSerializer
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated
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


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterHere(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.groups.all().values_list()[0][1] == 'Admin':

            try:
                username = request.data['email']
                password = request.data['password']
                station_id = request.data['station_id']

                try:
                    station = stationModel.objects.get(station_id=station_id)

                except:
                    return Response(
                        status=status.HTTP_404_NOT_FOUND,
                        data={
                              'message': 'Station does not exists.'
                        }
                    )

                station.email = username
                station.save()

                try:
                    users = User.objects.create_user(username=username, password=password)
                    if users:
                        users.groups.add(2)
                        print(users.groups)
                        users.save()
                        return Response(
                            status=status.HTTP_200_OK,
                            data={
                                  'message': 'Data is stored'
                            }
                        )
                    else:
                        return Response(
                            status=status.HTTP_502_BAD_GATEWAY,
                            data={
                                  'message':'Data cannot be stored, try again later'
                            }
                        )

                except:
                    return Response(
                        status=status.HTTP_400_BAD_REQUEST,
                        data={
                            'message' : 'User Already Exists'
                        }
                    )
            except:
                return Response(
                    status=status.HTTP_502_BAD_GATEWAY,
                    data={
                        'message' : 'Provide Required Details'
                    }
                )

        else:
            return Response(
                status=status.HTTP_401_UNAUTHORIZED,
                data={
                    "success": "Error",
                    "message": "Only Admins are allowed to Add Data"
                }
            )
