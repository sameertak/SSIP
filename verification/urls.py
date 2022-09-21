from django.urls import path, include
from .views import getPhoneNumberRegistered_TimeBased

urlpatterns = [
    path("time_based/<phone>/", getPhoneNumberRegistered_TimeBased.as_view(), name="OTP Gen Time Based"),
]