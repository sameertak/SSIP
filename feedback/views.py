from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import FeedbackSerializers
from .models import responseModel
from verification.models import phoneModel


class form(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = FeedbackSerializers(data=request.data)
        if serializer.is_valid():
            verify = serializer.validated_data
            tuple_list = list(verify.items())
            key_value = tuple_list[-1]
            mydata = phoneModel.objects.filter(mobile=key_value[1], is_verified=True).values()
            print(mydata[0])
            try:
                mydata[0]['id']
                serializer.save()
                mydata = phoneModel.objects.get(mobile=key_value[1])
                mydata.is_verified = False
                mydata.save()
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            except IndexError:
                return Response({"status": "Phone Number is not verified", "data": serializer.errors}, status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

