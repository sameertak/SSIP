from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from otp.serializers import ResetPasswordSerializer, NewPasswordSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User

from otp.utils import Util
from stations.models import stationModel
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

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


class ResetPassword(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = ResetPasswordSerializer
    def post(self, request):
        data = {'request':request, 'data':request.data}
        serializer = self.serializer_class(data=data)
        # serializer.is_valid(raise_exception=True)
        email = request.data['email']
        if User.objects.filter(username=email).exists():
            user = User.objects.get(username=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token=PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(request=request).domain
            relativeLink = reverse('password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})
            absurl = 'http://'+current_site+relativeLink
            email_body = f'''
            Hello,
            We recieved a request to reset your password.
            Click on the link to *reset* your password if the action was triggered by you
            {absurl}
            Else Ignore the Mail.'''

            email_subject = '''A Request to reset your password'''
            data={'email_body': email_body, 'to_email': user.username, 'email_subject': email_subject}

            Util.send_email(data)

            return Response(
                data={
                    'message':'''We have sent a link to reset your password on the registered email. Check Spam Folder if not able to find :)'''
                },
                status=status.HTTP_200_OK
            )
        return Response(
            data={
                'message': '''The email id is not associated with the database. Please Contact Admin, if you think it is a mistake.'''
            },
            status=status.HTTP_200_OK
        )


class VerifyToken(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def get(self,request, uidb64, token):
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response(
                    data={
                        "message" : "Token is not valid any more"
                    },
                        status=status.HTTP_401_UNAUTHORIZED
                )

            return Response(
                data={
                    "message" : "Credentials are Valid",
                    "uidb64" : uidb64,
                    "token" : token
                },
                status=status.HTTP_200_OK
            )

        except DjangoUnicodeDecodeError as identifier:
            return Response(
                data={
                    "message": "Token is not valid any more"
                },
                    status=status.HTTP_401_UNAUTHORIZED
            )

class NewPassword(generics.GenericAPIView):
    serializer_class = NewPasswordSerializer
    permission_classes = [AllowAny]
    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            data={
                'message' : 'Password Reset Success'
            },
            status=status.HTTP_200_OK
        )