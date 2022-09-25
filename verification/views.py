from _datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
import pyotp
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import phoneModel
import base64
from twilio.rest import Client
from decouple import config
from rest_framework.permissions import IsAuthenticated
import geocoder
from django.utils import timezone
# Create your models here.
import django

# This class returns the string needed to generate the key
class generateKey:
    @staticmethod
    def returnValue(phone):
        return str(phone) + str(datetime.date(datetime.now())) + "Some Random Secret Key"

# Time after which OTP will expire
EXPIRY_TIME = 50 # seconds

class getPhoneNumberRegistered_TimeBased(APIView):
    permission_classes = (IsAuthenticated,)
    # Get to Create a call for OTP
    @staticmethod
    def get(request, phone):

        context = {}

        x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forw_for is not None:
            ip = x_forw_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        add = geocoder.ip(ip)
        city = add.city
        lat_lng = add.latlng

        try:
            mobile = phoneModel.objects.get(mobile=phone)  # if mobile already exists then take this else create New One
        except ObjectDoesNotExist:
            phoneModel.objects.create(
                mobile=phone,
            )
            mobile = phoneModel.objects.get(mobile=phone)  # user Newly created Model

        mobile.ip_address = ip
        mobile.city = city
        mobile.lat_lng = lat_lng
        mobile.is_verified = False
        mobile.counter += 1
        mobile.save()  # Save the data

        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
        OTP = pyotp.TOTP(key,interval = EXPIRY_TIME)  # TOTP Model for OTP is created

        account_sid = config('account_sid')
        auth_token = config('auth_token')
        from_number = config('from_number')

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f'Your OTP is {OTP.now()}',
            from_=from_number,
            to=f'+91{phoneModel.objects.get(mobile=phone)}'
        )

        # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
        return Response({"OTP": OTP.now(), "id": mobile.id}, status=200)  # Just for demonstration

    # This Method verifies the OTP
    @staticmethod
    def post(request, phone):
        try:
            mobile = phoneModel.objects.get(mobile=phone)
        except ObjectDoesNotExist:
            return Response("User does not exist", status=404)  # False Call

        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Generating Key
        OTP = pyotp.TOTP(key,interval = EXPIRY_TIME)  # TOTP Model 
        if OTP.verify(request.data["otp"]):  # Verifying the OTP
            mobile.is_verified = True
            mobile.save()
            return Response("You are authorised", status=200)
        return Response("OTP is wrong/expired", status=400)
