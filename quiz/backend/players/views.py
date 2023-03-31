from rest_framework.generics import CreateAPIView

from . import models
from . import serializers


class PlayerCreateAPIView(CreateAPIView):
    """Create a new player. Only POST method is allowed.
    No authentication required.

    :returns: PlayerCreateAPIView
    :rtype: rest_framework.generics.CreateAPIView
    """

    queryset = models.Player.objects.all()
    serializer_class = serializers.PlayerSerializer
