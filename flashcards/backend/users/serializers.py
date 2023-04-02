from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer


class CustomUserSerializer(ModelSerializer):
    """Custom user serializer for creating users. Verifies email and password.
    Password is not displayed in response.

    """
    class Meta:
        model = get_user_model()
        fields = ("id", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        instance = self.Meta.model.objects.create_user(**validated_data)
        instance.is_active = True
        return instance
