from rest_framework import serializers

from . import models


class BadgeSerializer(serializers.ModelSerializer):
    badge_url = serializers.URLField(source="get_absolute_url", read_only=True)

    class Meta:
        model = models.Badge
        fields = (
            "name",
            "description",
            "owned_by_user_percentage",
            "points",
            "image",
            "badge_url",
        )
