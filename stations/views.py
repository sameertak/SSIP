from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import stationModel
from .StationSerialzer import StationSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class AddStation(APIView):
   permission_classes = [IsAuthenticated]

   def post(self, request):
    response = request.data

    try:
        stationId = response['station_id']

        try:
            stationModel.objects.get(station_id = stationId)

            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={
                    "success": "false",
                    "message": "Station alredy exists"
                    }
            )

        except:

            x = stationModel.objects.create(
                email = response["email"],
                station_id = response["station_id"],
                station_name = response["station_name"],
                district = response["district"],
                subdivision = response["subdivision"],
                address = response["address"],
                contact = response["contact"],
                pincode = response["pincode"],
            )
            if (x == None):
                return Response(
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                    data={
                        "success": "false",
                        "message": "Oops! station didn't create successfully"
                        }
                    )
            return Response(
                    status=status.HTTP_200_OK,
                    data={
                        "success": "true",
                        "message": "Station created successfully"
                    }
            )
    except:
        return Response(
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
            data={
                "success": "false",
                "message": "Please provide correct details"
            }
        )

class GetStationNameById(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request): 
        response = request.data
        station_id = response['station_id']

        try:
            stationName = stationModel.objects.get(station_id = station_id)
            
            return Response(
                status=status.HTTP_200_OK,
                data={
                    "success": "true",
                    "message": stationName.station_name
                }
            )
        except:
            return Response(
                status=status.HTTP_200_OK,
                data={
                    "success": "false",
                    "message": "Station id doesn't exist"
                }
            )

        