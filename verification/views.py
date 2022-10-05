from _datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
import pyotp
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import phoneModel
import base64
from twilio.rest import Client
from decouple import config
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils import timezone
import django
import geocoder


class generateKey:
    @staticmethod
    def returnValue(phone):
        return str(phone) + str(datetime.date(datetime.now()))

EXPIRY_TIME = 50


class getPhoneNumberRegistered_TimeBased(APIView):
    permission_classes = [AllowAny]
    @staticmethod
    def get(request, phone):
        x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forw_for is not None:
            ip = x_forw_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        add = geocoder.ip(ip)
        city = add.city
        lat_lng = add.latlng

        try:
            mobile = phoneModel.objects.get(mobile=phone)
        except ObjectDoesNotExist:
            phoneModel.objects.create(
                mobile=phone,
                ip_address=ip,
                is_verified=False,
                city=city,
                lat_lng=lat_lng
            )
            mobile = phoneModel.objects.get(mobile=phone)
        mobile.counter += 1
        mobile.save()

        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
        OTP = pyotp.TOTP(key,interval = EXPIRY_TIME)  # TOTP Model for OTP is created

        account_sid = config('account_sid')
        auth_token = config('auth_token')
        from_number = config('from_number')

        client = Client(account_sid, auth_token)
        phone_no = phoneModel.objects.get(mobile=phone)
        client.messages.create(
            body=f'Your OTP is {OTP.now()}',
            from_=from_number,
            to=f'+91{phone_no.mobile}'
        )

        return Response(
            status=status.HTTP_200_OK,
            data={
                "id": mobile.id
            }
        )

    @staticmethod
    def post(request, phone):
        try:
            mobile = phoneModel.objects.get(mobile=phone)
        except ObjectDoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={
                    "User does not exist"
                }
            )

        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())
        OTP = pyotp.TOTP(key,interval = EXPIRY_TIME)
        if OTP.verify(request.data["otp"]):
            mobile.is_verified = True
            mobile.save()
            return Response(
                status=status.HTTP_200_OK,
                data={
                    "You are authorised"
                }
            )

        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={
                "OTP is Wrong/Expired"
            }
        )
