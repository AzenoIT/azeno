from rest_framework.generics import CreateAPIView

from . import models
from . import serializers


class PlayerCreateAPIView(CreateAPIView):
    queryset = models.Player.objects.all()
    serializer_class = serializers.PlayerSerializer
