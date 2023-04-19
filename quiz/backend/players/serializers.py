from rest_framework.serializers import ModelSerializer, CharField

from helpers.validators.validators import validate_profanity
from . import models


class PlayerSerializer(ModelSerializer):
    """Serializer for Player model.

    :returns: PlayerSerializer
    :rtype: rest_framework.serializers.Serializer
    """

    username = CharField(source="nick", required=True, validators=[validate_profanity])

    class Meta:
        model = models.Player
        fields = (
            "uuid",
            "username",
        )
        read_only_fields = ("uuid",)


class PlayerDetailSerializer(ModelSerializer):
    """Serializer for Player model.

    :returns: PlayerSerializer
    :rtype: rest_framework.serializers.Serializer
    """

    username = CharField(source="nick")

    class Meta:
        model = models.Player
        fields = (
            "uuid",
            "username",
            "rank",
            "created_at",
        )
        read_only_fields = ("uuid", "rank", "created_at")
