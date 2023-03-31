from rest_framework import serializers
from rest_framework.fields import UUIDField, IntegerField, DateTimeField
from rest_framework.serializers import ModelSerializer

from . import models


class PlayerSerializer(ModelSerializer):
    """Serializer for Player model.

    :returns: PlayerSerializer
    :rtype: rest_framework.serializers.Serializer
    """

    class Meta:
        model = models.Player
        fields = ("uuid", "nick", "rank", "created_at")
        read_only_fields = ("uuid", "rank", "created_at")
