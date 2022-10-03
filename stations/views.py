from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from url_filter.integrations.drf import DjangoFilterBackend
from .models import stationModel
from .StationSerialzer import StationSerializer
from rest_framework.response import Response


class Stationdata(APIView):
    pass
    # def post(self, request):
    #
    #     if ('district' in request.data) and:
    #
    #         filtered_data  = Station.objects.filter(district=request.data['district'], subdivision=request.data['subdivision']).values()
    #
    #     return Response({filtered_data}, status=200)