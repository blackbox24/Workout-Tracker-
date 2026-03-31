from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class SignUpSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=20, required=True)
    last_name = serializers.CharField(max_length=20, required=True)

    username = serializers.CharField(max_length=20, required=True)

    email = serializers.CharField(max_length=20, required=True)

    password1 = serializers.CharField(max_length=20, required=True)
    password2 = serializers.CharField(max_length=20, required=True)

    def validate(self, attrs):
        clean_data = super().validate(attrs)
        password1 = clean_data.get("password1")
        password2 = clean_data.get("password2")

        if password1 != password2:
            raise serializers.ValidationError("Passwords do not match")

        return clean_data
