from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response



class Stations(generics.ListAPIView):
    queryset=Station.objects.all()
    serializer_class = StationSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields=('email','password')
    search_fields = ('email','password')

def list(self, request ):
    queryset = self.get_queryset()
    filter_backends = self.filter_queryset(queryset)
    serializer = StationSerializer(filter_backends, many=True)
    return Response(serializer.data)
