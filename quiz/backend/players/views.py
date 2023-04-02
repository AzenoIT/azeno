from typing import List

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from helpers.gen_username.generate import generate_username


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
