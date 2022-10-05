from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import stationModel
from .StationSerialzer import StationSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny


class AddStation(APIView):
   permission_classes = [IsAuthenticated]

   def post(self, request):
    if request.user.groups.all().values_list()[0][1] == 'Admin':
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
    else:
        return Response(
            status=status.HTTP_401_UNAUTHORIZED,
            data={
                "success": "Error",
                "message": "Only Admins are allowed to Add Data"
            }
        )
#
# class RemoveStation(APIView):
#     permission_classes = [IsAuthenticated]

class GetStationNameById(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        response = request.data
        station_id = response['station_id']

        try:
            stationName = stationModel.objects.get(station_id = station_id)
            
            return Response(
                status=status.HTTP_200_OK,
                data={
                    "message": stationName.station_name
                }
            )
        except:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={
                    "message": "Station id doesn't exist"
                }
            )


class GetAllDistrict(APIView):
    permission_classes = [AllowAny]

    def get(self, request):

        try:
            district_data = stationModel.objects.values_list('district').distinct()

            districts = []
            for i in district_data:
                districts.append(i[0])
            return Response(
                status=status.HTTP_200_OK,
                data={
                    "success": "true",
                    "message": districts
                }
            )

        except:
            return Response(
                status=status.HTTP_200_OK,
                data={
                    "success": "false",
                    "message": "Unknown error"
                }
            )


class GetAllSubdivisions(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        # try:
            district = request.data['district']
            district_data = stationModel.objects.filter(district=district).values()

            # subdivision_data = district_data.objects.values_list('subdivision').distinct()
            sub = []
            for i in district_data:
                sub.append(i['subdivision'])

            return Response(
                status=status.HTTP_200_OK,
                data={
                    "success": "true",
                    "message": set(sub)
                }
            )

        # except:
        #     return Response(
        #         status=status.HTTP_200_OK,
        #         data={
        #             "success": "false",
        #             "message": "Unknown error"
        #         }
        #     )
