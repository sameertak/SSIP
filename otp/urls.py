from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)
from .views import MyTokenObtainPairView, RegisterHere, VerifyToken, ResetPassword

urlpatterns = [
    path('verify/', include('verification.urls')),
    path('feedback/', include('feedback.urls')),
    path('station/', include('stations.urls')),
    path('admin/', admin.site.urls),
    path('register/', RegisterHere.as_view(), name='Register'),
    path('request-reset/', ResetPassword.as_view(), name='request-reset-password'),
    path('reset/<uidb64>/<token>/', VerifyToken.as_view(), name='password-reset-confirm'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/verify/', TokenVerifyView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
