from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

from users.serializers import CustomUserSerializer, UpdatePasswordSerializer, CustomUserGetCurrentUserSerializer


class CustomUserCreateView(APIView):
    """Custom Create User View.
    Creates a new account in the application. The user is created with the default values
    for the fields that are not specified in the request.
    Mandatory fields are: email and password. Email must be unique.

    :param str email: User email
    :param str password: User password
    """

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserUpdatePasswordView(UpdateAPIView):
    """Custom Update Password View. To change the password, the user must be authenticated.

    :param str current_password: Current password
    :param str new_password: New password
    :param str password_confirmation: Password confirmation
    """

    queryset = get_user_model().objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdatePasswordSerializer

    def get_object(self):
        return self.request.user


class CustomUserCurrentUserAPIView(APIView):
    """Custom Current User API View. Returns the currently logged-in user.

    :param str email: User email
    :param str password: User password
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = CustomUserGetCurrentUserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CustomUserLogoutViewWithBlacklistTokenReset(APIView):
    """Logout View With Blacklist Token Reset.
    Logs out the user by blacklisting the refresh token. The refresh token is sent in the request body
    as a JSON object with the key "refresh".
    After the refresh token is blacklisted, the user is logged out.

    :param str refresh: Refresh token
    """

    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
        except TokenError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_205_RESET_CONTENT)
