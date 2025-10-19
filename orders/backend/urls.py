# urls.py
from django.urls import path
from .views import (
    RegistrationAPIView,
    LoginAPIView,
)

urlpatterns = [
    path('auth/register/', RegistrationAPIView.as_view(), name='register'),
    path('auth/login/', LoginAPIView.as_view(), name='login'),
]