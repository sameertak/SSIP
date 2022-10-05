import csv

from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FeedbackSerializers
from .models import responseModel
from verification.models import phoneModel
import pandas as pd

class form(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = FeedbackSerializers(data=request.data)
        if serializer.is_valid():
            verify = serializer.validated_data
            tuple_list = list(verify.items())
            mob = tuple_list[-1]

            try:
                verify = phoneModel.objects.filter(mobile=mob[1], is_verified=True).values_list()[0]
                serializer.save()
                mydata = phoneModel.objects.get(mobile=mob[1])
                mydata.is_verified = False
                mydata.save()
                return Response(data={"message": serializer.data}, status=status.HTTP_200_OK)
            except IndexError:
                return Response(
                    status = status.HTTP_404_NOT_FOUND,
                    data={
                        "message": "Phone number is not verified"
                    }
                )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    "message": serializer.errors
                }
            )


class FilterFeedback(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        response = request.data
        global serializer

        district = response["district"]
        subdivision = response["subdivision"]
        rating = response["rating"]
        station_id = response["station_id"]


        if (station_id != "" and rating != "" and district == "" and subdivision == ""):
            q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON f.station_id=s.station_id WHERE s.station_id=" + "'" + station_id + "' AND f.res4=" + "'" + rating + "'"
            queryset = responseModel.objects.raw(q)
            serializer = FeedbackSerializers(queryset, many=True)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )

        if (station_id != "" and rating == "" and district != "" and subdivision == ""):
            q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON f.station_id=s.station_id WHERE s.station_id=" + "'" + station_id + "' AND f.district=" + "'" + district + "'"
            queryset = responseModel.objects.raw(q)
            serializer = FeedbackSerializers(queryset, many=True)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )

        if (station_id != "" and rating == "" and district == "" and subdivision != ""):
            q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON f.station_id=s.station_id WHERE s.station_id=" + "'" + station_id + "' AND f.subdivision=" + "'" + subdivision + "'"
            queryset = responseModel.objects.raw(q)
            serializer = FeedbackSerializers(queryset, many=True)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )

        if (station_id != "" and rating != "" and district == "" and subdivision != ""):
            q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON f.station_id=s.station_id WHERE s.station_id=" + "'" + station_id + "' AND f.res4=" + "'" + rating + "' AND f.subdivision=" + "'" + subdivision + "'"
            queryset = responseModel.objects.raw(q)
            serializer = FeedbackSerializers(queryset, many=True)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )

        if (station_id != "" and rating != "" and district != "" and subdivision == ""):
            q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON f.station_id=s.station_id WHERE s.station_id=" + "'" + station_id + "' AND f.res4=" + "'" + rating + "' AND f.district=" + "'" + district + "'"
            queryset = responseModel.objects.raw(q)
            serializer = FeedbackSerializers(queryset, many=True)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )

        if (station_id != "" and rating == "" and district != "" and subdivision == ""):
            q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON f.station_id=s.station_id WHERE s.station_id=" + "'" + station_id +"' AND f.district=" + "'" + district + "'"
            queryset = responseModel.objects.raw(q)
            serializer = FeedbackSerializers(queryset, many=True)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )

        if (station_id != "" and rating == "" and district != "" and subdivision != ""):
            q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON f.station_id=s.station_id WHERE s.station_id=" + "'" + station_id +"' AND f.district=" + "'" + district + "' AND f.subdivision=" + "'" + subdivision + "'"
            queryset = responseModel.objects.raw(q)
            serializer = FeedbackSerializers(queryset, many=True)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )

        if (district == "" and subdivision == "" and rating == "" and station_id == ""):
            q = "SELECT * FROM feedback_responsemodel"
            queryset = responseModel.objects.raw(q)
            serializer = FeedbackSerializers(queryset, many=True)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )

        if (district != "" and subdivision == "" and rating == "" and station_id == ""):
            q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON f.station_id=s.station_id WHERE s.district=" + "'" + district + "'"
            queryset = responseModel.objects.raw(q)
            serializer = FeedbackSerializers(queryset, many=True)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )

        if (district == "" and subdivision != "" and rating == "" and station_id == ""):
            q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON f.station_id=s.station_id WHERE s.subdivision=" + "'" + subdivision + "'"
            queryset = responseModel.objects.raw(q)
            serializer = FeedbackSerializers(queryset, many=True)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,

            )

        if (district == "" and subdivision == "" and rating != "" and station_id == ""):
            q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON f.station_id=s.station_id WHERE f.res4=" + "'" + rating + "'"
            queryset = responseModel.objects.raw(q)
            serializer = FeedbackSerializers(queryset, many=True)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,

            )

        if (district != "" and subdivision != "" and rating == "" and station_id == ""):
            q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON f.station_id=s.station_id WHERE s.district=" + "'" + district + "' AND s.subdivision=" + "'" + subdivision + "'"
            queryset = responseModel.objects.raw(q)
            serializer = FeedbackSerializers(queryset, many=True)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,

            )

        if (district != "" and subdivision == "" and rating != "" and station_id == ""):
            q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON f.station_id=s.station_id WHERE s.district=" + "'" + district + "' AND f.res4=" + "'" + rating + "'"
            queryset = responseModel.objects.raw(q)
            serializer = FeedbackSerializers(queryset, many=True)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,

            )

        if (district == "" and subdivision != "" and rating != "" and station_id == ""):
            q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON f.station_id=s.station_id WHERE s.subdivision=" + "'" + subdivision + "' AND f.res4=" + "'" + rating + "'"
            queryset = responseModel.objects.raw(q)
            serializer = FeedbackSerializers(queryset, many=True)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,

            )

        if (district != "" and subdivision != "" and rating != "" and station_id == ""):
            q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON f.station_id=s.station_id WHERE s.subdivision=" + "'" + subdivision + "' AND f.res4=" + "'" + rating + "' AND s.district=" + "'" + district + "'"
            queryset = responseModel.objects.raw(q)
            serializer = FeedbackSerializers(queryset, many=True)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )

    def get(self, request):
        try:
            response = HttpResponse(content_type='text/csv')
            writer = csv.writer(response)

            response['Content-Diposition'] = 'attachment; filename="data.csv'
            writer.writerow(['id', 'station_id', 'res1', 'res2', 'res3','res4','created_at','updated_at','res'])

            for ele in (serializer.data):
                writer.writerow(list(ele.values()))

            return response
        except:
            return Response(data={'message':'Unable to access the data'}, status=status.HTTP_400_BAD_REQUEST)