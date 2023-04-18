from rest_framework import serializers

from . import models


class BadgeSerializer(serializers.ModelSerializer):
    """A serializer for :class:`stats.models.Badge`.

    This serializer includes following fields:

    * id: The unique identifier of the badge.
    * image_url: The URL of the badge's image.
    * name: The name of the badge.
    * description: The description of the badge.
    * owned_by_user_percentage: The percentage of users who own the badge.
    * points: The number of points the badge is worth.
    * badge_url: The absolute URL of the badge's detail view.

    :ivar image_url: The URL field for image associated with badge instance.
    :type image_url: serializers.URLField
    :ivar badge_url: The URL field for the absolute url of the badge's detail view.
    :type badge_url: serializers.URLField

    """

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
