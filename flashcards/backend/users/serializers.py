from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
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


class CustomUserGetCurrentUserSerializer(ModelSerializer):
    """Custom user serializer for getting current user."""

    class Meta:
        model = get_user_model()
        fields = ("id", "email", "username", "is_staff", "is_superuser", "is_active")


class UpdatePasswordSerializer(serializers.ModelSerializer):
    """Custom update password serializer for updating user password. Verifies current password,
    new password and asks for password confirmation.

    """

    new_password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirmation = serializers.CharField(write_only=True, required=True)
    current_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = ("current_password", "new_password", "password_confirmation")

    def validate(self, attrs):
        if attrs["new_password"] != attrs["password_confirmation"]:
            raise serializers.ValidationError({"new_password": "Password fields didn't match."})
        return attrs

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError({"current_password": "Current password is not correct"})
        return value

    def update(self, instance, validated_data):
        user = self.context["request"].user
        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})
        instance.set_password(validated_data["new_password"])
        instance.save()

        return instance
