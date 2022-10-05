from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FeedbackSerializers
from .models import responseModel
from verification.models import phoneModel


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
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = request.data
        global serializer
        try:
            station_id = response["station_id"]
            rating = response["rating"]

            if (station_id != "" and rating == ""):
                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON f.station_id=s.station_id WHERE s.station_id=" + "'" + station_id + "'"
                queryset = responseModel.objects.raw(q)
                serializer = FeedbackSerializers(queryset, many=True)
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK,
                )

            if (station_id != "" and rating != ""):
                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON f.station_id=s.station_id WHERE s.station_id=" + "'" + station_id + "' AND f.res4=" + "'" + rating + "'"
                queryset = responseModel.objects.raw(q)
                serializer = FeedbackSerializers(queryset, many=True)
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK,
                )


        except:
            district = response["district"]
            division = response["division"]
            rating = response["rating"]

            if (district == "" and division == "" and rating == ""):
                q = "SELECT * FROM feedback_responsemodel"
                queryset = responseModel.objects.raw(q)
                serializer = FeedbackSerializers(queryset, many=True)
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK,
                )

            if (district != "" and division == "" and rating == ""):
                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON f.station_id=s.station_id WHERE s.district=" + "'" + district + "'"
                queryset = responseModel.objects.raw(q)
                serializer = FeedbackSerializers(queryset, many=True)
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK,
                )

            if (district == "" and division != "" and rating == ""):
                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON f.station_id=s.station_id WHERE s.division=" + "'" + division + "'"
                queryset = responseModel.objects.raw(q)
                serializer = FeedbackSerializers(queryset, many=True)
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK,

                )

            if (district == "" and division == "" and rating != ""):
                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON f.station_id=s.station_id WHERE f.res4=" + "'" + rating + "'"
                queryset = responseModel.objects.raw(q)
                serializer = FeedbackSerializers(queryset, many=True)
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK,

                )

            if (district != "" and division != "" and rating == ""):
                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON f.station_id=s.station_id WHERE s.district=" + "'" + district + "' AND s.division=" + "'" + division + "'"
                queryset = responseModel.objects.raw(q)
                serializer = FeedbackSerializers(queryset, many=True)
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK,

                )

            if (district != "" and division == "" and rating != ""):
                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON f.station_id=s.station_id WHERE s.district=" + "'" + district + "' AND f.res4=" + "'" + rating + "'"
                queryset = responseModel.objects.raw(q)
                serializer = FeedbackSerializers(queryset, many=True)
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK,

                )

            if (district == "" and division != "" and rating != ""):
                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON f.station_id=s.station_id WHERE s.division=" + "'" + division + "' AND f.res4=" + "'" + rating + "'"
                queryset = responseModel.objects.raw(q)
                serializer = FeedbackSerializers(queryset, many=True)
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK,

                )

            if (district != "" and division != "" and rating != ""):
                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON f.station_id=s.station_id WHERE s.division=" + "'" + division + "' AND f.res4=" + "'" + rating + "' AND s.district=" + "'" + district + "'"
                queryset = responseModel.objects.raw(q)
                serializer = FeedbackSerializers(queryset, many=True)
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK,
                )

    def get(self, request):

        return Response(content_type='text/csv', data = serializer.data, status=status.HTTP_200_OK)