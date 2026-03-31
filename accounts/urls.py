from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="account_login"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh_token"),
    path("signup/", views.SignUpView.as_view(), name="account_signup"),
]
