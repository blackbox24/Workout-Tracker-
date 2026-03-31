from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="account_login"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh_token"),
]
