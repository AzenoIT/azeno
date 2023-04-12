from rest_framework import serializers

from .models import Deck


class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ("id", "name", "author", "price", "category", "popularity", "rating",
                  "is_public", "is_active", "description", "image")
