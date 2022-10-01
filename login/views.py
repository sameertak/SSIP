from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import adminModel
from rest_framework.permissions import IsAuthenticated
from decouple import config
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password


# Create your views here.
class admin_login(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            user = adminModel.objects.get(email=request.data['email'])
        except:
            adminModel.objects.create(
                email=request.data['email'],
                password=make_password(request.data['password'])
            )
            user = adminModel.objects.get(email=request.data['email'])
            user.save()

        return Response({"Data Stored"}, status=200)


class admin_verify(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        email = request.data['email']
        pswd = request.data['password']

        try:
            admin = adminModel.objects.get(email=email)
            if check_password(pswd, admin.password):
                return Response("YES", status=200)
            return Response("NO", status=404)
        except:
            return Response("Doesn't Exist", status=404)
