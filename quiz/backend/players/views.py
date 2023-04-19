from typing import List, cast, Any
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from helpers.gen_username.generate import generate_username

from . import models
from . import serializers


class NicknameGeneratorAPIView(APIView):
    """This view is used to suggest a nickname for a new player.
    Return a list of 10 nicknames.
    Authentication is not required.

    :param count: Number of nicknames to generate.
    :type count: int
    :returns: List with 10 nicknames.
    :rtype: list[str]
    """

    def get(self, request) -> Response:
        nicknames: List[str] = generate_username(10)

        return Response(nicknames, status=status.HTTP_200_OK)


class PlayerCreateAPIView(CreateAPIView):
    """Create a new player. Only POST method is allowed.
    No authentication required.

    :returns: PlayerCreateAPIView
    :rtype: rest_framework.generics.CreateAPIView
    """

    queryset = models.Player.objects.all()
    serializer_class = serializers.PlayerSerializer

    def create(self, request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=False)

        if not serializer.errors:
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(
            {"message": "Invalid username."}, status=status.HTTP_406_NOT_ACCEPTABLE
        )


# TODO add authentication to the view below when auth type is decided on
class PlayerRetrieveAPIView(RetrieveAPIView):
    """Retrieve profile data for a specific player.
    No authentication required.

    :returns: PlayerRetrieveAPIView
    :rtype: rest.framework.generics.RetrieveAPIView
    """

    queryset = models.Player.objects.all()
    serializer_class = serializers.PlayerDetailSerializer
    lookup_field = "uuid"
