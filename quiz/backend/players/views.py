from typing import List

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from helpers.gen_username.generate import generate_username


class NicknameGeneratorAPIView(APIView):
    """This view is used to suggest a nickname for a new player.
    Pass query parameter `count` to specify the number of nicknames to generate, default is 1.
    Authentication is not required.

    :param count: Number of nicknames to generate.
    :type count: int
    :returns: A list of nicknames.
    :rtype: list[str]
    """

    def get(self, request) -> Response:
        count: int = int(self.request.query_params.get("count", 1))
        nicknames: List[str] = generate_username(count)

        return Response(nicknames, status=status.HTTP_200_OK)
