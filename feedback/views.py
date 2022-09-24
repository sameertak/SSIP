from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FeedbackSerializers
from .models import responseModel

class form(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer = FeedbackSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
#
# from .forms import FeedbackForm
# from .models import responseModel
#
#
# class form(APIView):
#
#     @staticmethod
#     def get(request, res1, res2, res3):
#         responseModel.objects.create(
#             res1=res1,
#             res2=res2,
#             res3=res3
#         )
#
#         Res = responseModel.objects.all()  # user Newly created Model
#         Res.save()
#
#         return Response("Your Feedback is Recorded", status=200)
#
# # from django.shortcuts import render, redirect
# # from django.http import HttpResponse
# #
# #
# # # Create your views here.
# # def homepage(request):
# #     return render(request, "main/home.html")
# #
# #
# # def form(APIView):
# #     if request.method == 'POST':
# #         form = FeedbackForm(request.POST)
# #         if form.is_valid():
# #             body = {
# #                 'res1': form.cleaned_data['res1'],
# #                 'res2': form.cleaned_data['res2'],
# #                 'res3': form.cleaned_data['res3'],
# #             }
# #             message = "\n".join(body.values())
# #
# #             Res = responseModel.objects.get(Feedback = message)
# #
# #             Res.save()
# #             return Response("Feedback has been Recorded", status=200)