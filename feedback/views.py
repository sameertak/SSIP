from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FeedbackSerializers
from .models import responseModel
from verification.models import phoneModel
import geocoder


class form(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forw_for is not None:
            ip = x_forw_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        add = geocoder.ip(ip)
        city = add.city
        lat_lng = add.latlng

        serializer = FeedbackSerializers(data=request.data)
        if serializer.is_valid():
            verify = serializer.validated_data
            tuple_list = list(verify.items())
            key_value = tuple_list[-1]
            mydata = phoneModel.objects.filter(mobile=key_value[1], is_verified=True).values()

            try:
                mydata[0]['id']
                serializer.save()
                mydata = phoneModel.objects.get(mobile=key_value[1])
                mydata.is_verified = False
                mydata.ip_address = ip
                mydata.city = city
                mydata.lat_lng = lat_lng
                mydata.save()
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            except IndexError:
                return Response({"status": "error", "data": serializer.errors}, status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

