from rest_framework import serializers
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


class ProfileSerializer(ModelSerializer):
    """Serializer for Profile model.

    :returns: ProfileSerializer
    :rtype: rest_framework.serializers.Serializer
    """

    uuid = serializers.UUIDField(source="player.uuid")
    nick = serializers.CharField(source="player.nick")
    created_at = serializers.DateTimeField(source="player.created_at")
    rank = serializers.IntegerField(source="player.rank")

    class Meta:
        model = models.Profile
        fields = (
            "uuid",
            "nick",
            "created_at",
            "rank",
            "avatar",
            "score",
            "status",
            "is_push_notification",
            "is_findable",
            "is_invitable",
        )
        read_only_fields = ("score", "rank", "created_at", "uuid")
