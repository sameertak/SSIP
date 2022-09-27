from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import adminModel
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class admin_login(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def post(request, mail):
        return Response({"OKAY"}, status=200)