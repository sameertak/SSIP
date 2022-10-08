import csv

from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.db.models import Count
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.encoding import smart_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from stations.models import stationModel
from .serializers import FeedbackSerializers, RatingCountSerializer, SubdivisionCountSerializer, \
    AvgRatingCountSerializer
from .models import responseModel
from verification.models import phoneModel


class form(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def post(request):
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
                    status=status.HTTP_404_NOT_FOUND,
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

    @staticmethod
    def post(request):
        response = request.data
        global serializer

        try:
            district = response["district"]
            subdivision = response["subdivision"]
            rating = response["rating"]
            station_id = response["station_id"]
            page = (int(response["pg"]) - 1) * 10

            if station_id != "" and rating == "" and district == "" and subdivision == "":
                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON " \
                    "f.station_id=s.station_id WHERE s.station_id=" + "'" + station_id + f"' ORDER BY f.created_at DESC LIMIT '10' OFFSET '{page}'"
                queryset = responseModel.objects.raw(q)
                serializer = FeedbackSerializers(queryset, many=True)

                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON " \
                    "f.station_id=s.station_id WHERE s.station_id=" + "'" + station_id + f"' ORDER BY f.created_at DESC"
                queryset = responseModel.objects.raw(q)
                serializer1 = FeedbackSerializers(queryset, many=True)

                count = len(serializer1.data)

                return Response(
                    data={
                        "count": count,
                        "data": serializer.data
                    },
                    status=status.HTTP_200_OK,
                )

            if station_id != "" and rating != "" and district == "" and subdivision == "":
                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON " \
                    "f.station_id=s.station_id WHERE s.station_id=" + "'" + station_id + "' AND f.res4=" + "'" + rating + f"' ORDER BY f.created_at DESC LIMIT '10' OFFSET '{page}'"
                queryset = responseModel.objects.raw(q)
                serializer = FeedbackSerializers(queryset, many=True)

                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON " \
                    "f.station_id=s.station_id WHERE s.station_id=" + "'" + station_id + "' AND f.res4=" + "'" + rating + f"' ORDER BY f.created_at DESC"
                queryset = responseModel.objects.raw(q)
                serializer1 = FeedbackSerializers(queryset, many=True)

                count = len(serializer1.data)

                return Response(
                    data={
                        "count": count,
                        "data": serializer.data
                    },
                    status=status.HTTP_200_OK,
                )

            if station_id != "" and rating == "" and district != "" and subdivision == "":
                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON " \
                    "f.station_id=s.station_id WHERE s.station_id=" + "'" + station_id + "' AND f.district=" + "'" + \
                    district + f"' ORDER BY f.created_at DESC LIMIT '10' OFFSET '{page}'"
                queryset = responseModel.objects.raw(q)
                serializer = FeedbackSerializers(queryset, many=True)

                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON " \
                    "f.station_id=s.station_id WHERE s.station_id=" + "'" + station_id + "' AND f.district=" + "'" + \
                    district + f"' ORDER BY f.created_at DESC"
                queryset = responseModel.objects.raw(q)
                serializer1 = FeedbackSerializers(queryset, many=True)

                count = len(serializer1.data)

                return Response(
                    data={
                        "count": count,
                        "data": serializer.data
                    },
                    status=status.HTTP_200_OK,
                )

            if station_id != "" and rating == "" and district == "" and subdivision != "":
                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON " \
                    "f.station_id=s.station_id WHERE s.station_id=" + "'" + station_id + "' AND f.subdivision=" + "'" + \
                    subdivision + f"' ORDER BY f.created_at DESC LIMIT '10' OFFSET '{page}'"
                queryset = responseModel.objects.raw(q)
                serializer = FeedbackSerializers(queryset, many=True)

                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON " \
                    "f.station_id=s.station_id WHERE s.station_id=" + "'" + station_id + "' AND f.subdivision=" + "'" + \
                    subdivision + f"' ORDER BY f.created_at DESC"
                queryset = responseModel.objects.raw(q)
                serializer1 = FeedbackSerializers(queryset, many=True)

                count = len(serializer1.data)

                return Response(
                    data={
                        "count": count,
                        "data": serializer.data
                    },
                    status=status.HTTP_200_OK,
                )

            if station_id != "" and rating != "" and district == "" and subdivision != "":
                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON " \
                    "f.station_id=s.station_id WHERE s.station_id=" + "'" + station_id + "' AND f.res4=" + "'" + \
                    rating + "' AND f.subdivision=" + "'" + subdivision + f"' ORDER BY f.created_at DESC LIMIT '10' OFFSET '{page}'"
                queryset = responseModel.objects.raw(q)
                serializer = FeedbackSerializers(queryset, many=True)

                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON " \
                    "f.station_id=s.station_id WHERE s.station_id=" + "'" + station_id + "' AND f.res4=" + "'" + \
                    rating + "' AND f.subdivision=" + "'" + subdivision + f"' ORDER BY f.created_at DESC"
                queryset = responseModel.objects.raw(q)
                serializer1 = FeedbackSerializers(queryset, many=True)

                count = len(serializer1.data)

                return Response(
                    data={
                        "count": count,
                        "data": serializer.data
                    },
                    status=status.HTTP_200_OK,
                )

            if station_id != "" and rating != "" and district != "" and subdivision == "":
                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON " \
                    "f.station_id=s.station_id WHERE s.station_id=" + "'" + station_id + "' AND f.res4=" + "'" + \
                    rating + "' AND f.district=" + "'" + district + f"' ORDER BY f.created_at DESC LIMIT '10' OFFSET '{page}'"
                queryset = responseModel.objects.raw(q)
                serializer = FeedbackSerializers(queryset, many=True)

                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON " \
                    "f.station_id=s.station_id WHERE s.station_id=" + "'" + station_id + "' AND f.res4=" + "'" + \
                    rating + "' AND f.district=" + "'" + district + f"' ORDER BY f.created_at DESC"
                queryset = responseModel.objects.raw(q)
                serializer1 = FeedbackSerializers(queryset, many=True)

                count = len(serializer1.data)

                return Response(
                    data={
                        "count": count,
                        "data": serializer.data
                    },
                    status=status.HTTP_200_OK,
                )

            if station_id != "" and rating == "" and district != "" and subdivision == "":
                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON " \
                    "f.station_id=s.station_id WHERE s.station_id=" + "'" + station_id + "' AND f.district=" + "'" + \
                    district + f"' ORDER BY f.created_at DESC LIMIT '10' OFFSET '{page}'"
                queryset = responseModel.objects.raw(q)
                serializer = FeedbackSerializers(queryset, many=True)

                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON " \
                    "f.station_id=s.station_id WHERE s.station_id=" + "'" + station_id + "' AND f.district=" + "'" + \
                    district + f"' ORDER BY f.created_at DESC"
                queryset = responseModel.objects.raw(q)
                serializer1 = FeedbackSerializers(queryset, many=True)
                count = len(serializer1.data)

                return Response(
                    data={
                        "count": count,
                        "data": serializer.data
                    },
                    status=status.HTTP_200_OK,
                )

            if station_id != "" and rating == "" and district != "" and subdivision != "":
                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON " \
                    "f.station_id=s.station_id WHERE s.station_id=" + "'" + station_id + "' AND f.district=" + "'" + \
                    district + "' AND f.subdivision=" + "'" + subdivision + f"' ORDER BY f.created_at DESC LIMIT '10' OFFSET '{page}'"
                queryset = responseModel.objects.raw(q)
                serializer = FeedbackSerializers(queryset, many=True)

                q = f"SELECT * FROM feedback_responsemodel ORDER BY feedback_responsemodel.created_at DESC"
                queryset = responseModel.objects.raw(q)
                serializer1 = FeedbackSerializers(queryset, many=True)
                count = len(serializer1.data)

                return Response(
                    data={
                        "count": count,
                        "data": serializer.data
                    },
                    status=status.HTTP_200_OK,
                )

            if district == "" and subdivision == "" and rating == "" and station_id == "":
                q = f"SELECT * FROM feedback_responsemodel ORDER BY feedback_responsemodel.created_at DESC LIMIT '10' OFFSET '{page}'"
                queryset = responseModel.objects.raw(q)
                serializer = FeedbackSerializers(queryset, many=True)

                q = f"SELECT * FROM feedback_responsemodel ORDER BY feedback_responsemodel.created_at DESC"
                queryset = responseModel.objects.raw(q)
                serializer1 = FeedbackSerializers(queryset, many=True)
                count = len(serializer1.data)

                return Response(
                    data={
                        "count": count,
                        "data": serializer.data
                    },
                    status=status.HTTP_200_OK,
                )

            if district != "" and subdivision == "" and rating == "" and station_id == "":
                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON " \
                    "f.station_id=s.station_id WHERE s.district=" + "'" + district + f"' ORDER BY f.created_at DESC LIMIT '10' OFFSET '{page}'"
                queryset = responseModel.objects.raw(q)
                serializer = FeedbackSerializers(queryset, many=True)

                q2 = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON " \
                    "f.station_id=s.station_id WHERE s.district=" + "'" + district + f"' ORDER BY f.created_at DESC"

                queryset = responseModel.objects.raw(q2)
                serializer1 = FeedbackSerializers(queryset, many=True)
                count = len(serializer1.data)

                return Response(
                    data={
                        "count": count,
                        "data": serializer.data
                    },
                    status=status.HTTP_200_OK,
                )

            if district == "" and subdivision != "" and rating == "" and station_id == "":
                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON " \
                    "f.station_id=s.station_id WHERE s.subdivision=" + "'" + subdivision + f"' ORDER BY f.created_at DESC LIMIT '10' OFFSET '{page}'"
                queryset = responseModel.objects.raw(q)
                serializer = FeedbackSerializers(queryset, many=True)

                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON " \
                    "f.station_id=s.station_id WHERE s.subdivision=" + "'" + subdivision + f"' ORDER BY f.created_at"
                queryset = responseModel.objects.raw(q)
                serializer1 = FeedbackSerializers(queryset, many=True)
                count = len(serializer1.data)

                return Response(
                    data={
                        "count": count,
                        "data": serializer.data
                    },
                    status=status.HTTP_200_OK,
                )

            if district == "" and subdivision == "" and rating != "" and station_id == "":
                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON " \
                    "f.station_id=s.station_id WHERE f.res4=" + "'" + rating + f"' ORDER BY f.created_at DESC LIMIT '10' OFFSET '{page}'"
                queryset = responseModel.objects.raw(q)
                serializer = FeedbackSerializers(queryset, many=True)

                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON " \
                    "f.station_id=s.station_id WHERE f.res4=" + "'" + rating + f"' ORDER BY f.created_at DESC LIMIT '10' OFFSET '{page}'"
                queryset = responseModel.objects.raw(q)
                serializer1 = FeedbackSerializers(queryset, many=True)

                count = len(serializer1.data)

                return Response(
                    data={
                        "count": count,
                        "data": serializer.data
                    },
                    status=status.HTTP_200_OK,
                )

            if district != "" and subdivision != "" and rating == "" and station_id == "":
                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON " \
                    "f.station_id=s.station_id WHERE s.district=" + "'" + district + "' AND s.subdivision=" + "'" + \
                    subdivision + f"' ORDER BY f.created_at DESC LIMIT '10' OFFSET '{page}'"
                queryset = responseModel.objects.raw(q)
                serializer = FeedbackSerializers(queryset, many=True)

                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON " \
                    "f.station_id=s.station_id WHERE s.district=" + "'" + district + "' AND s.subdivision=" + "'" + \
                    subdivision + f"' ORDER BY f.created_at"
                queryset = responseModel.objects.raw(q)
                serializer1 = FeedbackSerializers(queryset, many=True)

                count = len(serializer1.data)

                return Response(
                    data={
                        "count": count,
                        "data": serializer.data
                    },
                    status=status.HTTP_200_OK,
                )

            if district != "" and subdivision == "" and rating != "" and station_id == "":
                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON " \
                    "f.station_id=s.station_id WHERE s.district=" + "'" + district + "' AND f.res4=" + "'" + rating + \
                    f"' ORDER BY f.created_at DESC LIMIT '10' OFFSET '{page}'"
                queryset = responseModel.objects.raw(q)
                serializer = FeedbackSerializers(queryset, many=True)

                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON " \
                    "f.station_id=s.station_id WHERE s.district=" + "'" + district + "' AND f.res4=" + "'" + rating + \
                    f"' ORDER BY f.created_at"
                queryset = responseModel.objects.raw(q)
                serializer1 = FeedbackSerializers(queryset, many=True)

                count = len(serializer1.data)

                return Response(
                    data={
                        "count": count,
                        "data": serializer.data
                    },
                    status=status.HTTP_200_OK,
                )

            if district == "" and subdivision != "" and rating != "" and station_id == "":
                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON " \
                    "f.station_id=s.station_id WHERE s.subdivision=" + "'" + subdivision + "' AND f.res4=" + "'" + \
                    rating + f"' ORDER BY f.created_at DESC LIMIT '10' OFFSET '{page}'"
                queryset = responseModel.objects.raw(q)
                serializer = FeedbackSerializers(queryset, many=True)

                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON " \
                    "f.station_id=s.station_id WHERE s.subdivision=" + "'" + subdivision + "' AND f.res4=" + "'" + \
                    rating + f"' ORDER BY f.created_at DESC"
                queryset = responseModel.objects.raw(q)
                serializer1 = FeedbackSerializers(queryset, many=True)

                count = len(serializer1.data)

                return Response(
                    data={
                        "count": count,
                        "data": serializer.data
                    },
                    status=status.HTTP_200_OK,
                )

            if district != "" and subdivision != "" and rating != "" and station_id == "":
                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON " \
                    "f.station_id=s.station_id WHERE s.subdivision=" + "'" + subdivision + "' AND f.res4=" + "'" + \
                    rating + "' AND s.district=" + "'" + district + f"' ORDER BY f.created_at DESC LIMIT '10' OFFSET '{page}'"
                queryset = responseModel.objects.raw(q)
                serializer = FeedbackSerializers(queryset, many=True)

                q = "SELECT f.* FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON " \
                    "f.station_id=s.station_id WHERE s.subdivision=" + "'" + subdivision + "' AND f.res4=" + "'" + \
                    rating + "' AND s.district=" + "'" + district + f"' ORDER BY f.created_at DESC"
                queryset = responseModel.objects.raw(q)
                serializer1 = FeedbackSerializers(queryset, many=True)
                count = len(serializer1.data)

                return Response(
                    data={
                        "count": count,
                        "data": serializer.data
                    },
                    status=status.HTTP_200_OK,
                )

        except MultiValueDictKeyError as e:
            return Response(
                data={
                    'message': f'{e} is not provided'
                },
                status=status.HTTP_404_NOT_FOUND,
            )

    def get(self, request, *args, **kwargs):
        try:
            response = HttpResponse(content_type='application/pcap')
            response['Content-Disposition'] = 'attachment; filename="feedback.csv"'

            writer = csv.writer(response)
            writer.writerow(['Station ID', 'HOW DID YOU COME TO THE POLICE STATION?', 'AFTER HOW MUCH TIME YOU WERE HEARD IN PS?', 'HOW WOULD YOU DESCRIBE YOUR EXPERIENCE WITH POLICE OFFICERS IN THE POLICE STATION?', 'RATINGS', 'created_at'])

            for ele in serializer.data:
                writer.writerow(list(ele.values())[1:-2])

            return response

        except:
            return Response(data={'message': 'Unable to access the data'}, status=status.HTTP_400_BAD_REQUEST)


class GetRatingCount(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = request.data

        try:
            station_id = response["station_id"]

            if station_id != "":
                q = "SELECT stations_stationmodel.id, res4, COUNT(*) AS count FROM feedback_responsemodel INNER JOIN stations_stationmodel ON feedback_responsemodel.station_id = stations_stationmodel.station_id WHERE " \
                    "feedback_responsemodel.station_id =" + "'" + station_id + "' GROUP BY stations_stationmodel.station_id,stations_stationmodel.id," \
                                                                               "res4"
                queryset = responseModel.objects.raw(q)
                serializer = RatingCountSerializer(queryset, many=True)
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK,
                )

            else:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except KeyError as e:
            return Response(
                data={
                    'message': f'{e} is not provided'
                },
                status=status.HTTP_404_NOT_FOUND,
            )


class GetTotalFeedbackCount(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            count = responseModel.objects.all().count()
            return Response(
                count,
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
            )


class GetTotalCountDistrictSubdivision(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        response = request.data
        district = response['district']

        if district != "":
            q = "SELECT stations_stationmodel.id, COUNT(*) AS count FROM feedback_responsemodel INNER JOIN stations_stationmodel ON feedback_responsemodel.station_id = stations_stationmodel.station_id WHERE " \
                "stations_stationmodel.district =" + "'" + district + "' GROUP BY stations_stationmodel.subdivision,stations_stationmodel.id"
            queryset = stationModel.objects.raw(q)

            serializer = SubdivisionCountSerializer(queryset, many=True)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )

class GetCountForEachRating(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        data = responseModel.objects.all().order_by('res4').values("res4").annotate(total=Count('res4'))
        lst = list(data)
        return Response(
            data=lst,
                status=status.HTTP_200_OK
            )

class GetAverageRatings(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        q = "SELECT *, MAX f.id, MAX s.id, AVG(CAST(f.res4 as integer)) AS count FROM feedback_responsemodel f INNER JOIN stations_stationmodel s ON f.station_id=s.station_id GROUP BY s.district"
        # q = "SELECT DISTINCT *, AVG( CAST(feedback_responsemodel.res4 as integer)) AS count FROM feedback_responsemodel INNER JOIN stations_stationmodel ON feedback_responsemodel.station_id = stations_stationmodel.station_id GROUP BY stations_stationmodel.district"
        queryset = stationModel.objects.raw(q)

        serializer = AvgRatingCountSerializer(queryset, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )