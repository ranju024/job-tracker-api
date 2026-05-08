'''
TokenObtainPairView → handles login, returns access + refresh tokens
TokenRefreshView → accepts a refresh token, returns a new access token
'''

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView
from django.urls import path


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
