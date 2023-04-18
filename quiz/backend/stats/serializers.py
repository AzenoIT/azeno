from rest_framework import serializers

from . import models


class BadgeSerializer(serializers.ModelSerializer):
    image_url = serializers.URLField(source="image", read_only=True)
    badge_url = serializers.URLField(source="get_absolute_url", read_only=True)

    class Meta:
        model = models.Badge
        fields = (
            "id",
            "image_url",
            "name",
            "description",
            "owned_by_user_percentage",
            "points",
            "badge_url",
        )
