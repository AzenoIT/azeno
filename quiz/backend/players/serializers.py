from rest_framework import serializers
from rest_framework.fields import UUIDField, IntegerField, DateTimeField
from rest_framework.serializers import ModelSerializer

from . import models


class PlayerSerializer(ModelSerializer):
    """Serializer for Player model.

    :returns: PlayerSerializer
    :rtype: rest_framework.serializers.Serializer
    """

    uuid = UUIDField(read_only=True)
    nick = serializers.CharField(max_length=30)
    rank = IntegerField(read_only=True)
    created_at = DateTimeField(read_only=True)

    class Meta:
        model = models.Player
        fields = ("uuid", "nick", "rank", "created_at")
