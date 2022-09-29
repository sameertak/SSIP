from django.urls import path, include
from .views import admin_login, admin_verify


urlpatterns = [
    path("login/", admin_login.as_view(), name="Admin Login"),
    path("verify/", admin_verify.as_view(), name="Admin Verify")
]