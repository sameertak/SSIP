from django.urls import path, include, re_path
from .views import Stationdata

urlpatterns = [
    re_path('filter/', Stationdata.as_view()),
]