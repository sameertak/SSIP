from .views import FilterFeedback, form, GetRatingCount, GetCSV
from django.urls import path

urlpatterns = [
    path("form/", form.as_view(), name="Feedback Form"),
    path("filter/", FilterFeedback.as_view(), name="Feedback Form"),
    path("rating-count/", GetRatingCount.as_view(), name="Rating Count"),
    path("data/", GetCSV.as_view())
]