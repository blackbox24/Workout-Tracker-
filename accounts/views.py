from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import SignUpSerializer

User = get_user_model()


class SignUpView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = SignUpSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        serialized_data = self.serializer_class(data=request.data)
        if serialized_data.is_valid():
            data = serialized_data.validated_data
            if User.objects.filter(username=data.get("username")).exists():
                return Response(
                    {"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST
                )
            user = User.objects.create(
                username=data.get("username"),
                email=data.get("email"),
                first_name=data.get("first_name", ""),
                last_name=data.get("last_name", ""),
            )
            user.set_password(data.get("password1"))
            user.save()
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "message": "User created successfully",
                    "user_id": user.pk,
                    "access": str(refresh.access_token),
                    "refresh": str(refresh),
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
